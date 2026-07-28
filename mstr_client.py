import requests

from config import settings


class MSTRClient:

    def __init__(self):

        self.base_url = settings.MSTR_BASE_URL
        self.verify_ssl = settings.VERIFY_SSL

        self.session = requests.Session()
        self.session.verify = self.verify_ssl

        self.auth_token = None
        self.project_id = None
        self.changeset_id = None

    # --------------------------------------------------
    # Authentication
    # --------------------------------------------------

    def set_auth_token(self, token):

        self.auth_token = token

        self.session.headers.update({
            "X-MSTR-AuthToken": token
        })

    # --------------------------------------------------
    # Project
    # --------------------------------------------------

    def set_project(self, project_id):

        self.project_id = project_id

        self.session.headers.update({
            "X-MSTR-ProjectID": project_id
        })

    def clear_project(self):

        self.project_id = None

        self.session.headers.pop(
            "X-MSTR-ProjectID",
            None
        )

    # --------------------------------------------------
    # Modeling Changeset
    # --------------------------------------------------

    def set_changeset(self, changeset_id):

        """
        Store the active Modeling Changeset.

        The Changeset is NOT automatically added
        to every request because only certain
        Modeling APIs require it.
        """

        self.changeset_id = changeset_id

    def clear_changeset(self):

        self.changeset_id = None

    # --------------------------------------------------
    # HTTP Methods
    # --------------------------------------------------

    def get(self, endpoint, **kwargs):

        url = f"{self.base_url}{endpoint}"

        return self.session.get(
            url,
            **kwargs
        )

    def post(self, endpoint, **kwargs):

        url = f"{self.base_url}{endpoint}"

        return self.session.post(
            url,
            **kwargs
        )

    def put(self, endpoint, **kwargs):

        url = f"{self.base_url}{endpoint}"

        return self.session.put(
            url,
            **kwargs
        )

    def delete(self, endpoint, **kwargs):

        url = f"{self.base_url}{endpoint}"

        return self.session.delete(
            url,
            **kwargs
        )