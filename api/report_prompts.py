from mstr_client import MSTRClient


def get_report_prompts(
    client: MSTRClient,
    report_id: str,
    instance_id: str
):
    """
    Retrieve prompt definitions for a report instance.
    """

    endpoint = (
        f"/reports/{report_id}"
        f"/instances/{instance_id}"
        "/prompts"
    )

    print("\nCalling REST API")
    print("-" * 60)
    print(f"Endpoint : {endpoint}")

    response = client.get(endpoint)

    print(f"\nHTTP Status : {response.status_code}")

    if response.status_code != 200:
        raise Exception(
            f"Unable to retrieve prompts ({response.status_code})"
        )

    return response.json()