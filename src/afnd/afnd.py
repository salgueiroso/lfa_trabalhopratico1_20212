from functools import reduce
from os import stat
from typing import List
from src.afd.state import State
from src.common.afd_base import AFDBase
from src.afd.afd import AFD


class AFND(AFD):

    _subset_map: dict[str, dict[str, str]]

    _state_names: List[str]

    _group_labels: dict[str, str]

    _is_afnd: bool = False

    def __init__(self) -> None:
        self._subset_map = {}
        self._group_labels = {}
        self._state_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                             'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self._state_names.reverse()

    def _pop_next_name(self):
        _name = self._state_names.pop()
        return _name

    def _create_subset_key(self, key) -> dict[str, str]:
        if not self._subset_map.get(key, None):
            self._subset_map[key] = {}
            for symbol in self.alphabet:
                self._subset_map[key][symbol] = None
        return self._subset_map[key]

    def _create_subset(self):

        self._is_afnd = any(any(len(y) > 1 for y in x.transitions.values())
                            for x in self.parsed_states)

        if not self._is_afnd:
            raise Exception('Automato não é Não Deterministico!')

        _initial_state = next(
            (x for x in self.parsed_states if x.isInitilState), None)

        self._create_subset_items([_initial_state])

        self._subset_table_to_AFD()

        self._show_deterministic_automaton()

    def _rename_all_states(self):
        for state in self.parsed_states:
            _new_name = self._pop_next_name()
            for state_child in self.parsed_states:
                for transition_key, transition_value in state_child.transitions.items():

                    for i in range(len(transition_value)):
                        if transition_value[i] == state.name:
                            transition_value[i] = _new_name
            state.name = _new_name

    def _group_to_label(self, group: List[str]) -> str:
        group = list(set(group))
        group.sort()
        _name = ','.join(group)
        label = self._group_labels[_name] = self._group_labels.get(
            _name, None) or self._pop_next_name()
        return label

    def _label_to_group(self, label: str) -> List[str]:
        group, label = next(((k, v)
                             for k, v in self._group_labels.items() if v == label), None)
        return group.split(',')

    def _create_subset_items(self, _next_states: List[State]):

        _key = self._group_to_label([x.name for x in _next_states])
        _subset = self._create_subset_key(_key)
        for k in _subset:
            _target: str = None

            z = []
            for x in [x.transitions[k] for x in _next_states if x.transitions.get(k, None)]:
                z.extend(x)

            if not z:
                continue

            _target = self._group_to_label(z)

            if not _target:
                continue
            _subset[k] = _target

        for k, v in _subset.items():
            if v:
                if v not in self._subset_map:
                    self._create_subset_key(v)
                    _group = self._label_to_group(v)
                    _nexts = [x for x in self.parsed_states if any(
                        y for y in _group if y == x.name)]
                    if _nexts:
                        self._create_subset_items(_nexts)

    def isInitialState(self, state_name: str) -> bool:
        if AFDBase.isInitialState(self, state_name):
            return True
        elif state_name in self._group_labels.values():
            return self.initial in self._label_to_group(state_name)
        else:
            return False

    def isFinalState(self, state_name: str) -> bool:
        if AFDBase.isFinalState(self, state_name):
            return True
        elif state_name in self._group_labels.values():
            return any(item in self.accepting for item in self._label_to_group(state_name))
        else:
            return False

    def _subset_table_to_AFD(self):

        self.parsed_states = []

        for k0, v0 in self._subset_map.items():
            state = State(name=k0, isInitilState=self.isInitialState(
                k0), isFinalState=self.isFinalState(k0))
            self.parsed_states.append(state)
            for k1, v1 in v0.items():
                self._add_state(state_from=k0, alphabet_symbol=k1, state_to=v1)

        self.parsed_states.sort(key=lambda x: x.name)

    def _show_deterministic_automaton(self):
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||| AUTOMATO FINITO DETERMINISTICO TRANSFORMADO |||")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("#states")
        print("\n".join(list(map(lambda x: x.name, self.parsed_states))))
        print("#initial")
        print(next((x for x in self.parsed_states if x.isInitilState), None).name)
        print("#accepting")
        print("\n".join(list(map(lambda a: a.name, filter(
            lambda x: x.isFinalState, self.parsed_states)))))
        print("#alphabet")
        print("\n".join(self.alphabet))
        print("#transitions")
        for state in self.parsed_states:
            for k, v in state.transitions.items():
                if v:
                    print("{s}:{a}>{t}".format(
                        s=state.name, a=k, t=next((x for x in v), None)))
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||")

    def prepare(self, fsm_data: str):
        AFD.prepare(self, fsm_data=fsm_data)
        self._create_subset()

    def isAFND(self):
        return self._is_afnd

    def run(self, input: str) -> bool:

        if not self.isAFND():
            raise Exception('Automato não é Não Deterministico!')

        if any(symbol for symbol in input if symbol not in self.alphabet):
            raise Exception('Entrada possui simbolos não pertencentes ao alfabeto {alphabet_symbols}'.format(
                alphabet_symbols=self.alphabet))

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
                if states:
                    next_state = next((x for x in states), None)
                    actual_state = next(
                        (x for x in self.parsed_states if x.name == next_state), None)
                    found = bool(actual_state)

            if not found:
                return False

        return actual_state.isFinalState
