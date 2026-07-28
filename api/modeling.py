"""
Modeling Service APIs

Reusable SDK functions for working with
the MicroStrategy Modeling Service.
"""


def create_modeling_instance(client):
    """
    Create a Modeling Service instance.

    Parameters
    ----------
    client : MSTRClient

    Returns
    -------
    str
        Modeling Service Instance ID
    """

    endpoint = "/model"

    print("\nCalling REST API")
    print("-" * 60)
    print(f"Endpoint : {endpoint}")

    response = client.post(
        endpoint,
        headers={
            "Accept": "application/json"
        }
    )

    print("\nHTTP Status :", response.status_code)

    if response.status_code not in (200, 201):

        print("\nResponse")
        print(response.text)

        raise Exception(
            f"Unable to create Modeling Service instance ({response.status_code})"
        )

    instance_id = response.headers.get("X-MSTR-MS-Instance")

    if not instance_id:

        raise Exception(
            "Modeling Service Instance header was not returned."
        )

    print("\nModeling Service Instance")
    print("-" * 60)
    print(instance_id)

    return instance_id