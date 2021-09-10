import re


class AutomatoFinitoBase:

    def load(self, input: str) -> bool:

        self.states = re.fullmatch(
            r"(?:#states)(?P<states>[\n\w]+)^#", input, re.MULTILINE)

        return True
