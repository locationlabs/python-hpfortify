class GetTenantResponse(object):

    def __init__(self, tenant_name=None, tenant_code=None, time_zone=None):
        self.tenant_name = tenant_name
        self.tenant_code = tenant_code
        self.time_zone = time_zone

    def to_dict(self):
        return dict(tenantName=self.tenant_name,
                    tenantCode=self.tenant_code,
                    timeZone=self.time_zone,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(tenant_name=dct.get("tenantName"),
                   tenant_code=dct.get("tenantCode"),
                   time_zone=dct.get("timeZone"),
                   )
