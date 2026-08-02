"""
Row Builder

Builds report rows from the MicroStrategy report response.

Current Scope
-------------
- Extract row header references.
- Extract column header references.
- Extract raw metric values.
- Extract formatted metric values.

Future Scope
------------
- Resolve header indexes to actual attribute values.
- Combine attributes with metrics.
- Build one dictionary per report row.
- Support totals and subtotals.
- Support page-by reports.
"""


class RowBuilder:
    """
    Builds report rows.
    """

    @staticmethod
    def build(report_json):
        """
        Build intermediate row structure.

        Parameters
        ----------
        report_json : dict

        Returns
        -------
        dict
        """

        headers = report_json.get("headers", {})

        metric_values = report_json.get("metricValues", {})

        return {

            "row_headers": headers.get(
                "rows",
                []
            ),

            "column_headers": headers.get(
                "columns",
                []
            ),

            "raw_values": metric_values.get(
                "raw",
                []
            ),

            "formatted_values": metric_values.get(
                "formatted",
                []
            )

        }