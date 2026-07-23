def list_folders(client, project_id, folder_id=None):

    endpoint = "/folders"

    params = {
        "projectId": project_id
    }

    if folder_id:
        params["folderId"] = folder_id

    response = client.get(
        endpoint,
        params=params,
        headers={
            "Accept": "application/json"
        }
    )

    if response.status_code != 200:
        raise Exception(
            f"Unable to retrieve folders ({response.status_code})\n{response.text}"
        )

    return response.json()