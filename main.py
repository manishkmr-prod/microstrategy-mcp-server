from mstr_client import MSTRClient
from api.authentication import login
from api.projects import list_projects
from api.folders import list_folders

# Replace this with the Project ID you want to browse
PROJECT_ID = "205BABE083484404399FBBA37BAA874A"


def main():
    client = MSTRClient()

    print("Connecting to MicroStrategy...")

    login(client)

    print("Login Successful\n")

    # List all available projects
    projects = list_projects(client)

    print("Available Projects")
    print("-" * 50)

    for project in projects:
        print(f"{project['name']} ({project['id']})")

    # List folders for the selected project
    print("\nFolders")
    print("-" * 50)

    folders = list_folders(client, PROJECT_ID)

    for folder in folders:
        print(f"{folder['name']} ({folder['id']})")


if __name__ == "__main__":
    main()