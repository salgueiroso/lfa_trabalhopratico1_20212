from src.afnd.afnd import AFND
import pytest

automato = """
#states
s0
s1
s2
s3
#initial
s0
#accepting
s2
s3
#alphabet
a
b
c
#transitions
s0:c>s0,s1
s1:a>s0,s2
s1:b>s0,s1
s1:c>s0,s3
s2:a>s1,s2
s2:b>s0,s1
s2:c>s1,s3
s3:a>s0
s3:b>s0,s3
"""


def test_AFND_isAFND():
    obj = AFND()
    obj.prepare(automato)
    assert obj.isAFND()


def test_AFND_prepare_states():
    obj = AFND()
    obj.prepare(automato)
    assert sorted(obj.states) == sorted(['s0', 's1', 's2', 's3'])


def test_AFND_prepare_parsed_states_exists_s0s1s3():
    obj = AFND()
    obj.prepare(automato)
    assert any(x for x in obj.parsed_states if x.name == 'F')


def test_AFND_prepare_parsed_states_has_transition():
    obj = AFND()
    obj.prepare(automato)
    assert any(x for x in obj.parsed_states if x.name == 'F' and any(
        (y, z) for (y, z) in x.transitions.items() if y == 'c' and 'D' in z))


def test_AFND_prepare_parsed_states_has_no_transition():
    obj = AFND()
    obj.prepare(automato)
    assert not any(x for x in obj.parsed_states if x.name == 'F' and any(
        (y, z) for (y, z) in x.transitions.items() if y == 'c' and 'A' in z))


def test_AFND_run_valid():
    obj = AFND()
    obj.prepare(automato)
    assert obj.run('ccbcbcaabcaac')


def test_AFND_run_invalid():
    obj = AFND()
    obj.prepare(automato)
    assert not obj.run('cbbbacaaab')
