"""
Object Details API

Provides functions for retrieving metadata about a MicroStrategy object.
"""

import json


def get_object_details(client, object_id):
    """
    Retrieves metadata for a MicroStrategy object.

    Parameters
    ----------
    client : MSTRClient
        Authenticated client.

    object_id : str
        MicroStrategy object ID.

    Returns
    -------
    dict
        JSON response from the REST API.
    """

    endpoint = f"/objects/{object_id}"

    print("\nCalling REST API")
    print("-" * 60)
    print(f"Endpoint : {endpoint}")

    response = client.get(
        endpoint,
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