from requests import codes

from hpfortify.api.base import BaseClientApi
from hpfortify.model.common import ErrorResponse
from hpfortify.model.scan import PostStartScanResponse

POST_STATIC_SCAN_URL = "/api/v3/releases/{release_id}/static-scans/start-scan"
MAX_FILE_FRAGMENT_SIZE = 1024 * 1024  # 1MB


class StaticScanApi(BaseClientApi):

    def __init__(self, **kwargs):
        super(StaticScanApi, self).__init__(**kwargs)

    def post_static_scans(self,
                          file_path,
                          release_id,
                          assessment_type_id,
                          technology_stack,
                          entitlement_id,
                          entitlement_frequency_type,
                          language_level=None,
                          is_remediation_scan=False,
                          do_sonatype_scan=False,
                          exclude_third_party_libs=True,
                          scan_preference_type=None,
                          audit_preference_type=None,
                          ):

        parameters = dict(assessmentTypeId=assessment_type_id,
                          technologyStack=technology_stack,
                          entitlementId=entitlement_id,
                          entitlementFrequencyType=entitlement_frequency_type,
                          languageLevel=language_level,
                          isRemediationScan=is_remediation_scan,
                          doSonatypeScan=do_sonatype_scan,
                          excludeThirdPartyLibs=exclude_third_party_libs,
                          scanPreferenceType=scan_preference_type,
                          auditPreferenceType=audit_preference_type,
                          )
        offset = 0
        fragment_number = 0
        with open(file_path, "rb") as file:

            while True:
                file_fragment = file.read(MAX_FILE_FRAGMENT_SIZE)
                if len(file_fragment) == MAX_FILE_FRAGMENT_SIZE:
                    parameters['offset'] = offset
                    parameters['fragNo'] = fragment_number
                    offset = offset + len(file_fragment)
                    response = self.post_request(POST_STATIC_SCAN_URL.format(release_id=release_id),  # noqa
                                                 data=file_fragment,
                                                 params=parameters,
                                                 )
                    print response
                else:
                    # This is last file fragment
                    fragment_number = -1
                    parameters['offset'] = offset
                    parameters['fragNo'] = fragment_number
                    offset = offset + len(file_fragment)
                    status_code_dict = {
                        codes.ok: PostStartScanResponse,
                        codes.bad_request: ErrorResponse,
                        codes.unprocessable_entity: ErrorResponse,
                        codes.internal_server_error: ErrorResponse,
                    }

                    response = self.post_request(POST_STATIC_SCAN_URL.format(release_id=release_id),  # noqa
                                                 data=file_fragment,
                                                 params=parameters,
                                                 status_code_response_class_dict=status_code_dict)

                    print "Total bytes sent: ", offset
                    return response

                # Calculate parameters for next iteration
                fragment_number = fragment_number + 1
