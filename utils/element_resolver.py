"""
Element Resolver

Converts MicroStrategy row/column indexes into
human-readable attribute and metric values.
"""


class ElementResolver:
    """
    Resolves report indexes into business-readable values.
    """

    @staticmethod
    def resolve(grid_definition, report_data):
        """
        Build a resolved grid.

        Parameters
        ----------
        grid_definition : dict

        report_data : dict

        Returns
        -------
        dict
        """

        rows_definition = grid_definition.get("rows", [])
        columns_definition = grid_definition.get("columns", [])

        data = report_data.get("data", {})

        headers = data.get("headers", {})
        metric_values = data.get("metricValues", {})

        resolved_rows = []

        # ---------------------------------------------
        # Resolve row headers
        # ---------------------------------------------

        for row_indexes in headers.get("rows", []):

            row = {
                "row_type": "detail"
            }

            for attribute_index, element_index in enumerate(row_indexes):

                if attribute_index >= len(rows_definition):
                    continue

                attribute = rows_definition[attribute_index]

                attribute_name = attribute.get("name")

                elements = attribute.get("elements", [])

                if element_index < len(elements):

                    element = elements[element_index]

                    value = element.get(
                        "formValues",
                        [None]
                    )[0]

                    row[attribute_name] = value

                    if element.get("subtotal", False):
                        row["row_type"] = "summary"

                else:

                    row[attribute_name] = None

            resolved_rows.append(row)

        # ---------------------------------------------
        # Resolve metric names
        # ---------------------------------------------

        metric_names = []

        if columns_definition:

            for metric in columns_definition[0].get(
                "elements",
                []
            ):

                metric_names.append(
                    metric.get("name")
                )

        return {

            "rows": resolved_rows,

            "metrics": metric_names,

            "raw_values": metric_values.get(
                "raw",
                []
            ),

            "formatted_values": metric_values.get(
                "formatted",
                []
            )

        }