class Fields(object):
    def __init__(self, client):
        self.client = client

    def update_custom_field_text_value(self, contact_id, field_id, value):
        """
        Update a value for a custom field


        Args:
            contact_id: string
            field_id: string
            value: string

        Returns:


        """
        data = {"fieldValue":{"contact":str(contact_id),"field":str(field_id),"value":str(value)}}

        return self.client._post("/fieldValues", json=data)

