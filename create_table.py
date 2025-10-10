"""
Filename: create_tabular.py
Author: Open Risk
Date: 11 09 2025
Version: 0.1
Description: This script converts an awesome list into tabular and OPML formats
License: GPL
Contact: info@openriskmanagement.com
"""

import markdown
import mistune
from markdown.extensions.tables import TableExtension
from mistune import Markdown
import xml.etree.ElementTree as ET

def extract_list_items(markdown_text):
    lines = markdown_text.split('\n')
    list_items = []
    for line in lines:
        if line.strip().startswith('-'):
            list_items.append(line.strip()[2:].strip())
    return list_items

def create_table_from_list(list_items):
    table_lines = ["| Index | Item   |", "|------|--------|"]
    for index, item in enumerate(list_items, start=1):
        table_lines.append(f"| {index} | {item} |")
    return "\n".join(table_lines)

def convert_markdown_list_to_table(markdown_text):
    list_items = extract_list_items(markdown_text)
    table = create_table_from_list(list_items)
    return table

class SectionParser:
    def __init__(self):
        self.sections = {}
        self.current_section = None
        self.current_content = []

    def parse(self, markdown_text):
        lines = markdown_text.split('\n')
        for line in lines:
            if line.startswith('#'):
                self._handle_header(line)
            else:
                self._handle_content(line)
        self._finalize_section()

    def _handle_header(self, line):
        if self.current_section:
            self._finalize_section()
        self.current_section = line.strip()
        self.current_content = []
        self.sections[self.current_section] = []

    def _handle_content(self, line):
        if self.current_section:
            self.current_content.append(line)

    def _finalize_section(self):
        if self.current_section and self.current_content:
            self.sections[self.current_section].extend(self.current_content)
            self.current_content = []

    def get_sections(self):
        return self.sections

def parse_markdown_sections(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()
    parser = SectionParser()
    parser.parse(markdown_text)
    return parser.get_sections()

if __name__ == "__main__":

    input_file = 'README.md'
    output_file = 'TABULAR.md'
    output_text = ''
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
            output_text += section + '\n\n'
            markdown_text = "\n".join(content)
            table_text = convert_markdown_list_to_table(markdown_text)
            output_text += table_text  + '\n\n'
            outline = ET.SubElement(body, "outline", text=section, description=section)
            list_items = extract_list_items(markdown_text)
            for index, item in enumerate(list_items, start=1):
                item = ET.SubElement(outline, "outline", text="", description=item)


    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(output_text)
        file.close()

    tree = ET.ElementTree(opml)
    with open("awesome_sustainable_finance_feeds.opml", "wb") as file:
        tree.write(file, encoding="utf-8", xml_declaration=True)