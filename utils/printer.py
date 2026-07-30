"""
Console output helpers.

All user-facing printing should go through this class so the
workflow remains focused on orchestration.
"""

from utils.object_types import ObjectType


class Printer:

    # --------------------------------------------------
    # Generic
    # --------------------------------------------------

    @staticmethod
    def separator():
        print("-" * 60)

    @staticmethod
    def header(title):
        print(f"\n{title}")
        Printer.separator()

    # --------------------------------------------------
    # Login
    # --------------------------------------------------

    @staticmethod
    def connecting():
        print("Connecting to MicroStrategy...")

    @staticmethod
    def login_success():
        print("Login Successful\n")

    # --------------------------------------------------
    # Project
    # --------------------------------------------------

    @staticmethod
    def selected_project(project):

        Printer.header("Selected Project")

        print(project["name"])

    # --------------------------------------------------
    # Changeset
    # --------------------------------------------------

    @staticmethod
    def creating_changeset():

        Printer.header("Creating Modeling Changeset...")

    @staticmethod
    def changeset(changeset):

        Printer.header("Changeset Created")

        print(f"ID : {changeset['id']}")

    # --------------------------------------------------
    # Folder Browsing
    # --------------------------------------------------

    @staticmethod
    def browsing_all_root_folders():

        Printer.header("Browsing ALL Root Folders")

    @staticmethod
    def browsing_folder(folder_name):

        Printer.header("Browsing Folder")

        print(folder_name)

    @staticmethod
    def folder_contents(contents):

        Printer.header("Contents")

        if not contents:

            print("Folder is empty.")
            return

        for index, obj in enumerate(contents, start=1):

            print(
                f"{index}. "
                f"{obj['name']} "
                f"({obj['id']})"
            )

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    @staticmethod
    def search_title():

        Printer.header("Search Objects")

    @staticmethod
    def search_results(results):

        Printer.header("Search Results")

        if not results:

            print("No objects found.")
            return

        for index, obj in enumerate(results, start=1):

            print(f"\n{index}. {obj.get('name', '-')}")

            print(f"   ID          : {obj.get('id', '-')}")

            object_type = obj.get("type")

            if object_type in [item.value for item in ObjectType]:
                object_type_name = ObjectType(object_type).name.title()
            else:
                object_type_name = object_type

            print(f"   Type        : {object_type_name}")

            if "subtype" in obj:
                print(f"   Subtype     : {obj['subtype']}")

            if "reportType" in obj:
                print(f"   Report Type : {obj['reportType']}")

            if "owner" in obj:
                owner = obj.get("owner", {})
                print(f"   Owner       : {owner.get('name', '-')}")

            if "dateModified" in obj:
                print(f"   Modified    : {obj['dateModified']}")

    @staticmethod
    def selected_object(obj):

        Printer.header("Selected Object")

        print(f"Name : {obj.get('name')}")
        print(f"ID   : {obj.get('id')}")

    # --------------------------------------------------
    # Object Details
    # --------------------------------------------------

    @staticmethod
    def object_details(details):

        print()

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

    # --------------------------------------------------
    # Report Definition
    # --------------------------------------------------

    @staticmethod
    def report_definition(report):

        info = report.get("information", {})

        print()
        print("=" * 60)
        print("Report Definition")
        print("=" * 60)

        print("Name")
        print("-" * 20)
        print(info.get("name", "-"))

        print()

        print("Description")
        print("-" * 20)
        print(info.get("description", "-"))

        # ---------------- Rows ----------------

        rows = (
            report.get("grid", {})
            .get("viewTemplate", {})
            .get("rows", {})
            .get("units", [])
        )

        print()
        print("Rows")
        print("-" * 20)

        if rows:

            for row in rows:
                print(f"• {row.get('name')}")

        else:
            print("-")

        # ---------------- Columns ----------------

        columns = (
            report.get("grid", {})
            .get("viewTemplate", {})
            .get("columns", {})
            .get("units", [])
        )

        print()
        print("Columns")
        print("-" * 20)

        metrics = []

        for column in columns:

            if column.get("type") == "attribute":

                print(f"• {column.get('name')}")

            elif column.get("type") == "metrics":

                for metric in column.get("elements", []):

                    metrics.append(metric.get("name"))

        # ---------------- Metrics ----------------

        print()
        print("Metrics")
        print("-" * 20)

        if metrics:

            for metric in metrics:
                print(f"• {metric}")

        else:
            print("-")

        # ---------------- Filters ----------------

        print()
        print("Filters")
        print("-" * 20)

        filter_tree = (
            report.get("dataSource", {})
            .get("filter", {})
            .get("tree", {})
        )

        prompt_count = 0

        if "children" in filter_tree:

            for child in filter_tree["children"]:

                predicate = child.get("predicateTree", {})

                filter_object = predicate.get("filter", {})

                if filter_object:

                    print(f"• {filter_object.get('name')}")

                    if filter_object.get("isEmbedded"):
                        prompt_count += 1

        elif "predicateTree" in filter_tree:

            filter_object = (
                filter_tree["predicateTree"]
                .get("filter", {})
            )

            if filter_object:

                print(f"• {filter_object.get('name')}")

                if filter_object.get("isEmbedded"):
                    prompt_count += 1

        else:

            print("-")

        # ---------------- Prompts ----------------

        print()
        print("Prompts")
        print("-" * 20)

        print(f"{prompt_count} Prompt Filter(s)")

        print()
        print("=" * 60)