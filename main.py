from mstr_client import MSTRClient
from api.authentication import login
from api.projects import list_projects
from api.folders import list_root_folders, browse_folder
from api.search import search_objects

from utils.menu import Menu


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

    print("\nBrowsing Folder")
    print("-" * 60)
    print(selected_folder["name"])

    # --------------------------------------------------
    # Browse Folder
    # --------------------------------------------------

    contents = browse_folder(
        client,
        selected_folder["id"]
    )

    print("\nContents")
    print("-" * 60)

    if not contents:
        print("Folder is empty.")
    else:
        for index, obj in enumerate(contents, start=1):
            print(f"{index}. {obj['name']} ({obj['id']})")

    # --------------------------------------------------
    # Object Type Selection
    # --------------------------------------------------

    object_type = Menu.select_object_type()

    search_text = input("\nSearch Text : ")

    results = search_objects(
        client,
        search_text,
        object_type
    )

    # --------------------------------------------------
    # Display Search Results
    # --------------------------------------------------

    print("\nSearch Results")
    print("-" * 80)

    print(f"Total Results : {results['totalItems']}")
    print()

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