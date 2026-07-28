"""
Report APIs

Reusable SDK functions for working with
MicroStrategy Modeling Reports.
"""


def get_report_definition(
    client,
    report_id,
    fields=None
):
    """
    Retrieve the definition of a report using the
    Modeling API.

    Parameters
    ----------
    client : MSTRClient

    report_id : str

    fields : str, optional
        Comma-separated list of fields to return.

    Returns
    -------
    dict
    """

    endpoint = f"/model/reports/{report_id}"

    params = {}

    if fields:
        params["fields"] = fields

    print("\nCalling REST API")
    print("-" * 60)
    print(f"Endpoint : {endpoint}")

    response = client.get(
        endpoint,
        params=params,
        headers={
            "Accept": "application/json"
        }
    )

    print("\nHTTP Status :", response.status_code)

    if response.status_code != 200:

        print("\nResponse")
        print(response.text)

        raise Exception(
            f"Unable to retrieve report definition ({response.status_code})"
        )

    return response.json()