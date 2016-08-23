class ReleaseAssessmentType(object):

    def __init__(self,
                 assessment_type_id=None,
                 name=None,
                 scan_type=None,
                 scan_type_id=None,
                 entitlement_id=None,
                 frequency_type=None,
                 frequency_type_id=None,
                 units=None,
                 units_available=None,
                 subscription_end_date=None,
                 is_remediation=None,
                 remediation_scans_available=None,
                 ):
        self.assessment_type_id = assessment_type_id
        self.name = name
        self.scan_type = scan_type
        self.scan_type_id = scan_type_id
        self.entitlement_id = entitlement_id
        self.frequency_type = frequency_type
        self.frequency_type_id = frequency_type_id
        self.units = units
        self.units_available = units_available
        self.subscription_end_date = subscription_end_date
        self.is_remediation = is_remediation
        self.remediation_scans_available = remediation_scans_available

    def to_dict(self):
        return dict(assessmentTypeId=self.assessment_type_id,
                    name=self.name,
                    scanType=self.scan_type,
                    scanTypeId=self.scan_type_id,
                    entitlementId=self.entitlement_id,
                    frequencyType=self.frequency_type,
                    frequencyTypeId=self.frequency_type_id,
                    units=self.units,
                    unitsAvailable=self.units_available,
                    subscriptionEndDate=self.subscription_end_date,
                    isRemediation=self.is_remediation,
                    remediationScansAvailable=self.remediation_scans_available,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(assessment_type_id=dct.get("assessmentTypeId"),
                   name=dct.get("name"),
                   scan_type=dct.get("scanType"),
                   scan_type_id=dct.get("scanTypeId"),
                   entitlement_id=dct.get("entitlementId"),
                   frequency_type=dct.get("frequencyType"),
                   frequency_type_id=dct.get("frequencyTypeId"),
                   units=dct.get("units"),
                   units_available=dct.get("unitsAvailable"),
                   subscription_end_date=dct.get("subscriptionEndDate"),
                   is_remediation=dct.get("isRemediation"),
                   remediation_scans_available=dct.get("remediationScansAvailable"),  # noqa
                  )


class ReleaseAssessmentTypeListResponse(object):

    def __init__(self, items=None, total_count=None):
        self.items = items
        self.total_count = total_count

    def to_dict(self):
        return dict(items=[item.to_dict() for item in self.items] if self.items else None,  # noqa
                    totalCount=self.total_count,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(items=[ReleaseAssessmentType.from_dict(item) for item in dct.get("items")] if dct.get("items") else None,  # noqa
                   total_count=dct.get("totalCount"),
                   )
