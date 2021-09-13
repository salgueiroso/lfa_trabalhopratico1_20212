import re
from typing import Any, List


class AutomatoFinitoBase:

    def load(self, input: str) -> bool:

        self.states = self._load_states(input) or []
        self.initial = self._load_initial(input) or []

        return len(self.states) > 0 and len(self.initial) > 0

    def _load_states(self, input: str) -> List[str]:

        states_section_str = re.search(
            r"(?:#states)(?P<states>[\r\n\w ]+)^[ ]*#", input, re.MULTILINE)

        if states_section_str:
            states_str = states_section_str.group('states')

            states_list = list(
                map(lambda x: x.strip(), states_str.strip().splitlines()))

            states_list = list(filter(lambda x: x, states_list))

            return states_list if len(states_list) > 0 else None

        return None

    def _load_initial(self, input: str) -> List[str]:

        initial_section_str = re.search(
            r"(?:#initial)(?P<initial>[\r\n\w ]+)^[ ]*#", input, re.MULTILINE)

        if initial_section_str:
            initial_str = initial_section_str.group('initial')

            initial_list = list(
                map(lambda x: x.strip(), initial_str.strip().splitlines()))

            initial_list = list(filter(lambda x: x, initial_list))

            return initial_list if len(initial_list) > 0 else None

        return None
