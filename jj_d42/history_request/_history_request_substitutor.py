from typing import Any, cast

from d42.substitution import Substitutor, SubstitutorValidator
from d42.validation import ValidationResult
from jj.mock import HistoryRequest
from niltype import Nil, Nilable
from th import PathHolder

from ._history_request_schema import HistoryRequestSchema

__all__ = ("HistoryRequestSubstitutor", "HistoryRequestSubstitutorValidator",)


class HistoryRequestSubstitutor(Substitutor, extend=True):
    def visit_jj_history_request(self, schema: HistoryRequestSchema, *,
                                 value: Any = Nil, **kwargs: Any) -> HistoryRequestSchema:
        if isinstance(value, HistoryRequest):
            value = value.to_dict()
        return cast(HistoryRequestSchema, self.visit_type_alias(schema, value=value, **kwargs))


class HistoryRequestSubstitutorValidator(SubstitutorValidator, extend=True):
    def visit_jj_history_request(self, schema: HistoryRequestSchema, *,
                                 value: Any = Nil, path: Nilable[PathHolder] = Nil,
                                 **kwargs: Any) -> ValidationResult:
        if isinstance(value, HistoryRequest):
            value = value.to_dict()
        return self.visit_type_alias(schema, value=value, path=path, **kwargs)
