from hpfortify_client.api.appilcation import (
    get_applications,
)
from hpfortify_client.api.auth import (
    authorize,
)
from hpfortify_client.api.tenant_entitlement import (
    get_tenant_entitlements
)
from hpfortify_client.api.util import (
    BASE_URL_US,
)


def main():
    credential_file = open("/tmp/hpfortify")

    response = authorize(BASE_URL_US,
                         credential_file.readline().strip(),
                         credential_file.readline().strip())
    print response
    # response = get_tenant_entitlements(BASE_URL_US, response.access_token)
    response = get_applications(BASE_URL_US, response.access_token)
    import ipdb; ipdb.set_trace()
    print response
    response = expire_access_token(BASE_URL_US, response.access_token)
    print response

if __name__ == "__main__":
    main()
