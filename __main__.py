from sys import path
from typing import IO
from src.afnd.afnd import AFND
from src.afnde.afnde import AFNDE
from src.afd.afd import AFD
import argparse


def setupArgParse():
    parser = argparse.ArgumentParser(
        description='Interpretador de autômatos finitos')
    parser.add_argument('--type', action='store', dest='type', choices={"DFA", "NFA", "eNFA"},
                        required=True, help='Tipo de automato a ser analisado. Valores permisidos são: DFA, NFA e eNFA')
    parser.add_argument('--fsmfile', action='store', dest='fsmfile',
                        required=True, help='Arquivo o a definição do automato')
    parser.add_argument('--input', action='store', dest='input',
                        required=True, help='Simbolos de entrada')

    return parser.parse_args()


if __name__ == "__main__":

    arguments = setupArgParse()

    type = str(arguments.type).upper()
    automato = open(arguments.fsmfile, 'r').read()
    input_simbols = arguments.input

    obj = None

    if type == 'DFA':
        obj = AFD()
    elif type == 'NFA':
        obj = AFND()
    elif type == 'ENFA':
        obj = AFNDE()

    obj.prepare(automato)

    valido = obj.run(input_simbols)

    if valido:
        print("Simbolos de entrada '{symbols}' são válidos para o automato".format(
            symbols=input_simbols))
    else:
        print("Simbolos de entrada '{symbols}' inválidos!".format(
            symbols=input_simbols))
