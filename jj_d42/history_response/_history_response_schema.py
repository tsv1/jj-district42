from typing import Any, cast

from d42 import schema
from d42.declaration import SchemaVisitor
from d42.declaration import SchemaVisitorReturnType as ReturnType
from d42.declaration.types import DictSchema, GenericTypeAliasSchema, TypeAliasProps

from jj_d42.types.header_list import HeaderListSchema

__all__ = ("HistoryResponseSchema", "HistoryResponseProps", "ResponseSchema",)


ResponseSchema = schema.dict({
    "status": schema.int,
    "reason": schema.str,
    "headers": HeaderListSchema(),
    "body": schema.any,
    "raw": schema.bytes,
})


class HistoryResponseProps(TypeAliasProps):
    @property
    def type(self) -> DictSchema:
        return cast(DictSchema, self.get("type", ResponseSchema))


class HistoryResponseSchema(GenericTypeAliasSchema[HistoryResponseProps]):
    def __accept__(self, visitor: SchemaVisitor[ReturnType], **kwargs: Any) -> ReturnType:
        try:
            return cast(ReturnType, visitor.visit_jj_history_response(self, **kwargs))
        except AttributeError:
            return visitor.visit_type_alias(self, **kwargs)

    def __add__(self, /, other: DictSchema) -> "HistoryResponseSchema":
        assert isinstance(other, DictSchema)
        merged = self.props.type + other
        return self.__class__(self.props.update(type=merged))
