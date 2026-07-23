def search_objects(
    client,
    search_text,
    object_type=None,
    limit=25
):
    """
    Generic Search API

    Parameters
    ----------
    client : MSTRClient

    search_text : str

    object_type : ObjectType (optional)

    limit : int
    """

    params = {
        "name": search_text,
        "pattern": 4,
        "limit": limit,
        "getAncestors": True
    }

    if object_type is not None:

        params["type"] = object_type.value

    response = client.get(
        "/searches/results",
        params=params,
        headers={
            "Accept": "application/json"
        }
    )

    print("\nHTTP Status :", response.status_code)

    if response.status_code != 200:

        print(response.text)

        raise Exception("Search failed")

    return response.json()