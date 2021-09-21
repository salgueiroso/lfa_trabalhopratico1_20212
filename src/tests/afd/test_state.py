
from src.afd.state import State


def test_State():
    state = State(name='s1')
    assert state.name == 's1'


def test_State_isFinalState():
    state = State(name='s1', isFinalState=True)
    assert state.isFinalState


def test_State_isInitilState():
    state = State(name='s1', isInitilState=True)
    assert state.isInitilState


def test_State_transitions():
    state = State(name='s1')
    assert state.transitions == {}
