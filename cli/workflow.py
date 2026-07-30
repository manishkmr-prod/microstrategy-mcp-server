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
from utils.printer import Printer


def run():

    client = MSTRClient()

    # --------------------------------------------------
    # Login
    # --------------------------------------------------

    Printer.connecting()

    login(client)

    Printer.login_success()

    # --------------------------------------------------
    # Project Selection
    # --------------------------------------------------

    projects = list_projects(client)

    selected_project = Menu.select_project(projects)

    client.set_project(selected_project["id"])

    Printer.selected_project(selected_project)

    # --------------------------------------------------
    # Create Modeling Changeset
    # --------------------------------------------------

    Printer.creating_changeset()

    changeset = create_changeset(
        client,
        schema_edit=False
    )

    client.set_changeset(
        changeset["id"]
    )

    Printer.changeset(changeset)

    # --------------------------------------------------
    # Root Folder Selection
    # --------------------------------------------------

    folders = list_root_folders(client)

    selected_folder = Menu.select_root_folder(folders)

    if selected_folder == "ALL":

        Printer.browsing_all_root_folders()

        for folder in folders:

            print(f"\n{folder['name']}")

            contents = browse_folder(
                client,
                folder["id"]
            )

            for obj in contents:
                print(f"  {obj['name']}")

    else:

        Printer.browsing_folder(
            selected_folder["name"]
        )

        contents = browse_folder(
            client,
            selected_folder["id"]
        )

        Printer.folder_contents(contents)

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    Printer.search_title()

    object_type = Menu.select_object_type()

    search_text = input("\nSearch Text : ")

    results = search_objects(
        client,
        search_text,
        object_type.value
    )

    search_results = results.get("result", [])

    Printer.search_results(search_results)

    if not search_results:
        return

    object_choice = int(
        input("\nSelect Object Number : ")
    )

    selected_object = search_results[
        object_choice - 1
    ]

    Printer.selected_object(selected_object)

    # --------------------------------------------------
    # Report Definition or Object Details
    # --------------------------------------------------

    if selected_object["type"] == ObjectType.REPORT.value:

        report = get_report_definition(
            client,
            selected_object["id"]
        )

        Printer.report_definition(report)

    else:

        details = get_object_details(
            client,
            selected_object["id"],
            selected_object["type"]
        )

        Printer.object_details(details)