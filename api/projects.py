def list_projects(client):
    response = client.get(
        "/projects",
        headers={
            "Accept": "application/json"
        }
    )

    if response.status_code != 200:
        raise Exception(
            f"Unable to retrieve projects ({response.status_code})\n{response.text}"
        )

    return response.json()