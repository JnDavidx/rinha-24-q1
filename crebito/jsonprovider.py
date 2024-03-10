from datetime import date
from typing import Any

from flask.json.provider import DefaultJSONProvider


class CrebitoJSONProvider(DefaultJSONProvider):

    __slots__ = []

    sort_keys = False

    @staticmethod
    def default(obj: Any) -> Any:
        if isinstance(obj, date):
            return obj.isoformat()

        return DefaultJSONProvider.default(obj)