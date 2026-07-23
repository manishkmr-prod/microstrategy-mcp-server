from mstr_client import MSTRClient
from api.authentication import login
from api.projects import list_projects
from api.folders import list_root_folders, browse_folder
from api.search import search_objects

from utils.menu import Menu


def display_folder_contents(client, folder):
    """
    Browse and display a folder.
    """

    print("\n" + "=" * 80)
    print(folder["name"])
    print("=" * 80)

    contents = browse_folder(client, folder["id"])

    if not contents:
        print("Folder is empty.")
        return

    for index, obj in enumerate(contents, start=1):
        print(f"{index}. {obj['name']} ({obj['id']})")


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

    selection = Menu.select_root_folder(folders)

    # --------------------------------------------------
    # Browse ALL Root Folders
    # --------------------------------------------------

    if selection == "ALL":

        for folder in folders:
            display_folder_contents(client, folder)

    # --------------------------------------------------
    # Browse Selected Folder
    # --------------------------------------------------

    else:

        display_folder_contents(client, selection)

    # --------------------------------------------------
    # Object Search
    # --------------------------------------------------

    object_type = Menu.select_object_type()

    search_text = input("\nSearch Text : ")

    results = search_objects(
        client,
        search_text,
        object_type
    )

    print("\nSearch Results")
    print("-" * 80)

    print(f"Total Results : {results['totalItems']}\n")

    if results["totalItems"] == 0:

        print("Nothing found.")

    else:

        for index, obj in enumerate(results["result"], start=1):

            print(f"{index}. {obj['name']}")
            print(f"   ID          : {obj['id']}")
            print(f"   Type        : {obj['type']}")

            if obj.get("description"):
                print(f"   Description : {obj['description']}")

            print()


if __name__ == "__main__":
    main()