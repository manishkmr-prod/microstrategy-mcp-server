"""
Data Parser

Extracts report data rows from a MicroStrategy report response.

This parser is responsible only for locating and returning
the raw report data.

Future commits will convert the raw data into fully formatted
records using report headers and metric metadata.
"""


class DataParser:
    """
    Parser for report data.
    """

    @staticmethod
    def parse(report_json):
        """
        Parse report data.

        Parameters
        ----------
        report_json : dict
            Complete report response.

        Returns
        -------
        list
            Raw report rows.
        """

        data = report_json.get("data", {})

        return data.get("root", {}).get("children", [])