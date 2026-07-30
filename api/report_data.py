"""
Report Data API

Wrapper around:

GET /api/v2/reports/{reportId}/instances/{instanceId}

Retrieves the executed report data for a report instance.
"""


def get_report_data(
    client,
    report_id,
    instance_id
):
    """
    Retrieve report data for a report instance.

    Parameters
    ----------
    client : MSTRClient
        Authenticated MicroStrategy client.

    report_id : str
        Report object ID.

    instance_id : str
        Report instance ID.

    Returns
    -------
    dict
        JSON response containing the report data.
    """

    endpoint = (
        f"/v2/reports/"
        f"{report_id}"
        f"/instances/"
        f"{instance_id}"
    )

    response = client.get(endpoint)

    if response.status_code != 200:

        raise Exception(
            f"Unable to retrieve report data "
            f"({response.status_code})"
        )

    return response.json()