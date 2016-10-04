from hpfortify.model.audit import (
    AuditAction,
    GetAuditOptionsResponse,
    PostAuditActionRequest,
)
from hpfortify.tests.test_util import assert_from_and_to_dict

GET_AUDIT_OPTIONS_RESPONSE_DICT = {
    "releaseId": 1234,
    "auditProcessing": False,
    "canAudit": True,
    "canChallenge": True,
    "canEdit": True,
    "inAuditMode": False
}

POST_AUDIT_ACTION_REQUEST_DICT = {
    "auditAction": AuditAction.CANCEL.value,
}


def test_get_audit_options_response():
    assert_from_and_to_dict(GetAuditOptionsResponse, GET_AUDIT_OPTIONS_RESPONSE_DICT)


def test_post_audit_action_request():
    assert_from_and_to_dict(PostAuditActionRequest, POST_AUDIT_ACTION_REQUEST_DICT)
