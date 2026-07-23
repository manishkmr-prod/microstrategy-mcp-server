def list_root_folders(client):
    """
    Returns the root folders for the selected project.
    """

    response = client.get(
        "/folders",
        headers={
            "Accept": "application/json"
        }
    )

    if response.status_code != 200:
        raise Exception(
            f"Unable to retrieve root folders ({response.status_code})\n{response.text}"
        )

    return response.json()


def browse_folder(client, folder_id):
    """
    Returns the contents of a folder.
    """

    response = client.get(
        f"/folders/{folder_id}",
        headers={
            "Accept": "application/json"
        }
    )

    if response.status_code != 200:
        raise Exception(
            f"Unable to browse folder ({response.status_code})\n{response.text}"
        )

    return response.json()