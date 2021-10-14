from src.afnd.afnd import AFND
from src.afd.afd import AFD


class AFNDE(AFND):

    _is_afnd: bool = False

    def prepare(self, fsm_data: str):
        AFD.prepare(self, fsm_data=fsm_data)
        self.alphabet.extend('$')
        self.alphabet = list(set(self.alphabet))
        self._create_subset()
        self._is_afnd = any([x for x in self.parsed_states if '$' in x.transitions.keys(
        ) and len(x.transitions['$']) > 0])

    def isAcceptableAlphabet(self, alphabet_simbol: chr) -> bool:
        return AFND.isAcceptableAlphabet(self, alphabet_simbol) or alphabet_simbol == '$'

    def isAFNDE(self):
        return self._is_afnd

    def run(self, input: str) -> bool:

        if not self.isAFNDE():
            raise Exception(
                'Automato não é Não Deterministico com Transição Vazia!')

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

            symbol, targets = next(
                ((sy, st) for sy, st in actual_state.transitions.items() if sy == input[i]), (None, None))

            if symbol:
                if targets:
                    next_state = next((x for x in targets), None)
                    actual_state = next(
                        (x for x in self.parsed_states if x.name == next_state), None)
                    found = bool(actual_state)

            if not found:
                return False

        return actual_state.isFinalState
