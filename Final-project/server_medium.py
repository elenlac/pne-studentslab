import http.server
from http import HTTPStatus
import socketserver
from termcolor import *
from pathlib import Path
import os
from urllib.parse import urlparse, parse_qs, quote
import jinja2
import json
from Seq import Seq

"""BASIC & MEDIUM LEVEL SERVER"""
PORT = 8080
ENSEMBL_SERVER = "rest.ensembl.org"  # the IP of the ensembl server
HTML_FOLDER = "html"  # optional, since we could have the html files in the same directory as the server
RESOURCE_TO_ENSEMBL_REQUEST = {
    '/listSpecies': {'resource': "/info/species", 'params': "content-type=application/json"},
    '/karyotype': {'resource': "/info/assembly", 'params': "content-type=application/json"},
    '/chromosomeLength': {'resource': "/info/assembly", 'params': "content-type=application/json"},
    '/geneSeq': {'resource': "/sequence/id", 'params': "content-type=application/json"},
    '/geneInfo': {'resource': "/overlap/id", 'params': "content-type=application/json;feature=gene"},
    '/geneCalc': {'resource': "/sequence/id/", 'params': "content-type=application/json;feature=gene"},
    '/geneList': {'resource': "/overlap/region/human/", 'params': "content-type=application/json"}
}  # dict that contains a resource/endpoint as key with a dict as value. we state what we will request to ensembl
RESOURCE_NOT_AVAILABLE_ERROR = "Resource not available"
ENSEMBL_COMMUNICATION_ERROR = "Error in communication with the Ensembl server"
GENES = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]  # for reference
IDs = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}


def read_html_template(file_name):  # RETURNS A TEMPLATE, we don't use it with basic_index.html (static)
    file_path = os.path.join(HTML_FOLDER, file_name)  # create the path to the file (valid for every os)
    contents = Path(file_path).read_text()  # create an object of class Path to read the file
    contents = jinja2.Template(contents)  # GENERATE A jinja2 TEMPLATE (use it to generate dynamic content)
    return contents


def server_request(server, url):  # server: ENSEMBL_SERVER. url: the one requested
    import http.client  # local import, as we are only using it in this function

    error = False
    data = None
    try:  # if everything is ok, data = content and error = False
        connection = http.client.HTTPSConnection(server)  # object that establishes a secure connection to the server
        connection.request("GET", url)  # sends the GET request
        response = connection.getresponse()  # obtains the http response in bytes, contains a status code (not in bytes)
        if response.status == HTTPStatus.OK:
            json_str = response.read().decode()  # read the bytes, decode them and get the str json format
            data = json.loads(json_str)  # load the file into a python object
        else:
            error = True
    except Exception:  # ANY error in the communication with server, data = None and error = True
        error = True
    return error, data  # returns a duple


def handle_error(endpoint, message):  # endpoint: resource received from user. message: str response
    context = {
        'endpoint': endpoint,
        'message': message
    }
    return read_html_template("error.html").render(context=context)


def list_species(endpoint, parameters):
    request = RESOURCE_TO_ENSEMBL_REQUEST[endpoint]
    url = f"{request['resource']}?{request['params']}"
    error, data = server_request(ENSEMBL_SERVER, url)
    if not error:
        limit = None  # REMEMBER LIMIT IS OPTIONAL("None" as default)
        if 'limit' in parameters:
            limit = int(parameters['limit'][0])

        print(f"List species data: {data}")

        species = data['species']  # list<dict>, each species is a dict
        name_species = []
        for specie in species[:limit]:  # will iterate through the list of dicts
            name_species.append(specie['display_name'])
        context = {
            'number_of_species': len(species),
            'limit': limit,
            'name_species': name_species
        }
        contents = read_html_template("species.html").render(context=context)
        code = HTTPStatus.OK
    else:
        contents = handle_error(endpoint, ENSEMBL_COMMUNICATION_ERROR)
        code = HTTPStatus.SERVICE_UNAVAILABLE  # we change code to "503"
    return code, contents  # returns a duple


