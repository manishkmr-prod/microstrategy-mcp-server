"""
Changeset APIs

Reusable SDK functions for the
MicroStrategy Modeling Service.
"""


def create_changeset(
    client,
    schema_edit=False
):
    """
    Create a Modeling Changeset.

    Parameters
    ----------
    client : MSTRClient

    schema_edit : bool
        True when editing schema objects.
        False for read-only operations.

    Returns
    -------
    dict
    """

    endpoint = "/model/changesets"

    print("\nCalling REST API")
    print("-" * 60)
    print(f"Endpoint : {endpoint}")

    response = client.post(
        endpoint,
        params={
            "schemaEdit": str(schema_edit).lower()
        },
        headers={
            "Accept": "application/json"
        }
    )

    print("\nHTTP Status :", response.status_code)

    if response.status_code != 201:

        print("\nResponse")
        print(response.text)

        raise Exception(
            f"Unable to create Changeset ({response.status_code})"
        )

    return response.json()