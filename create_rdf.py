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

if __name__ == "__main__":

    doap = get_ontology("file://doap.rdf").load()
    print(list(doap.classes()))