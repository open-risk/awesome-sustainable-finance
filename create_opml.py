"""
Filename: create_opml.py
Author: Open Risk
Date: 11 09 2025
Version: 0.1
Description: This script converts an awesome list into an OPML format
License: GPL
Contact: info@openriskmanagement.com
"""

import markdown
import mistune
from markdown.extensions.tables import TableExtension
from mistune import Markdown
import xml.etree.ElementTree as ET
from parser import SectionParser

def extract_list_items(markdown_text):
    lines = markdown_text.split('\n')
    list_items = []
    for line in lines:
        if line.strip().startswith('-'):
            list_items.append(line.strip()[2:].strip())
    return list_items

def parse_markdown_sections(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()
    parser = SectionParser()
    parser.parse(markdown_text)
    return parser.get_sections()

if __name__ == "__main__":

    input_file = 'README.md'
    sections = parse_markdown_sections(input_file)

    opml_title = "Awesome List as RSS List"
    description = "For use in any standard RSS reader"

    opml = ET.Element("opml", version="2.0")
    head = ET.SubElement(opml, "head")
    ET.SubElement(head, "title").text = opml_title
    ET.SubElement(head, "description").text = description
    body = ET.SubElement(opml, "body")

    for section, content in sections.items():
        if section.startswith('# '):
            pass
        else:
            markdown_text = "\n".join(content)
            outline = ET.SubElement(body, "outline", text=section, description=section)
            list_items = extract_list_items(markdown_text)
            for index, item in enumerate(list_items, start=1):
                item = ET.SubElement(outline, "outline", text="", description=item)

    tree = ET.ElementTree(opml)
    with open("asf_feeds.opml", "wb") as file:
        tree.write(file, encoding="utf-8", xml_declaration=True)


print("OPML file created successfully.")