def karyotype(endpoint, parameters):
    request = RESOURCE_TO_ENSEMBL_REQUEST[endpoint]
    coded_species = quote(parameters['species'][0])
    # sent with good format-> change blank space with appropriate html format. FOR INTRODUCING INTO URL ONLY
    decoded_species = parameters['species'][0]
    url = f"{request['resource']}/{coded_species}?{request['params']}"
    error, data = server_request(ENSEMBL_SERVER, url)
    if not error:
        print(f"Karyotype data: {data}")

        karyotype_chromosomes = data['karyotype']
        context = {
            'species': decoded_species,
            'karyotype_chromosomes': karyotype_chromosomes
        }
        contents = read_html_template("karyotype.html").render(context=context)
        code = HTTPStatus.OK
    else:
        contents = handle_error(endpoint, ENSEMBL_COMMUNICATION_ERROR)
        code = HTTPStatus.SERVICE_UNAVAILABLE
    return code, contents


def chromosome_length(endpoint, parameters):
    request = RESOURCE_TO_ENSEMBL_REQUEST[endpoint]
    species = parameters['species'][0]
    user_chromosome = parameters['chromo'][0]  # not always an integer!!!
    url = f"{request['resource']}/{species}?{request['params']}"
    error, data = server_request(ENSEMBL_SERVER, url)
    if not error:
        print(f"Chromosome length data: {data}")

        chromosomes_list = data['top_level_region']  # obtain all chromosomes of the specie, it is an array of objects

        length = None
        for chromo in chromosomes_list:  # will iterate the list of dicts
            if chromo['name'] == user_chromosome:  # REQUESTED CHROMOSOME HAS BEEN FOUND, no need to keep searching
                length = chromo['length']
                break

        """OTHER WAY TO DO IT:
        length = None
        found = False
        i = 0  # index starts at 0
        while not found and i < len(chromosomes_list):  # not found = True
            chromo = chromosomes_list[i]
            if chromo['name'] == user_chromosome:  # WE HAVE FOUND THE REQUESTED CHROMOSOME 
                length = chromo['length']
                found = True
            i += 1
        """
        context = {
            'length': length,
            'chromosomes_list': chromosomes_list,
            'chromo': user_chromosome,
            'species': species
        }
        contents = read_html_template("chromosome_length.html").render(context=context)
        code = HTTPStatus.OK
    else:
        contents = handle_error(endpoint, ENSEMBL_COMMUNICATION_ERROR)
        code = HTTPStatus.SERVICE_UNAVAILABLE
    return code, contents


def get_id(gene):  # petition to the ensembl server where given a gene we transform it into its identifier id
    species = "human"
    symbol = gene
    resource = f"/homology/symbol/{species}/{symbol}"
    params = 'content-type=application/json;format=condensed'
    url = f"{resource}?{params}"
    error, data = server_request(ENSEMBL_SERVER, url)
    gene_id = None  # in case we ask a nonhuman gene
    if not error:
        # print(f"Gene id data: {data}")
        gene_id = data["data"][0]["id"]
    return gene_id


def human_gene(endpoint, parameters):
    gene = parameters['gene'][0]
    gene_id = get_id(gene)
    print(f"Gene: {gene} - Gene ID: {gene_id}")

    if gene_id is not None:
        request = RESOURCE_TO_ENSEMBL_REQUEST[endpoint]
        url = f"{request['resource']}/{gene_id}?{request['params']}"
        error, data = server_request(ENSEMBL_SERVER, url)
        if not error:
            print(f"Human gene sequence data: {data}")
            bases = data["seq"]
            context = {
                'gene': gene,
                'bases': bases
            }
            contents = read_html_template("human_gene.html").render(context=context)
            code = HTTPStatus.OK
        else:
            contents = handle_error(endpoint, ENSEMBL_COMMUNICATION_ERROR)
            code = HTTPStatus.SERVICE_UNAVAILABLE
        return code, contents


def gene_info(endpoint, parameters):
    gene = parameters['gene'][0]
    gene_id = get_id(gene)
    print(f"Gene: {gene} - Gene ID: {gene_id}")

    if gene_id is not None:
        request = RESOURCE_TO_ENSEMBL_REQUEST[endpoint]
        url = f"{request['resource']}/{gene_id}?{request['params']}"
        error, data = server_request(ENSEMBL_SERVER, url)
        if not error:
            print(f"Gene info data: {data}")
            start = data[0]["start"]
            end = data[0]["end"]
            length = end - start
            chromosome = data[0]['seq_region_name']
            context = {
                'id': gene_id,
                'gene': gene,
                'start': start,
                'end': end,
                'length': length,
                'chromosome': chromosome
            }
            contents = read_html_template("gene_info.html").render(context=context)
            code = HTTPStatus.OK
        else:
            contents = handle_error(endpoint, ENSEMBL_COMMUNICATION_ERROR)
            code = HTTPStatus.SERVICE_UNAVAILABLE
        return code, contents


