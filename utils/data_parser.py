"""
Data Parser

Extracts the data section returned from a MicroStrategy
Report Instance REST API response.

Current Scope
-------------
- Row header indexes
- Column header indexes
- Raw metric values
- Formatted metric values

Future Scope
------------
- Build logical rows
- Handle totals
- Handle subtotals
- Handle page-by
- Produce report-ready records
"""


class DataParser:
    """
    Parser for report data.
    """

    @staticmethod
    def parse(report_json):
        """
        Parse the report data section.

        Parameters
        ----------
        report_json : dict

        Returns
        -------
        dict
        """

        data = report_json.get(
            "data",
            {}
        )

        headers = data.get(
            "headers",
            {}
        )

        metric_values = data.get(
            "metricValues",
            {}
        )

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