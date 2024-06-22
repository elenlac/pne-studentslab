import http.server
import http.client
from http import HTTPStatus
import socketserver
from termcolor import *
from pathlib import Path
import os
from urllib.parse import urlparse, parse_qs, quote
import jinja2 as j
import json
from Seq import Seq

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


def read_html_template(file_name):  # RETURNS A TEMPLATE, we don't use it with basic_index.html (static)
    file_path = os.path.join("html", file_name)  # create the path to the file (valid for every os)
    contents = Path(file_path).read_text()  # create an object of class Path to read the file
    contents = j.Template(contents)  # GENERATE A jinja2 TEMPLATE (use it to generate dynamic content)
    return contents


def request_to_ensembl(url):
    server = "rest.ensembl.org"  # the IP of the ensembl server
    error = False
    info = None
    try:
        connection = http.client.HTTPSConnection(server)
        connection.request("GET", url)
        response = connection.getresponse()
        if response.status == HTTPStatus.OK:
            info = json.loads(response.read().decode())
        else:
            error = True
            print(f"HTTP error occurred: {response.status} {response.reason}")
        connection.close()
    except Exception as e:
        error = True
        print(f"Exception occurred: {e}")
    return error, info


def obtain_gene_id(gene_name, endpoint):
    resource = f"/homology/symbol/human/" + gene_name
    params = 'content-type=application/json;format=condensed'
    url = f"{resource}?{params}"
    error, info = request_to_ensembl(url)
    contents = ""
    code = HTTPStatus.OK
    gene_id = None
    if not error:
        # print(f"Gene id data: {data}")
        gene_id = info["data"][0]["id"]
    else:
        error_message = "Gene ID not found"
        context = {
            'endpoint': endpoint,
            'message': error_message
        }
        contents = read_html_template("error.html").render(context=context)
        code = HTTPStatus.NOT_FOUND
    return gene_id, contents, code


