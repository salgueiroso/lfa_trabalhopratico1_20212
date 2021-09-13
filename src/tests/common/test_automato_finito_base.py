from src.common.automato_finito_base import AutomatoFinitoBase

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


def test_AutomatoFinitoBase_load():
    assert AutomatoFinitoBase().load(automato) == True


def test_AutomatoFinitoBase_load_states():
    obj = AutomatoFinitoBase()
    obj.load(automato)
    assert sorted(obj.states) == sorted(['q0', 'q1', 'qf'])


def test_AutomatoFinitoBase_load_initial():
    obj = AutomatoFinitoBase()
    obj.load(automato)
    assert obj.initial == ['q0']
