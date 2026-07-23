def search_reports(client, search_text):
    """
    Search reports by name.
    """

    response = client.get(
        "/searches/results",
        params={
            "name": search_text,
            "type": 3,          # Report
            "pattern": 4,       # Contains
            "limit": 25,
            "getAncestors": True
        },
        headers={
            "Accept": "application/json"
        }
    )

    print("HTTP Status:", response.status_code)

    if response.status_code != 200:
        print(response.text)
        raise Exception("Search failed")

    return response.json()