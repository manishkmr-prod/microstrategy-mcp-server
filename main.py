from mstr_client import MSTRClient
from api.authentication import login
from api.projects import list_projects
from api.folders import list_root_folders, browse_folder
from api.search import search_objects
from api.object_details import get_object_details

from utils.menu import Menu
from utils.object_types import ObjectType

import json


def main():

    client = MSTRClient()

    print("Connecting to MicroStrategy...")

    login(client)

    print("Login Successful\n")

    # --------------------------------------------------
    # Select Project
    # --------------------------------------------------

    projects = list_projects(client)

    selected_project = Menu.select_project(projects)

    client.set_project(selected_project["id"])

    print("\nSelected Project")
    print("-" * 60)
    print(selected_project["name"])

    # --------------------------------------------------
    # Browse Root Folder
    # --------------------------------------------------

    folders = list_root_folders(client)

    selected_folder = Menu.select_root_folder(folders)

    # --------------------------------------------------
    # Browse ALL Root Folders
    # --------------------------------------------------

    if selected_folder == "ALL":

        print("\nBrowsing ALL Root Folders")
        print("-" * 60)

        all_objects = []

        for folder in folders:

            print(f"\n{folder['name']}")

            contents = browse_folder(client, folder["id"])

            for obj in contents:
                print(f"  {obj['name']}")

                all_objects.append(obj)

    # --------------------------------------------------
    # Browse Single Folder
    # --------------------------------------------------

    else:

        print("\nBrowsing Folder")
        print("-" * 60)

        print(selected_folder["name"])

        contents = browse_folder(client, selected_folder["id"])

        print("\nContents")
        print("-" * 60)

        if not contents:

            print("Folder is empty.")

        else:

            for index, obj in enumerate(contents, start=1):
                print(f"{index}. {obj['name']} ({obj['id']})")

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    print("\nSearch Objects")
    print("-" * 60)

    object_type = Menu.select_object_type()

    search_text = input("\nSearch Text : ")

    results = search_objects(
        client,
        search_text,
        object_type.value
    )

    print("\nSearch Results")
    print("-" * 60)

    search_results = results.get("result", [])

    if not search_results:

        print("No objects found.")
        return

    for index, obj in enumerate(search_results, start=1):

        print(f"{index}. {obj['name']} ({obj['id']})")

    # --------------------------------------------------
    # NEW CODE - Select Object
    # --------------------------------------------------

    object_choice = int(input("\nSelect Object : "))

    selected_object = search_results[object_choice - 1]

    # --------------------------------------------------
    # NEW CODE - Object Details
    # --------------------------------------------------

    details = get_object_details(
        client,
        selected_object["id"],
        selected_object["type"]
    )

    print("\nObject Details")
    print("-" * 60)

    print(json.dumps(details, indent=4))


if __name__ == "__main__":
    main()