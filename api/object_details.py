"""
Object Details API

Provides functions for retrieving metadata about a MicroStrategy object.
"""

import json


def get_object_details(client, object_id, object_type):
    """
    Retrieves metadata for a MicroStrategy object.

    Parameters
    ----------
    client : MSTRClient

    object_id : str

    object_type : int
        MicroStrategy object type
        (Report=3, Metric=4, Attribute=12, Folder=8, etc.)
    """

    endpoint = f"/objects/{object_id}"

    params = {
        "type": object_type
    }

    print("\nCalling REST API")
    print("-" * 60)
    print(f"Endpoint : {endpoint}")
    print(f"Type     : {object_type}")

    response = client.get(
        endpoint,
        params=params,
        headers={
            "Accept": "application/json"
        }
    )

    print("\nHTTP Status :", response.status_code)

    if response.status_code != 200:

        print("\nResponse")
        print(response.text)

        raise Exception(
            f"Unable to retrieve object details ({response.status_code})"
        )

    data = response.json()

    print("\nReturned JSON")
    print("-" * 60)

    print(json.dumps(data, indent=4))

    return data