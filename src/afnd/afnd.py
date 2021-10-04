from functools import reduce
from typing import List
from src.afd.state import State
from src.common.afd_base import AFDBase
from src.afd.afd import AFD


class AFND(AFD):

    _subset_map: dict[str, dict[str, str]]

    def __init__(self) -> None:
        self._subset_map = {}

    def _create_subset_key(self, key) -> dict[str, str]:
        if not self._subset_map.get(key, None):
            self._subset_map[key] = {}
            for symbol in self.alphabet:
                self._subset_map[key][symbol] = None
        return self._subset_map[key]

    def _create_subset(self):

        self._create_subset_key('$')

        _initial_state = next(
            (x for x in self.parsed_states if x.isInitilState), None)

        self._create_subset_items([_initial_state])

        self._subset_table_to_AFD()

    def _create_subset_items(self, _next_states: List[State]):

        #_next_states.sort(key=lambda x: x.name)

        _key = reduce(lambda a, b: a+','+b, [x.name for x in _next_states])
        _subset = self._create_subset_key(_key)
        for k in _subset:
            _transitions: List[str] = []

            for x in [x.transitions[k] for x in _next_states if x.transitions.get(k, None)]:
                _transitions.extend(set(x))

            if not _transitions:
                continue
            _transitions = list(set([x for x in _transitions]))
            _transitions.sort()
            _new_key = reduce(lambda a, b: a+','+b, _transitions)
            _subset[k] = _new_key

        for v in _subset.values():
            if v and v not in self._subset_map:
                _splited = v.split(',')
                _nexts = [x for x in self.parsed_states if any(
                    y for y in _splited if y == x.name)]
                self._create_subset_items(_nexts)

    def _subset_table_to_AFD(self):

        self.parsed_states = []

        for k0, v0 in self._subset_map.items():
            state = State(name=k0, isInitilState=self.isInitialState(
                k0), isFinalState=self.isFinalState(k0))
            self.parsed_states.append(state)
            for k1, v1 in v0.items():
                self._add_state(state_from=k0, alphabet_symbol=k1, state_to=v1)

    def isAFND(self):
        return any(any(len(y) > 1 for y in x.transitions.values()) for x in self.parsed_states)

    def run(self, input: str) -> bool:

        if not self.isAFND():
            raise Exception('Automato não é Não Deterministico!')

        if any(symbol for symbol in input if symbol not in self.alphabet):
            raise Exception('Entrada possui simbolos não pertencentes ao alfabeto {alphabet_symbols}'.format(
                alphabet_symbols=self.alphabet))

        self._create_subset()
        self._loadStates()
        self._extractTransitionsStates()

        initial_state = next(
            (x for x in self.parsed_states if x.isInitilState), None)

        if not initial_state:
            raise Exception('Não foi definido um estado inicial')

        actual_state = initial_state

        for i in range(len(input)):

            found = False

            symbol, states = next(
                ((sy, st) for sy, st in actual_state.transitions.items() if sy == input[i]), (None, None))

            if symbol:
                next_state = next((x for x in states), None)
                actual_state = next(
                    (x for x in self.parsed_states if x.name == next_state), None)
                found = bool(actual_state)

            if not found:
                return False

        return actual_state.isFinalState
