import json

from mstr_client import MSTRClient

from api.authentication import login
from api.projects import list_projects
from api.folders import (
    list_root_folders,
    browse_folder
)
from api.search import search_objects
from api.object_details import get_object_details
from api.reports import get_report_definition
from api.changesets import create_changeset

from utils.menu import Menu
from utils.object_types import ObjectType


# --------------------------------------------------
# Pretty-print Object Details
# --------------------------------------------------

def print_object_details(details):

    print("\n")
    print("=" * 60)
    print("Object Details")
    print("=" * 60)

    print(f"Name         : {details.get('name', '-')}")
    print(f"ID           : {details.get('id', '-')}")

    object_type = details.get("type")

    if object_type in [item.value for item in ObjectType]:
        object_type = ObjectType(object_type).name.title()

    print(f"Type         : {object_type}")

    print(f"Description  : {details.get('description', '-')}")

    owner = details.get("owner", {})

    print(f"Owner        : {owner.get('name', '-')}")
    print(f"Created      : {details.get('dateCreated', '-')}")
    print(f"Modified     : {details.get('dateModified', '-')}")
    print(f"Version      : {details.get('version', '-')}")

    print("=" * 60)


def run():

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
    # Create Modeling Changeset
    # --------------------------------------------------

    print("\nCreating Modeling Changeset...")
    print("-" * 60)

    changeset = create_changeset(
        client,
        schema_edit=False
    )

    client.set_changeset(
        changeset["id"]
    )

    print("\nChangeset Created")
    print("-" * 60)
    print(f"ID : {changeset['id']}")

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

            contents = browse_folder(
                client,
                folder["id"]
            )

            for obj in contents:
                print(f"  {obj['name']}")

    else:

        print("\nBrowsing Folder")
        print("-" * 60)

        print(selected_folder["name"])

        contents = browse_folder(
            client,
            selected_folder["id"]
        )

        print("\nContents")
        print("-" * 60)

        if not contents:

            print("Folder is empty.")

        else:

            for index, obj in enumerate(
                contents,
                start=1
            ):

                print(
                    f"{index}. "
                    f"{obj['name']} "
                    f"({obj['id']})"
                )
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

        print(f"\n{index}. {obj.get('name', '-')}")

        print(f"   ID          : {obj.get('id', '-')}")

        obj_type = obj.get("type")

        if obj_type in [item.value for item in ObjectType]:
            obj_type_name = ObjectType(obj_type).name.title()
        else:
            obj_type_name = obj_type

        print(f"   Type        : {obj_type_name}")

        if "subtype" in obj:
            print(f"   Subtype     : {obj['subtype']}")

        if "reportType" in obj:
            print(f"   Report Type : {obj['reportType']}")

        if "owner" in obj:
            owner = obj.get("owner", {})
            print(f"   Owner       : {owner.get('name', '-')}")

        if "dateModified" in obj:
            print(f"   Modified    : {obj['dateModified']}")

    object_choice = int(
        input("\nSelect Object Number : ")
    )

    selected_object = search_results[
        object_choice - 1
    ]

    # --------------------------------------------------
    # DEBUG
    # --------------------------------------------------

    print("\nSelected Object")
    print("-" * 60)

    print(
        json.dumps(
            selected_object,
            indent=4
        )
    )

    # --------------------------------------------------
    # Report Definition or Object Details
    # --------------------------------------------------

    if selected_object["type"] == ObjectType.REPORT.value:

        report = get_report_definition(
            client,
            selected_object["id"]
        )

        print("\nReturned Report Definition")
        print("-" * 60)

        print(
            json.dumps(
                report,
                indent=4
            )
        )

    else:

        details = get_object_details(
            client,
            selected_object["id"],
            selected_object["type"]
        )

        print_object_details(details)