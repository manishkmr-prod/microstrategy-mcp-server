"""
Header Parser

Parses report headers returned by the Report Data API.

This parser is responsible for extracting only:

- Row headers
- Column headers
- Page-by headers

It does NOT parse:

- Metric values
- Data cells
- Formatting
"""


class HeaderParser:
    """
    Utility class for parsing report headers.
    """

    @staticmethod
    def parse(grid_definition):
        """
        Parse report headers.

        Parameters
        ----------
        grid_definition : dict
            The "definition.grid" object returned by the
            Report Data API.

        Returns
        -------
        dict
            Parsed report headers.
        """

        if not grid_definition:
            return {
                "rows": [],
                "columns": [],
                "page_by": []
            }

        return {
            "rows": HeaderParser._extract_names(
                grid_definition.get("rows", [])
            ),
            "columns": HeaderParser._extract_names(
                grid_definition.get("columns", [])
            ),
            "page_by": HeaderParser._extract_names(
                grid_definition.get("pageBy", [])
            )
        }

    @staticmethod
    def _extract_names(objects):
        """
        Extract object names from a list of grid objects.

        Parameters
        ----------
        objects : list

        Returns
        -------
        list[str]
        """

        names = []

        for obj in objects:

            name = obj.get("name")

            if name:
                names.append(name)

        return names