def handle_endpoint(endpoint, parameters):
    code = HTTPStatus.OK  # establish "200" as default

    if endpoint == "/":
        file_path = os.path.join("html", "index.html")
        contents = Path(file_path).read_text()

    elif endpoint == "/listSpecies":
        resource = "/info/species"
        params = "content-type=application/json"
        url = f"{resource}?{params}"
        error, info = request_to_ensembl(url)
        if not error:
            all_species = info['species']  # list<dict>, each species is a dict
            limit = parameters.get("limit")  # REMEMBER LIMIT IS OPTIONAL("None" as default)
            if limit:
                limit = int(limit[0])
            else:
                limit = len(all_species)

            print(f"List species data: {info}")

            names = []
            for s in all_species[:limit]:  # will iterate through the list of dicts
                names.append(s['display_name'])

            contents = read_html_template("species.html").render(context={'species_num': len(all_species),
                                                                          'limit': limit, 'names': names})
        else:
            error_message = "Something went wrong"
            context = {
                'endpoint': endpoint,
                'message': error_message
            }
            contents = read_html_template("error.html").render(context=context)
            code = HTTPStatus.SERVICE_UNAVAILABLE  # we change code to "503"

    elif endpoint == "/karyotype":
        resource = "/info/assembly"
        params = "content-type=application/json"
        species = parameters.get('species')[0]
        quote_species = quote(species)
        # sent with good format -> change blank space with appropriate html format. FOR INTRODUCING INTO URL ONLY
        url = f"{resource}/{quote_species}?{params}"
        error, info = request_to_ensembl(url)
        if not error:
            print(f"Karyotype data: {info}")

            chrom_karyotype = info['karyotype']
            contents = read_html_template("karyotype.html").render(context={'species': species,
                                                                            'karyotype_chromosomes': chrom_karyotype})
        else:
            error_message = "Something went wrong"
            context = {
                'endpoint': endpoint,
                'message': error_message
            }
            contents = read_html_template("error.html").render(context=context)
            code = HTTPStatus.SERVICE_UNAVAILABLE

    elif endpoint == "/chromosomeLength":
        resource = "/info/assembly"
        params = "content-type=application/json"
        species = parameters.get('species')[0]
        chosen_chromo = parameters.get('chromo')[0]  # not always an integer!!!
        url = f"{resource}/{species}?{params}"
        error, info = request_to_ensembl(url)
        if not error:
            print(f"Chromosome length data: {info}")

            list_of_chromo = info['top_level_region']
            # obtain all chromosomes of the specie, it is an array of objects

            length = None
            for chromo in list_of_chromo:
                if chromo['name'] == chosen_chromo:
                    length = chromo['length']
                    break

            contents = read_html_template("chromosome_length.html").render(context={'length': length,
                                                                                    'chromosomes_list': list_of_chromo,
                                                                                    'chromo': chosen_chromo,
                                                                                    'species': species})
        else:
            error_message = "Something went wrong"
            context = {
                'endpoint': endpoint,
                'message': error_message
            }
            contents = read_html_template("error.html").render(context=context)
            code = HTTPStatus.SERVICE_UNAVAILABLE

    elif endpoint == "/geneSeq":
        gene_name = parameters.get('gene')[0]
        gene_id, error_contents, error_code = obtain_gene_id(gene_name, endpoint)

        # print(f"Gene: {gene_name} - Gene ID: {gene_id}")

        if gene_id:
            resource = "/sequence/id"
            params = "content-type=application/json"
            url = f"{resource}/{gene_id}?{params}"
            error, info = request_to_ensembl(url)
            if not error:
                print(f"Human gene sequence data: {info}")
                sequence = info["seq"]
                contents = read_html_template("human_gene.html").render(context={'gene': gene_name, 'bases': sequence})
            else:
                error_message = "Something went wrong"
                context = {
                    'endpoint': endpoint,
                    'message': error_message
                }
                contents = read_html_template("error.html").render(context=context)
                code = HTTPStatus.SERVICE_UNAVAILABLE
        else:
            contents = error_contents
            code = error_code

    elif endpoint == "/geneInfo":
        gene_name = parameters.get('gene')[0]
        gene_id, error_contents, error_code = obtain_gene_id(gene_name, endpoint)

        # print(f"Gene: {gene_name} - Gene ID: {gene_id}")

        if gene_id:
            resource = "/overlap/id"
            params = "content-type=application/json;feature=gene"
            url = f"{resource}/{gene_id}?{params}"
            error, info = request_to_ensembl(url)
            if not error:
                print(f"Gene info data: {info}")
                start = info[0]["start"]
                end = info[0]["end"]
                length = end - start
                chromosome = info[0]['seq_region_name']
                contents = read_html_template("gene_info.html").render(context={'id': gene_id, 'gene': gene_name,
                                                                                'start': start, 'end': end,
                                                                                'length': length,
                                                                                'chromosome': chromosome})
            else:
                error_message = "Something went wrong"
                context = {
                    'endpoint': endpoint,
                    'message': error_message
                }
                contents = read_html_template("error.html").render(context=context)
                code = HTTPStatus.SERVICE_UNAVAILABLE
        else:
            contents = error_contents
            code = error_code

    elif endpoint == "/geneCalc":
        gene_name = parameters.get('gene')[0]
        gene_id, error_contents, error_code = obtain_gene_id(gene_name, endpoint)
        print(f"Gene: {gene_name} - Gene ID: {gene_id}")

        if gene_id:
            resource = "/sequence/id/"
            params = "content-type=application/json;feature=gene"
            url = f"{resource}{gene_id}?{params}"
            error, info = request_to_ensembl(url)
            if not error:
                print(f"Gene calc data: {info}")
                sequence = info["seq"]
                s = Seq(sequence)
                calc = s.info().replace("\n", "<br><br>")
                #  could also introduce in "context" 'length': s.len() and 'info': s.info()
                contents = read_html_template("gene_calculations.html").render(context={'calc': calc,
                                                                                        'gene': gene_name})
            else:
                error_message = "Something went wrong"
                context = {
                    'endpoint': endpoint,
                    'message': error_message
                }
                contents = read_html_template("error.html").render(context=context)
                code = HTTPStatus.SERVICE_UNAVAILABLE
        else:
            contents = error_contents
            code = error_code

    elif endpoint == "/geneList":
        user_chromosome = parameters['chromo'][0]
        start = parameters['start'][0]
        end = parameters['end'][0]
        resource = "/overlap/region/human/"
        params = "content-type=application/json"
        url = (
            f"{resource}{user_chromosome}:{start}-{end}?{params};feature=gene;feature=transcript;"
            f"feature=cds;feature=exon")
        error, info = request_to_ensembl(url)
        if not error:
            print(f"Gene list data: {info}")
            # data is a list of the human genes that are located on the X chromosome from start to finish/end

            genes_list = []
            for i in info:  # every "i"=gene is a dictionary of the list of dicts "data"
                if i['feature_type'] == "gene":
                    if i.get("external_name"):
                        genes_list.append(i.get("external_name"))

            if len(genes_list) == 0:
                genes_list.append("There are no genes in this region")

            contents = read_html_template("gene_list.html").render(context={'chromo_number': user_chromosome,
                                                                            'genes': genes_list, 'start': start,
                                                                            'end': end})
        else:
            error_message = "Something went wrong"
            context = {
                'endpoint': endpoint,
                'message': error_message
            }
            contents = read_html_template("error.html").render(context=context)
            code = HTTPStatus.SERVICE_UNAVAILABLE

    return code, contents


class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # inherits functionality for handling different types of HTTP requests,
    # but also overrides specific methods of it to customise behaviour of the server

    def do_GET(self):

        print(colored(f"Request line: {self.requestline}", 'green'))
        print(f"URL: {self.path}")
        parsed_url = urlparse(self.path)  # slices the url into attributes contained in the ParseResult object
        print(f"URL fragments: {parsed_url}")
        endpoint = parsed_url.path
        print(colored(f"Endpoint: {endpoint}", "blue"))
        parameters = parse_qs(parsed_url.query)  # takes the info in 'query' and creates a dictionary -> {key:[]}
        print(colored(f"Parameters: {parameters}", "blue"))

        content_type = "text/html"
        code, contents = handle_endpoint(endpoint, parameters)

        self.send_response(code)
        contents_bytes = contents.encode()  # transform to bytes to send the contents through the network
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(contents_bytes)))
        self.end_headers()
        # finish sending HTTP headers to the client, after the server will start sending the body

        self.wfile.write(contents_bytes)
        # writes the content of the response (body) to the output stream, preparing it to be sent to the client


with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print("Serving at PORT...", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:  # Ctrl+C
        print()
        print("Stopped by the user")
        httpd.server_close()  # server_socket is closed and port is free
