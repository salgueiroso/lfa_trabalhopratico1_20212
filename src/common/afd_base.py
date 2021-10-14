
import re
from typing import List


class AFDBase:

    states: List[str]
    initial: str
    accepting: List[str]
    alphabet: List[chr]
    transitions: List[str]

    def load(self, fsm_data: str) -> bool:

        self.states = self._load(fsm_data, 'states') or []
        self.initial = next(
            (x for x in (self._load(fsm_data, 'initial') or []) if x), '')
        self.accepting = self._load(fsm_data, 'accepting') or []
        self.alphabet = (self._load(fsm_data, 'alphabet') or [])
        self.transitions = self._load(fsm_data, 'transitions') or []

        return bool(self.states) and bool(self.initial) and bool(self.accepting) and bool(self.alphabet) and bool(self.transitions)

    def isFinalState(self, state_name: str) -> bool:
        return any(x for x in self.accepting if x == state_name)

    def isInitialState(self, state_name: str) -> bool:
        return state_name == self.initial

    def isAcceptableAlphabet(self, alphabet_simbol: chr) -> bool:
        return alphabet_simbol in self.alphabet

    def _load(self, fsm_data: str, section: str) -> List[str]:
        section_str = re.search(
            r"(?:#"+section+")(?P<"+section+">[\r\n\\w :>,$]+)", fsm_data, re.MULTILINE+re.IGNORECASE)

        if section_str:
            str = section_str.group(section)

            _list = self._limpar_criar_lista(str)

            return _list if len(_list) > 0 else None

        return None

    def _limpar_criar_lista(self, str: str) -> List[str]:

        # conversao str para list
        _list = list(
            map(lambda x: x.strip(), str.strip().splitlines()))

        # remocao de linhas vazias
        _list = list(filter(lambda x: x, _list))

        _list.sort()

        return _list
