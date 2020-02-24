class Tags(object):
    def __init__(self, client):
        self.client = client

    def create_a_tag(self, tag_id, contact_id):
        """
        Create a new tag


        Args:
            tag_id: string
            contact_id: string

        Returns:


        """
        data = {"contactTag":{"contact":str(contact_id),"tag":str(tag_id)}}

        return self.client._post("/contactTags", json=data)

    def delete_a_tag(self, contact_tag_id):
        """
        Retrieve an existing user


        Args:
            contact_tag_id:

        Returns:

        """
        return self.client._delete(f"/contactTags/{str(contact_tag_id)}")
