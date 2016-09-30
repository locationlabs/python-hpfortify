class TenantFeature(object):

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def to_dict(self):
        return dict(id=self.id, name=self.name)

    @classmethod
    def from_dict(cls, dct):
        return cls(id=dct.get("id"), name=dct.get("name"))


class TenantFeatureListResponse(object):

    def __init__(self, items, total_count):
        self.items = items
        self.total_count = total_count

    def to_dict(self):
        return dict(items=[item.to_dict() for item in self.items] if self.items else None,  # noqa
                    totalCount=self.total_count,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(items=[TenantFeature.from_dict(item) for item in dct.get("items")] if dct.get("items") else None,  # noqa
                   total_count=dct.get("totalCount"),
                   )
