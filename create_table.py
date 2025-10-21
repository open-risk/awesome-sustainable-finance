"""
Filename: create_table.py
Author: Open Risk
Start Date: 11 09 2025
Version: 0.2
Description: This script converts an awesome list into a tabular formats
License: GPL
Contact: info@openriskmanagement.com
"""

import markdown
import mistune
from markdown.extensions.tables import TableExtension
from mistune import Markdown
import xml.etree.ElementTree as ET
from parser import SectionParser

# Extract information from each line of markdown text
def extract_list_items(markdown_text):
    lines = markdown_text.split('\n')
    list_items = []
    for line in lines:
        item = {}
        if line.strip().startswith('-'):
            raw = line.strip()[2:].strip()
            desc = raw.split('-')[-1].strip()
            bs = raw.index("[") + 1
            be = raw.index("]")
            ps = raw.index("(") + 1
            pe = raw.index(")")
            title = raw[bs:be]
            link = raw[ps:pe]
            item['title'] = title
            item['url'] = link
            item['description'] = desc
            list_items.append(item)
        else:
            pass
    return list_items

def create_table_from_list(list_items):
    table_lines = ["| Name | Description | Repository | Link |", "|------|------|------|------|"]
    for item in list_items:
        print(item)
        table_lines.append(f"| {item['title']} | {item['description']} |   | {item['url']} |  ")
    return "\n".join(table_lines)

def convert_markdown_list_to_table(markdown_text):
    list_items = extract_list_items(markdown_text)
    table = create_table_from_list(list_items)
    return table

def parse_markdown_sections(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()
    parser = SectionParser()
    parser.parse(markdown_text)
    return parser.get_sections()

if __name__ == "__main__":

    input_file = 'README.md'
    output_file = 'TABULAR.md'
    sections = parse_markdown_sections(input_file)

    # Iterate over sections and create one markdown table for each
    # Unless its a root level section, which we pass
    # NB: all other sections are treated the same, irrespective of nesting

    output_text = ''
    for section, content in sections.items():
        if section.startswith('# '):
            pass
        else:
            output_text += section + '\n\n'
            markdown_text = "\n".join(content)
            table_text = convert_markdown_list_to_table(markdown_text)
            output_text += table_text  + '\n\n'

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(output_text)
        file.close()

print("Tabular file created successfully.")