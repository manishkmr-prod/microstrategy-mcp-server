from mstr_client import MSTRClient
from api.authentication import login
from api.projects import list_projects
from api.folders import list_root_folders, browse_folder


def main():

    client = MSTRClient()

    print("Connecting to MicroStrategy...")

    login(client)

    print("Login Successful\n")

    # --------------------------------------------------
    # List Projects
    # --------------------------------------------------

    projects = list_projects(client)

    print("Available Projects")
    print("-" * 60)

    for index, project in enumerate(projects, start=1):
        print(f"{index}. {project['name']}")

    choice = int(input("\nSelect Project Number : "))

    selected_project = projects[choice - 1]

    client.set_project(selected_project["id"])

    print("\nSelected Project")
    print("-" * 60)
    print(selected_project["name"])

    # --------------------------------------------------
    # Root folders
    # --------------------------------------------------

    folders = list_root_folders(client)

    print("\nRoot Folders")
    print("-" * 60)

    for index, folder in enumerate(folders, start=1):
        print(f"{index}. {folder['name']}")

    folder_choice = int(input("\nSelect Folder : "))

    selected_folder = folders[folder_choice - 1]

    print("\nBrowsing Folder")
    print("-" * 60)
    print(selected_folder["name"])

    # --------------------------------------------------
    # Browse Selected Folder
    # --------------------------------------------------

    contents = browse_folder(client, selected_folder["id"])

    print("\nContents")
    print("-" * 60)

    if not contents:
        print("Folder is empty.")
    else:
        for index, obj in enumerate(contents, start=1):
            print(f"{index}. {obj['name']} ({obj['id']})")


if __name__ == "__main__":
    main()