def gene_calc(endpoint, parameters):
    gene = parameters['gene'][0]
    gene_id = get_id(gene)
    print(f"Gene: {gene} - Gene ID: {gene_id}")

    if gene_id is not None:
        request = RESOURCE_TO_ENSEMBL_REQUEST[endpoint]
        url = f"{request['resource']}{gene_id}?{request['params']}"
        error, data = server_request(ENSEMBL_SERVER, url)
        if not error:
            print(f"Gene calc data: {data}")
            bases = data["seq"]
            s = Seq(bases)
            calc = s.info().replace("\n", "<br><br>")
            #  could also introduce in "context" 'length': s.len() and 'info': s.info()
            context = {
                'calc': calc,
                'gene': gene
            }
            contents = read_html_template("gene_calculations.html").render(context=context)
            code = HTTPStatus.OK
        else:
            contents = handle_error(endpoint, ENSEMBL_COMMUNICATION_ERROR)
            code = HTTPStatus.SERVICE_UNAVAILABLE
        return code, contents


def gene_list(endpoint, parameters):
    user_chromosome = parameters['chromo'][0]
    start = parameters['start'][0]
    end = parameters['end'][0]
    request = RESOURCE_TO_ENSEMBL_REQUEST[endpoint]
    url = (f"{request['resource']}{user_chromosome}:{start}-{end}?{request['params']};feature=gene;feature=transcript;"
           f"feature=cds;feature=exon")
    error, data = server_request(ENSEMBL_SERVER, url)
    if not error:
        print(f"Gene list data: {data}")
        # data is a list of the human genes that are located on the X chromosome from start to finish/end

        genes_list = []
        for i in data:  # every "i"=gene is a dictionary of the list of dicts "data"
            if i['feature_type'] == "gene":
                if i.get("external_name"):
                    genes_list.append(i.get("external_name"))
                """OTHER WAY TO DO IT:
                if 'external_name' in i:
                genes.append(i['external_name'])"""

        if len(genes_list) == 0:
            genes_list.append("There are no genes in this region")

        context = {
            'chromo_number': user_chromosome,
            'genes': genes_list,
            'start': start,
            'end': end
                }
        contents = read_html_template("gene_list.html").render(context=context)
        code = HTTPStatus.OK
    else:
        contents = handle_error(endpoint, ENSEMBL_COMMUNICATION_ERROR)
        code = HTTPStatus.SERVICE_UNAVAILABLE
    return code, contents


"""MAIN PROGRAM"""

socketserver.TCPServer.allow_reuse_address = True


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

        code = HTTPStatus.OK  # establish "200" as default
        content_type = "text/html"
        if endpoint == "/":
            file_path = os.path.join(HTML_FOLDER, "basic_index.html")
            contents = Path(file_path).read_text()
        elif endpoint == "/listSpecies":
            code, contents = list_species(endpoint, parameters)
        elif endpoint == "/karyotype":
            code, contents = karyotype(endpoint, parameters)
        elif endpoint == "/chromosomeLength":
            code, contents = chromosome_length(endpoint, parameters)
        elif endpoint == "/geneSeq":
            code, contents = human_gene(endpoint, parameters)
        elif endpoint == "/geneInfo":
            code, contents = gene_info(endpoint, parameters)
        elif endpoint == "/geneCalc":
            code, contents = gene_calc(endpoint, parameters)
        elif endpoint == "/geneList":
            code, contents = gene_list(endpoint, parameters)
        else:
            contents = handle_error(endpoint, RESOURCE_NOT_AVAILABLE_ERROR)
            code = HTTPStatus.NOT_FOUND  # change code to "404"

        self.send_response(code)
        contents_bytes = contents.encode()  # transform to bytes to send the contents through the network
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(contents_bytes)))
        self.end_headers()  # finish sending HTTP headers to the client, after the server will start sending the body

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
