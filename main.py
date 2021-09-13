from src.common.automato_finito_base import AutomatoFinitoBase


if __name__ == "__main__":
    automato = """
#states
q0  
q1

qf
#initial
q0
#accepting
qf
#alphabet
0
1
#transitions
q0:0>q0,q1
q1:1>qf
"""
    # AutomatoFinitoBase().load(automato)
    obj = AutomatoFinitoBase()
    obj.load(automato)
    assert sorted(obj.states) == sorted(['q0', 'q1', 'qf'])
