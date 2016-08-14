
class ApplicationListResponse(object):

    def __init__(self,
                 items,
                 total_count,
        ):

        self.items = items
        self.total_count = total_count


class Application(object):

    def __init__(self,
                 application_id,
                 application_name,
                 application_description,
                 application_created_date,
                 business_criticality_type_id,
                 business_criticality_type,
                 email_list,
                 application_type_id,
                 application_type,
                 attributes,
        ):
        """
        """
        self.application_id = application_id
        self.application_name = application_name
        self.application_description = application_description
        self.application_created_date = application_created_date
        self.business_criticality_type_id = business_criticality_type_id
        self.business_criticality_type = business_criticality_type
        self.email_list = email_list
        self.application_type_id = application_type_id
        self.application_type = application_type
        self.attributes = attributes

    @classmethod
    def from_dict(cls, dct):
        rturn cls(
            application_id=dct["applicationId"]
            )

class ApplicationAttributeExtended(object):

    def __init__(self,
                 name,
                 id,
                 value,
        ):
        """
        :param name: (optional) name of attribute
        :type name: string
        :param id:  (optional) id of attribute
        :type id: integer
        :param value: (optional) value of attribute
        :type value: string
        """
        self.id = id
        self.name = name
        self.value = value
