from src.afd.afd import AFD
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
s1
#alphabet
a
b
c
#transitions
s0:a>s2
s0:b>s1
s0:c>s3
s1:a>s0
s1:b>s3
s1:c>s1
s2:a>s2
s2:b>s0
s2:c>s1
s3:a>s0
s3:b>s3
s3:c>s0
"""


def test_AFD_isAFD():
    obj = AFD()
    obj.prepare(automato)
    assert obj.isAFD()


def test_AFD_isAFD_invalid():
    obj = AFD()
    obj.prepare(automato+"\ns3:a>s3")
    assert not obj.isAFD()


def test_AFD_prepare_states():
    obj = AFD()
    obj.prepare(automato)
    assert sorted(obj.states) == sorted(['s0', 's1', 's2', 's3'])


def test_AFD_prepare_parsed_states_exists_s3():
    obj = AFD()
    obj.prepare(automato)
    assert any(x for x in obj.parsed_states if x.name == 's3')


def test_AFD_prepare_parsed_states_has_transaction():
    obj = AFD()
    obj.prepare(automato)
    assert any(x for x in obj.parsed_states if x.name == 's2' and any(
        (y, z) for (y, z) in x.transitions.items() if y == 'c' and 's1' in z))


def test_AFD_prepare_parsed_states_has_no_transaction():
    obj = AFD()
    obj.prepare(automato)
    assert not any(x for x in obj.parsed_states if x.name == 's2' and any(
        (y, z) for (y, z) in x.transitions.items() if 's3' in z))


def test_AFD_run_valid():
    obj = AFD()
    obj.prepare(automato)
    assert obj.run('baaaccbcacc')


def test_AFD_run_invalid():
    obj = AFD()
    obj.prepare(automato)
    assert not obj.run('cbaaaabccbcaaacaabbcabbcaa')
