from utils.object_types import ObjectType


class Menu:
    """
    Handles all menu display and user input.
    """

    OBJECT_MENU = {
        1: ObjectType.REPORT,
        2: ObjectType.METRIC,
        3: ObjectType.ATTRIBUTE,
        4: ObjectType.FACT,
        5: ObjectType.FILTER,
        6: ObjectType.FOLDER,
        7: ObjectType.DOCUMENT,
        8: ObjectType.SEARCH_ALL
    }

    @staticmethod
    def select_project(projects):

        print("\nAvailable Projects")
        print("-" * 60)

        for index, project in enumerate(projects, start=1):
            print(f"{index}. {project['name']}")

        while True:

            try:

                choice = int(input("\nSelect Project Number : "))

                if 1 <= choice <= len(projects):
                    return projects[choice - 1]

                print("Invalid selection.")

            except ValueError:
                print("Please enter a valid number.")

    @staticmethod
    def select_root_folder(folders):

        print("\nAvailable Root Folders")
        print("-" * 60)

        print("\nA. Browse ALL Root Folders\n")

        print("-------------------- OR --------------------\n")

        for index, folder in enumerate(folders, start=1):
            print(f"{index}. {folder['name']}")

        while True:

            choice = input("\nSelect Folder : ").strip().upper()

            if choice == "A":
                return "ALL"

            try:

                choice = int(choice)

                if 1 <= choice <= len(folders):
                    return folders[choice - 1]

                print("Invalid selection.")

            except ValueError:
                print("Please enter A or a valid number.")

    @classmethod
    def select_object_type(cls):

        print("\nObject Types")
        print("-" * 60)

        print("1. Reports")
        print("2. Metrics")
        print("3. Attributes")
        print("4. Facts")
        print("5. Filters")
        print("6. Folders")
        print("7. Documents")
        print("8. Search Everything")

        while True:

            try:

                choice = int(input("\nSelect Object Type : "))

                if choice in cls.OBJECT_MENU:
                    return cls.OBJECT_MENU[choice]

                print("Invalid selection.")

            except ValueError:
                print("Please enter a valid number.")