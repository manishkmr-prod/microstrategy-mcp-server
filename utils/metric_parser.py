"""
Metric Parser

Extracts report metric metadata from the report grid definition.

This parser is responsible only for identifying the metrics
defined in the report template.

It does NOT parse:

- metric values
- report rows
- formatting
- headers
"""


class MetricParser:
    """
    Parser for report metrics.
    """

    @staticmethod
    def parse(grid):
        """
        Parse report metric definitions.

        Parameters
        ----------
        grid : dict
            Report grid definition.

        Returns
        -------
        list
            List of metric dictionaries.

            Example:

            [
                {
                    "id": "...",
                    "name": "Revenue"
                },
                {
                    "id": "...",
                    "name": "Profit"
                }
            ]
        """

        metrics = []

        columns = grid.get("columns", [])

        for column in columns:

            for element in column.get("elements", []):

                if element.get("type") == "metric":

                    metrics.append(
                        {
                            "id": element.get("id"),
                            "name": element.get("name")
                        }
                    )

        return metrics