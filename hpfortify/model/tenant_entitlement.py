
class GetTenantEntitlementResponse(object):

    def __init__(self,
                 entitlement_type_id=None,
                 entitlement_type=None,
                 subscription_type_id=None,
                 subscription_type=None,
                 tenant_entitlements=None,
                 ):
        self.entitlement_type_id = entitlement_type_id
        self.entitlement_type = entitlement_type
        self.subscription_type_id = subscription_type_id
        self.subscription_type = subscription_type
        self.tenant_entitlements = tenant_entitlements

    def to_dict(self):
        return dict(entitlementTypeId=self.entitlement_type_id,
                    entitlementType=self.entitlement_type,
                    subscriptionTypeId=self.subscription_type_id,
                    subscriptionType=self.subscription_type,
                    tenantEntitlements=[element.to_dict() for element in self.tenant_entitlements] if self.tenant_entitlements else None,  # noqa
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(entitlement_type_id=dct.get("entitlementTypeId"),
                   entitlement_type=dct.get("entitlementType"),
                   subscription_type_id=dct.get("subscriptionTypeId"),
                   subscription_type=dct.get("subscriptionType"),
                   tenant_entitlements=[TenantEntitlement.from_dict(element) for element in dct.get("tenantEntitlements")] if dct.get("tenantEntitlements") else None,  # noqa
                   )


class TenantEntitlement(object):

    def __init__(self,
                 entitlement_id,
                 units_purchased,
                 units_consumed,
                 start_date,
                 end_date,
                 extended_properties,
                 ):
        self.entitlement_id = entitlement_id
        self.units_purchased = units_purchased
        self.units_consumed = units_consumed
        self.start_date = start_date
        self.end_date = end_date
        self.extended_properties = extended_properties

    def to_dict(self):
        return dict(entitlementId=self.entitlement_id,
                    unitsPurchased=self.units_purchased,
                    unitsConsumed=self.units_consumed,
                    startDate=self.start_date,
                    endDate=self.end_date,
                    extendedProperties=self.extended_properties.to_dict() if self.extended_properties else None,  # noqa
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(entitlement_id=dct.get("entitlementId"),
                   units_purchased=dct.get("unitsPurchased"),
                   units_consumed=dct.get("unitsConsumed"),
                   start_date=dct.get("startDate"),
                   end_date=dct.get("endDate"),
                   extended_properties=TenantEntitlementExtendedProperties.from_dict(dct.get("extendedProperties")) if dct.get("extendedProperties") else None,  # noqa
                   )


class TenantEntitlementExtendedProperties(object):

    def __init__(self,
                 assessment_type_id,
                 frequency_type_id,
                 frequency_type,
                 subscription_length
                 ):
        self.assessment_type_id = assessment_type_id
        self.frequency_type_id = frequency_type_id
        self.frequency_type = frequency_type
        self.subscription_length = subscription_length

    def to_dict(self):
        return dict(assessmentTypeId=self.assessment_type_id,
                    frequencyTypeId=self.frequency_type_id,
                    frequencyType=self.frequency_type,
                    subscriptionLength=self.subscription_length,
                    )

    @classmethod
    def from_dict(cls, dct):
        return cls(assessment_type_id=dct.get("assessmentTypeId"),
                   frequency_type_id=dct.get("frequencyTypeId"),
                   frequency_type=dct.get("frequencyType"),
                   subscription_length=dct.get("subscriptionLength"),
                   )
