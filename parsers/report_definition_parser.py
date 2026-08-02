"""
Parser for MicroStrategy Report Definition.

This parser extracts only the report template metadata.
It does NOT parse report data or metric values.

Commit 1 Scope:
- Report Name
- Row Attributes
- Column Attributes
- Metrics
- Page By
- Crosstab Information
- Metric Position
"""


def parse_report_definition(report_json):
    """
    Extract report definition metadata.

    Parameters
    ----------
    report_json : dict
        Raw response returned from the Report Instance REST API.

    Returns
    -------
    dict
        Parsed report definition.
    """

    definition = report_json.get("definition", {})
    grid = definition.get("grid", {})

    return {
        "report_name": report_json.get("name"),

        "row_attributes": grid.get("rows", []),

        "column_attributes": grid.get("columns", []),

        "metrics": (
            grid.get("columns", [{}])[0].get("elements", [])
            if grid.get("columns")
            else []
        ),

        "page_by": grid.get("pageBy", []),

        "cross_tab": grid.get("crossTab", False),

        "metric_position": grid.get("metricsPosition", {})
    }