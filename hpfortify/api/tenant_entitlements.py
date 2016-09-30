from requests import codes
from hpfortify.model.tenant_entitlement import (  # noqa
    GetTenantEntitlementResponse,
)
from hpfortify.api.base import BaseClientApi

TENANT_ENTITLEMENT_URL = "/api/v3/tenant-entitlements"


class TenantEntitlementsApi(BaseClientApi):

    def __init__(self, **kwargs):
        super(TenantEntitlementsApi, self).__init__(**kwargs)

    def get_tenant_entitlements(self):
        """
        This method fetches all the entitlement associated with the account.
        """
        status_code_dict = {codes.ok: GetTenantEntitlementResponse}
        return self.get_request(TENANT_ENTITLEMENT_URL,
                                status_code_response_class_dict=status_code_dict)
