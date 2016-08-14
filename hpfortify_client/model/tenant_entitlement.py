from json import dumps, loads


class GetTenantEntitlementResponse(object):

    def __init__(self,
                 entitlement_type_id,  # integer (optional)
                 entitlement_type,  # string (optional)
                 subscription_type_id,  # integer (optional)
                 subscription_type,  # string (optional)
                 tenant_entitlements, # list of TenantEntitlement (optional)
        ):
        self.entitlement_type_id = entitlement_type_id
        self.entitlement_type = entitlement_type
        self.subscription_type_id = subscription_type_id
        self.subscription_type = subscription_type
        self.tenant_entitlements = tenant_entitlements

    def to_json(self):
        return dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        return cls(**loads(json_str))


class TenantEntitlement(object):

    def __init__(self,
                 entitlement_id,  # integer (optional)
                 units_purchased,  # integer (optional)
                 units_consumed,  # integer
                 start_date,  # string (optional)
                 end_date,  # string (optional)
                 extended_properties,  #  TenantEntitlementExtendedProperties (optional)
        ):
        self.entitlement_id = entitlement_id
        self.units_purchased = units_purchased
        self.units_consumed = units_consumed
        self.start_date = start_date
        self.end_date = end_date
        self.extended_properties = extended_properties

    def to_json(self):
        return dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        return cls(**loads(json_str))


class TenantEntitlementExtendedProperties(object):

    def __init__(self,
                 assessment_type_id,  # integer (optional)
                 frequency_type_id,  # integer (optional)
                 frequency_type,  # string (optional)
                 subscription_length):  # String (optional)
        self.assessment_type_id = assessment_type_id
        self.frequency_type_id = frequency_type_id
        self.frequency_type = frequency_type
        self.subscription_length = subscription_length

    def to_json(self):
        return dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        return cls(**loads(json_str))
