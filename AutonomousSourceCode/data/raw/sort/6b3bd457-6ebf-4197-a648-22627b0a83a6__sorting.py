import functools

from flask import request
from sqlalchemy import desc

from ._compat import httplib
from .request_utils import error_abort


def sort_query(query, allowed_fields=(), default=None):
    allowed_fields = set(allowed_fields)
    sort_param = request.args.get("sort", None)
    if sort_param:
        sort_fields = sort_param.split(",")

        for sort_field in sort_fields:
            descending = sort_field.startswith("-")
            if descending:
                sort_field = sort_field[1:]

            if sort_field not in allowed_fields:
                error_abort(httplib.BAD_REQUEST, "Cannot sort by field {0!r}".format(sort_field))
            query = query.order_by(desc(sort_field) if descending else sort_field)
    elif default is not None:
        query = query.order_by(default)

    return query


def sorted_view(func=None, **sort_kwargs):
    if func is None:
        return functools.partial(sorted_view, **sort_kwargs)

    @functools.wraps(func)
    def new_func(*args, **kwargs):
        returned = func(*args, **kwargs)
        return sort_query(returned, **sort_kwargs)

    return new_func
