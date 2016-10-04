"""
This module contains base resource classes.
"""
from abc import ABCMeta, abstractmethod


class Resource(object):
    """
    This is the base class for resource/DTO class
    """
    __metaclass__ = ABCMeta

    def _dict_no_none(self, **kwargs):
        """
        This is a helper method to remove fields whose value is None. HPfortify doesn't like
        request which has none value field.
        """
        return {
            k: v
            for k, v in kwargs.iteritems()
            if v is not None
        }

    @abstractmethod
    def to_dict(self):
        pass

    @classmethod
    def from_dict(cls, resource_dict):
        raise NotImplementedError()


class ResourceList(Resource):
    """
    This is a base class for resource list.
    """
    def __init__(self, items=None, total_count=None):
        self.items = items
        self.total_count = total_count

    @classmethod
    def items_class(cls):
        raise NotImplementedError("`items_class` method is not implemented")

    def to_dict(self):
        return {
            "items": [item.to_dict() for item in self.items] if self.items else None,
            "totalCount": self.total_count,
        }

    @classmethod
    def from_dict(cls, dct):
        return cls(
            items=[cls.items_class().from_dict(item) for item in dct.get("items")] if dct.get("items") else None,  # noqa
            total_count=dct.get("totalCount"),
        )
