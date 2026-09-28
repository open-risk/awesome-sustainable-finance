"""
Filename: create_rdf.py
Author: Open Risk
Date: 03 11 2025
Version: 0.1
Description: This script creates and DOAP RDF file per project in the Awesome List
License: GPL
Contact: info@openriskmanagement.com
"""

from owlready2 import *
import rdflib

if __name__ == "__main__":

    doap = get_ontology("file://doap.owl").load()
    print(list(doap.classes()))
    print(doap.imported_ontologies)
    print(list(doap.properties()))

    for cls in doap.classes():
        print(cls.name, cls.namespace)

    # graph = rdflib.Graph()
    # graph.parse('doap.owl')
    #
    # query = """
    # SELECT ?class
    # WHERE {
    #     ?class rdf:type rdfs:Class .
    # }
    # """
    # for row in graph.query(query):
    #     print(row[0])