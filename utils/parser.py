from urllib.parse import urlparse


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
            parsed_url = urlparse(link)
            domain_name = parsed_url.netloc
            path = parsed_url.path.split('/')
            if len(path) > 2:
                owner = path[1]
                repo = path[2]
            else:
                owner = None
                repo = None
            item['title'] = title
            item['host'] = domain_name
            # TODO This is the github API
            item['owner'] = owner
            item['repo'] = repo
            item['url'] = link
            item['description'] = desc
            list_items.append(item)
        else:
            pass
    return list_items


def create_table_from_list(list_items):
    table_lines = ["| Name | Description | Repository | Link |", "|------|------|------|------|"]
    for item in list_items:
        table_lines.append(f"| {item['title']} | {item['description']} |   | {item['url']} |  ")
    return "\n".join(table_lines)


def create_dict_from_list(list_items):
    dict = {}
    for item in list_items:
        dict[item['title']] = \
            {'description': item['description'],
             'url': item['url'],
             'repo': item['repo'],
             'host': item['host'],
             'owner': item['owner']}
    return dict


def convert_markdown_list_to_table(markdown_text):
    list_items = extract_list_items(markdown_text)
    table = create_table_from_list(list_items)
    return table


def convert_markdown_list_to_dict(markdown_text):
    list_items = extract_list_items(markdown_text)
    dict = create_dict_from_list(list_items)
    return dict


def parse_markdown_sections(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()
    parser = SectionParser()
    parser.parse(markdown_text)
    return parser.get_sections()


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

    # Return the sections dictionary
    def get_sections(self):
        return self.sections
