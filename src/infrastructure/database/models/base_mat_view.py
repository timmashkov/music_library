from typing import Any

from sqlalchemy import (
    DDL,
    Column,
    DDLElement,
    PrimaryKeyConstraint,
    Table,
    event,
    select,
)
from sqlalchemy.ext import compiler

from infrastructure.database.models import Base


class CreateMaterialized(DDLElement):

    def __init__(self, name: str, selectable: select) -> None:
        self.name = name
        self.selectable = selectable


@compiler.compiles(CreateMaterialized)
def mat_compile(element, mat_compiler: Any, **kwargs: Any) -> str:
    return "CREATE MATERIALIZED VIEW %s AS %s" % (
        element.name,
        mat_compiler.sql_compiler.process(element.selectable, literal_binds=True),
    )


def create_mat_view(metadata, name, selectable):
    _internal_metadata = (
        Base.metadata
    )  # temp metadata just for initial Table object creation
    t = Table(
        name, _internal_metadata
    )  # the actual mat view class is bound to db.metadata
    for c in selectable.c:
        t.append_column(Column(c.name, c.type, primary_key=c.primary_key))

    if not (any([c.primary_key for c in selectable.c])):
        t.append_constraint(PrimaryKeyConstraint(*[c.name for c in selectable.c]))

    event.listen(metadata, "after_create", CreateMaterialized(name, selectable))

    @event.listens_for(metadata, "after_create")
    def create_indexes(target, connection, **kw):
        for idx in t.indexes:
            idx.create(connection)

    event.listen(
        metadata, "before_drop", DDL("DROP MATERIALIZED VIEW IF EXISTS " + name)
    )
    return t
