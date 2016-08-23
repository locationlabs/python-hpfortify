from enum import Enum


class AuditPreferenceType(Enum):
    """
    Enum class for audit preference type which is used for scan request.
    """
    MANUAL = "Manual"
    AUTOMATED = "Automated"


class EntitlementFrequencyType(Enum):
    """
    Enum class for Entitlement Frequency type which is used for scan request.
    """
    SUBSCRIPTION = "Subscription"
    SINGLE_SCAN = "SingleScan"


class GetImportScanSessionIdResponse(object):

    def __init__(self, import_scan_session_id=None):
        self.import_scan_session_id = import_scan_session_id

    def to_dict(self):
        return dict(importScanSessionId=self.import_scan_session_id)

    @classmethod
    def from_dict(cls, dct):
        return cls(import_scan_session_id=dct.get("importScanSessionId"))


class GetStaticScanOptionsResponse(object):

    def __init__(self, items=None):
        self.items = items

    def to_dict(self):
        return dict(items=[item.to_dict() for item in self.items] if self.items else None,  # noqa
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(items=[ScanOption.from_dict(item) for item in dct.get("items")] if dct.get("items") else None,  # noqa
                  )


class LookupItem(object):

    def __init__(self, value=None, text=None, group=None):
        self.value = value
        self.text = text
        self.group = group

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, dct):
        return cls(value=dct.get("value"),
                   text=dct.get("text"),
                   group=dct.get("group"),
                   )


class PostStartScanResponse(object):

    def __init__(self, scan_id=None):

        self.scan_id = scan_id

    def to_dict(self):
        return dict(scanId=self.scan_id)

    @classmethod
    def from_dict(cls, dct):
        return cls(scan_id=dct.get("scanId"))


class Scan(object):

    def __init__(self,
                 application_id=None,
                 release_id=None,
                 scan_id=None,
                 scan_type_id=None,
                 scan_type=None,
                 assessment_type_id=None,
                 analysis_status_type_id=None,
                 analysis_status_type=None,
                 started_date_time=None,
                 completed_date_time=None,
                 total_issues=None,
                 star_rating=None,
                 notes=None,
                 is_false_positive_challenge=None,
                 is_remediation_scan=None,
                 ):
        self.application_id = application_id
        self.release_id = release_id
        self.scan_id = scan_id
        self.scan_type_id = scan_type_id
        self.scan_type = scan_type
        self.assessment_type_id = assessment_type_id
        self.analysis_status_type_id = analysis_status_type_id
        self.analysis_status_type = analysis_status_type
        self.started_date_time = started_date_time
        self.completed_date_time = completed_date_time
        self.total_issues = total_issues
        self.star_rating = star_rating
        self.notes = notes
        self.is_false_positive_challenge = is_false_positive_challenge
        self.is_remediation_scan = is_remediation_scan

    def to_dict(self):
        return dict(applicationId=self.application_id,
                    releaseId=self.release_id,
                    scanId=self.scan_id,
                    scanTypeId=self.scan_type_id,
                    scanType=self.scan_type,
                    assessmentTypeId=self.assessment_type_id,
                    analysisStatusTypeId=self.analysis_status_type_id,
                    analysisStatusType=self.analysis_status_type,
                    startedDateTime=self.started_date_time,
                    completedDateTime=self.completed_date_time,
                    totalIssues=self.total_issues,
                    starRating=self.star_rating,
                    notes=self.notes,
                    isFalsePositiveChallenge=self.is_false_positive_challenge,
                    isRemediationScan=self.is_remediation_scan,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(application_id=dct.get("applicationId"),
                   release_id=dct.get("releaseId"),
                   scan_id=dct.get("scanId"),
                   scan_type_id=dct.get("scanTypeId"),
                   scan_type=dct.get("scanType"),
                   assessment_type_id=dct.get("assessmentTypeId"),
                   analysis_status_type_id=dct.get("analysisStatusTypeId"),
                   analysis_status_type=dct.get("analysisStatusType"),
                   started_date_time=dct.get("startedDateTime"),
                   completed_date_time=dct.get("completedDateTime"),
                   total_issues=dct.get("totalIssues"),
                   star_rating=dct.get("starRating"),
                   notes=dct.get("notes"),
                   is_false_positive_challenge=dct.get("isFalsePositiveChallenge"),  # noqa
                   is_remediation_scan=dct.get("isRemediationScan"),
                   )


class ScanListResponse(object):

    def __init__(self, items=None, total_count=None):
        self.items = items
        self.total_count = total_count

    def to_dict(self):
        return dict(items=[item.to_dict() for item in self.items] if self.items else None,  # noqa
                    totalCount=self.total_count,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(items=[Scan.from_dict(item) for item in dct.get("items")] if dct.get("items") else None,  # noqa
                   total_count=dct.get("totalCount"),
                   )


class ScanOption(object):

    def __init__(self,
                 id=None,
                 name=None,
                 last_selected_option=None,
                 options=None,
                 ):
        self.id = id
        self.name = name
        self.last_selected_option = last_selected_option
        self.options = options

    def to_dict(self):
        return dict(id=self.id,
                    name=self.name,
                    lastSelectedOption=self.last_selected_option,
                    options=[item.to_dict() for item in self.options] if self.options else None,  # noqa
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(id=dct.get("id"),
                   name=dct.get("name"),
                   last_selected_option=dct.get("lastSelectedOption"),
                   options=[LookupItem.from_dict(item) for item in dct.get("optons")] if dct.get("options") else None,  # noqa
                   )


class ScanPreferenceType(Enum):
    """
    Enum class for Scan Preference Type which is used for scan request.
    """
    STANDARD = "Standard"
    EXPRESS = "Express"


class TechnologyStack(Enum):
    """
    Enum class for Technology stack which can be used for scan request.
    """
    ABAP = "ABAP"
    ANDROID = "Android"
    ASP = "ASP"
    C_AND_C_PLUS_PLUS = "C/C++"
    CFML = "CFML"
    COBOL = "COBOL"
    IOS = "iOS Swift & Objective-C/C++"
    JAVA = "Java/J2EE"
    MBS = "MBS"
    PHP = "PHP"
    SQL = "PL/SQL & T-SQL"
    PYTHON = "PYTHON"
    RUBY = "Ruby"
    VB6 = "VB6"
    VB_SCRIPT = "VBScript"
    XML_HTML = "XML/HTML"
    DOT_NET = ".NET"
    OTHER = "OTHER"
