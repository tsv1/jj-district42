from baby_steps import given, then, when
from d42 import validate
from d42.validation.errors import MissingElementValidationError, TypeValidationError
from th import PathHolder

from jj_d42.types.param_list import ParamListSchema


def test_header_list_empty_list_validation():
    with given:
        value = []

    with when:
        result = validate(ParamListSchema(), value)

    with then:
        assert result.get_errors() == []


def test_header_list_list_validation():
    with given:
        value = [["key", "val"]]

    with when:
        result = validate(ParamListSchema(), value)

    with then:
        assert result.get_errors() == []


def test_header_list_empty_dict_validation():
    with given:
        value = {}

    with when:
        result = validate(ParamListSchema(), value)

    with then:
        assert result.get_errors() == []


def test_header_list_dict_validation():
    with given:
        value = {"key": "val"}

    with when:
        result = validate(ParamListSchema(), value)

    with then:
        assert result.get_errors() == []


def test_header_list_type_validation_error():
    with given:
        value = set()

    with when:
        result = validate(ParamListSchema(), value)

    with then:
        assert result.get_errors() == [TypeValidationError(PathHolder(), value, list)]


def test_header_list_value_validation_error():
    with given:
        value = [set()]

    with when:
        result = validate(ParamListSchema(), value)

    with then:
        assert result.get_errors() == [TypeValidationError(PathHolder()[0], value[0], list)]


def test_header_list_value_empty_validation_error():
    with given:
        value = [[]]

    with when:
        result = validate(ParamListSchema(), value)

    with then:
        assert result.get_errors() == [MissingElementValidationError(PathHolder()[0], value[0], 0)]


def test_header_list_value_partial_validation_error():
    with given:
        value = [["key"]]

    with when:
        result = validate(ParamListSchema(), value)

    with then:
        assert result.get_errors() == [MissingElementValidationError(PathHolder()[0], value[0], 1)]


def test_header_list_value_key_validation_error():
    with given:
        value = [[None, "val"]]

    with when:
        result = validate(ParamListSchema(), value)

    with then:
        assert result.get_errors() == [TypeValidationError(PathHolder()[0][0], value[0][0], str)]


def test_header_list_value_val_validation_error():
    with given:
        value = [["key", None]]

    with when:
        result = validate(ParamListSchema(), value)

    with then:
        assert result.get_errors() == [TypeValidationError(PathHolder()[0][1], value[0][1], str)]
