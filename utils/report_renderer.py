"""
Report Renderer

Responsible for presenting a report dataset.

Current Scope
-------------
- Console rendering
- Dynamic column widths
- Clean table formatting

Future Scope
------------
- CSV Export
- Excel Export
- Markdown Export
- HTML Export
"""


class ReportRenderer:
    """
    Renders report datasets.
    """

    @staticmethod
    def render(report_name, dataset):
        """
        Render dataset to console.

        Parameters
        ----------
        report_name : str

        dataset : list[dict]
        """

        print("\n")
        print("=" * 60)
        print(report_name)
        print("=" * 60)

        if not dataset:
            print("\nNo rows returned.")
            return

        columns = list(dataset[0].keys())

        # ------------------------------------------
        # Calculate column widths
        # ------------------------------------------

        widths = {}

        for column in columns:

            max_width = len(column)

            for row in dataset:

                value = str(row.get(column, ""))

                if len(value) > max_width:
                    max_width = len(value)

            widths[column] = max_width + 2

        # ------------------------------------------
        # Header
        # ------------------------------------------

        header = ""

        for column in columns:
            header += column.ljust(widths[column])

        print(header)
        print("-" * len(header))

        # ------------------------------------------
        # Rows
        # ------------------------------------------

        for row in dataset:

            line = ""

            for column in columns:

                value = str(row.get(column, ""))

                line += value.ljust(widths[column])

            print(line)

        print()