"""
Report Instance APIs

Creates and deletes report instances used for
report execution.
"""


def create_report_instance(
    client,
    report_id,
    execution_stage="execute_data"
):
    """
    Create a report instance.

    Parameters
    ----------
    client : MSTRClient

    report_id : str

    execution_stage : str
        execute_data
        resolve_prompts

    Returns
    -------
    dict
    """

    endpoint = f"/model/reports/{report_id}/instances"

    params = {
        "executionStage": execution_stage
    }

    print("\nCalling REST API")
    print("-" * 60)
    print(f"Endpoint : {endpoint}")

    response = client.post(
        endpoint,
        params=params,
        headers={
            "Accept": "application/json"
        }
    )

    print("\nHTTP Status :", response.status_code)

    if response.status_code != 201:

        print("\nResponse")
        print(response.text)

        raise Exception(
            f"Unable to create report instance ({response.status_code})"
        )

    return response.json()


def delete_report_instance(
    client,
    report_id,
    instance_id
):
    """
    Delete report instance.

    Parameters
    ----------
    client : MSTRClient

    report_id : str

    instance_id : str
    """

    endpoint = f"/model/reports/{report_id}/instances"

    print("\nCalling REST API")
    print("-" * 60)
    print(f"Endpoint : {endpoint}")

    response = client.delete(
        endpoint,
        headers={
            "Accept": "application/json",
            "X-MSTR-MS-Instance": instance_id
        }
    )

    print("\nHTTP Status :", response.status_code)

    if response.status_code != 204:

        print("\nResponse")
        print(response.text)

        raise Exception(
            f"Unable to delete report instance ({response.status_code})"
        )