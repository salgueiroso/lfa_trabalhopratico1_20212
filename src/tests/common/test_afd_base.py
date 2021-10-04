from src.common.afd_base import AFDBase

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


def test_AFDBase_load():
    assert AFDBase().load(automato) == True


def test_AFDBase_load_states():
    obj = AFDBase()
    obj.load(automato)
    assert sorted(obj.states) == sorted(['q0', 'q1', 'qf'])


def test_AFDBase_load_initial():
    obj = AFDBase()
    obj.load(automato)
    assert obj.initial == 'q0'


def test_AFDBase_load_accepting():
    obj = AFDBase()
    obj.load(automato)
    assert obj.accepting == ['qf']


def test_AFDBase_load_alphabet():
    obj = AFDBase()
    obj.load(automato)
    assert obj.alphabet == ['0', '1']


def test_AFDBase_load_transitions():
    obj = AFDBase()
    obj.load(automato)
    assert obj.transitions == ['q0:0>q0,q1', 'q1:1>qf']


def test_AFDBase_isFinalState():
    obj = AFDBase()
    obj.load(automato)
    assert obj.isFinalState('qf')


def test_AFDBase_isFinalState_inverse():
    obj = AFDBase()
    obj.load(automato)
    assert not obj.isFinalState('q1')


def test_AFDBase_InitialState():
    obj = AFDBase()
    obj.load(automato)
    assert obj.isInitialState('q0')


def test_AFDBase_InitialState_inverse():
    obj = AFDBase()
    obj.load(automato)
    assert not obj.isInitialState('q1')


def test_AFDBase_isAcceptableAlphabet():
    obj = AFDBase()
    obj.load(automato)
    assert obj.isAcceptableAlphabet('1')


def test_AFDBase_isAcceptableAlphabet_inverse():
    obj = AFDBase()
    obj.load(automato)
    assert not obj.isAcceptableAlphabet('z')
