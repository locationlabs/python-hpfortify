from enum import Enum


class AuditAction(Enum):
    """
    This Enum class represents Audit Action type.
    """
    CANCEL = "Cancel"
    START = "Start"
    SUBMIT = "Submit"


class GetAuditOptionsResponse(object):

    def __init__(self,
                 release_id=None,
                 audit_processing=None,
                 can_audit=None,
                 can_challenge=None,
                 can_edit=None,
                 in_audit_mode=None,
                 ):

        self.release_id = release_id
        self.audit_processing = audit_processing
        self.can_audit = can_audit
        self.can_challenge = can_challenge
        self.can_edit = can_edit
        self.in_audit_mode = in_audit_mode

    def to_dict(self):
        return dict(releaseId=self.release_id,
                    auditAction=self.audit_action,
                    canAudit=self.can_audit,
                    canChallenge=self.can_challenge,
                    canEdit=self.can_edit,
                    inAuditMode=self.in_audit_mode,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(release_id=dct.get("releaseId"),
                   audit_action=dct.get("auditAction"),
                   can_audit=dct.get("canAudit"),
                   can_challenge=dct.get("canChallenge"),
                   can_edit=dct.get("canEdit"),
                   in_audit_mode=dct.get("inAuditMode"),
                   )


class PostAuditActionRequest(object):

    def __init__(self, audit_action=None):
        self.audit_action = audit_action

    def to_dict(self):
        return dict(auditAction=self.audit_action.value)

    @classmethod
    def from_dict(cls, dct):
        return cls(audit_action=AuditAction(dct.get("auditAction")) if dct.get("auditAction") else None)  # noqa
