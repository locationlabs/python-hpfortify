from requests import codes

from hpfortify.api.base import BaseClientApi
from hpfortify.model.feature import TenantFeatureListResponse
from hpfortify.model.tenant import GetTenantResponse

TENANTS_FEATURES_URL = "/api/v3/tenants/features"
TENANTS_URL = "/api/v3/tenants"


class TenantApi(BaseClientApi):

    def __init__(self, **kwargs):
        super(TenantApi, self).__init__(**kwargs)

    def get_tenants(self):
        """
        This method fetches the tenant information for the given access token.
        """
        status_code_dict = {codes.ok: GetTenantResponse}
        return self.get_request(TENANTS_URL, status_code_response_class_dict=status_code_dict)

    def get_tenants_features(self):
        """
        This method fetches the tenant information for the given access token.
        """
        status_code_dict = {codes.ok: TenantFeatureListResponse}
        return self.get_request(TENANTS_FEATURES_URL,
                                status_code_response_class_dict=status_code_dict)
