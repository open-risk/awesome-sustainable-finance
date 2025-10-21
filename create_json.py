"""
Filename: create_json.py
Author: Open Risk
Start Date: 21 10 2025
Version: 0.1
Description: This script converts an awesome list into a JSON Dict
License: GPL
Contact: info@openriskmanagement.com
"""

import json
import markdown
import mistune
from markdown.extensions.tables import TableExtension
from mistune import Markdown
import xml.etree.ElementTree as ET
from parser import SectionParser, parse_markdown_sections, convert_markdown_list_to_dict

if __name__ == "__main__":

    input_file = 'README.md'
    output_file = 'asf.json'
    sections = parse_markdown_sections(input_file)

    # Iterate over sections and add to dict
    # Unless its a root level section, which we pass
    # NB: all sections are treated the same, irrespective of nesting level

    asf_dict = {}
    for section, content in sections.items():
        if section.startswith('# '):
            pass
        else:
            markdown_text = "\n".join(content)
            asf_dict[section] = convert_markdown_list_to_dict(markdown_text)

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(asf_dict, file, indent=4)

print("JSON file created successfully.")