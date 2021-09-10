from src.common.automato_finito_base import AutomatoFinitoBase


def test_AutomatoFinitoBase_load():
    assert AutomatoFinitoBase().load("asd") == True
