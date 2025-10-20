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
