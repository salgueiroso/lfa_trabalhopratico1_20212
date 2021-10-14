from typing import List


class State:
    name: str
    isFinalState: bool
    isInitilState: bool
    transitions: dict[str, List[str]]

    def __init__(self, name: str, isFinalState: bool = False, isInitilState: bool = False) -> None:
        self.name = name
        self.isFinalState = isFinalState
        self.isInitilState = isInitilState
        self.transitions = {}

    def insertTransition(self, alphabet_symbol: str, targetState: str):
        self.transitions[alphabet_symbol] = self.transitions.get(
            alphabet_symbol, [])
        if targetState:
            for item in targetState.split(','):
                if not any(x for x in self.transitions[alphabet_symbol] if x == item):
                    self.transitions[alphabet_symbol].append(item)
        self.transitions[alphabet_symbol].sort()
