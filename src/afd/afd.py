from typing import List
from src.common.afd_base import AFDBase
from src.afd.state import State
import re


class AFD(AFDBase):

    parsed_states: List[State]

    def _extractTransitionsStates(self):
        pattern = r"(?P<from>\w+):(?P<symbol>[$\w+-])>(?P<to>[\w,]+)"
        for t in self.transitions:
            results = re.search(pattern, t, re.IGNORECASE)
            if not results:
                raise Exception(
                    '"{transition}" não segue o padrão "q0:a>q1"'.format(transition=t))
            self._add_state(results['from'], results['symbol'], results['to'])

    def _add_state(self, state_from: str, alphabet_symbol: str, state_to: str):

        if not self.isAcceptableAlphabet(alphabet_symbol):
            raise Exception('"{alphabet_symbol}" não é um simbolo do alfabeto'.format(
                alphabet_symbol=alphabet_symbol))

        state = next(
            (x for x in self.parsed_states if x.name == state_from), None)

        if not state:
            raise Exception(
                'Estado "{state}" não foi previamente declarado'.format(state=state_from))

        state.insertTransition(alphabet_symbol, state_to)

    def _loadStates(self):
        self.parsed_states = []
        for state_name in sorted(self.states):
            is_final_state = self.isFinalState(state_name)
            is_initial_state = self.isInitialState(state_name)
            state = State(name=state_name, isFinalState=is_final_state,
                          isInitilState=is_initial_state)
            self.parsed_states.append(state)

    def isAFD(self):
        return all(all(len(y) == 1 for y in x.transitions.values()) for x in self.parsed_states)

    def prepare(self, fsm_data: str):
        if self.load(fsm_data=fsm_data):
            self._loadStates()
            self._extractTransitionsStates()
        else:
            raise Exception('Automato invalido!')

    def run(self, input: str) -> bool:

        if not self.isAFD():
            raise Exception('Automato não é Deterministico!')

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
                next_state = next((x for x in states), None)
                actual_state = next(
                    (x for x in self.parsed_states if x.name == next_state), None)
                found = bool(actual_state)

            if not found:
                return False

        return actual_state.isFinalState
