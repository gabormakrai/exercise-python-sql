import pytest

from test_helper import MockXmlData
from utils import get_element_or_none


def test_get_element_or_none_with_string_method():
    elem = MockXmlData({'key': 'value'})
    value = get_element_or_none(elem, 'key', str)
    assert value == 'value'


def test_get_element_or_none_with_int_method():
    elem = MockXmlData({'key': '1'})
    value = get_element_or_none(elem, 'key', int)
    assert value == 1


def test_get_element_or_none_with_strin_value_int_method():
    with pytest.raises(ValueError):
        elem = MockXmlData({'key': 'not_a_number'})
        get_element_or_none(elem, 'key', int)
