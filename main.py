from mstr_client import MSTRClient
from api.authentication import login
from api.projects import list_projects
from api.folders import list_root_folders, browse_folder
from api.search import search_objects
from api.object_details import get_object_details

from utils.menu import Menu
from utils.object_types import ObjectType


# --------------------------------------------------
# NEW FUNCTION
# Pretty-print object details
# --------------------------------------------------

def print_object_details(details):

    print("\n")
    print("=" * 60)
    print("Object Details")
    print("=" * 60)

    print(f"Name         : {details.get('name', '-')}")
    print(f"ID           : {details.get('id', '-')}")
    print(f"Type         : {ObjectType(details.get('type')).name.title() if details.get('type') in [item.value for item in ObjectType] else details.get('type', '-')}")

    print(f"Description  : {details.get('description', '-')}")

    owner = details.get("owner", {})

    print(f"Owner        : {owner.get('name', '-')}")
    print(f"Created      : {details.get('dateCreated', '-')}")
    print(f"Modified     : {details.get('dateModified', '-')}")
    print(f"Version      : {details.get('version', '-')}")

    print("=" * 60)


def main():

    client = MSTRClient()

    print("Connecting to MicroStrategy...")

    login(client)

    print("Login Successful\n")

    # --------------------------------------------------
    # Project Selection
    # --------------------------------------------------

    projects = list_projects(client)

    selected_project = Menu.select_project(projects)

    client.set_project(selected_project["id"])

    print("\nSelected Project")
    print("-" * 60)
    print(selected_project["name"])

    # --------------------------------------------------
    # Root Folder Selection
    # --------------------------------------------------

    folders = list_root_folders(client)

    selected_folder = Menu.select_root_folder(folders)

    if selected_folder == "ALL":

        print("\nBrowsing ALL Root Folders")
        print("-" * 60)

        for folder in folders:

            print(f"\n{folder['name']}")

            contents = browse_folder(client, folder["id"])

            for obj in contents:
                print(f"  {obj['name']}")

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

    object_choice = int(input("\nSelect Object Number : "))

    selected_object = search_results[object_choice - 1]

    details = get_object_details(
        client,
        selected_object["id"],
        selected_object["type"]
    )

    # --------------------------------------------------
    # NEW CODE
    # Pretty-print object details
    # --------------------------------------------------

    print_object_details(details)


if __name__ == "__main__":
    main()