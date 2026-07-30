"""
Grid Parser

Parses the report template (definition.grid).

This module is responsible ONLY for extracting the report
layout information.

It does NOT parse report data.

It does NOT parse metric values.

It does NOT parse row values.

It only extracts:

- Row Attributes
- Column Attributes
- Metrics
- Page By Attributes
"""


class GridParser:
    """
    Parses definition.grid section from a report response.
    """

    @staticmethod
    def parse(grid):
        """
        Parse the report grid definition.

        Parameters
        ----------
        grid : dict
            response["definition"]["grid"]

        Returns
        -------
        dict
        """

        return {

            "row_attributes":
                GridParser._parse_rows(grid),

            "column_attributes":
                GridParser._parse_columns(grid),

            "metrics":
                GridParser._parse_metrics(grid),

            "page_by":
                GridParser._parse_page_by(grid)
        }

    # ---------------------------------------------------------
    # Row Attributes
    # ---------------------------------------------------------

    @staticmethod
    def _parse_rows(grid):

        rows = []

        for attribute in grid.get("rows", []):

            rows.append({

                "id":
                    attribute.get("id"),

                "name":
                    attribute.get("name"),

                "type":
                    attribute.get("type"),

                "forms":
                    attribute.get("forms", []),

                "elements":
                    attribute.get("elements", [])
            })

        return rows

    # ---------------------------------------------------------
    # Column Attributes
    # ---------------------------------------------------------

    @staticmethod
    def _parse_columns(grid):

        columns = []

        for column in grid.get("columns", []):

            columns.append({

                "id":
                    column.get("id"),

                "name":
                    column.get("name"),

                "type":
                    column.get("type"),

                "elements":
                    column.get("elements", [])
            })

        return columns

    # ---------------------------------------------------------
    # Metrics
    # ---------------------------------------------------------

    @staticmethod
    def _parse_metrics(grid):

        metrics = []

        for column in grid.get("columns", []):

            if column.get("type") != "templateMetrics":
                continue

            for metric in column.get("elements", []):

                metrics.append({

                    "id":
                        metric.get("id"),

                    "name":
                        metric.get("name"),

                    "dataType":
                        metric.get("dataType"),

                    "format":
                        metric.get("numberFormatting", {})
                })

        return metrics

    # ---------------------------------------------------------
    # Page By
    # ---------------------------------------------------------

    @staticmethod
    def _parse_page_by(grid):

        page_by = []

        for attribute in grid.get("pageBy", []):

            page_by.append({

                "id":
                    attribute.get("id"),

                "name":
                    attribute.get("name"),

                "type":
                    attribute.get("type"),

                "forms":
                    attribute.get("forms", []),

                "elements":
                    attribute.get("elements", [])
            })

        return page_by