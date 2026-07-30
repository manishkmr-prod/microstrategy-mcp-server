"""
Report Executor

Responsible for executing a report from start to finish.

Workflow

1. Create report instance
2. Retrieve prompt definitions
3. If prompts exist:
      - Collect answers
      - Submit answers
4. Retrieve report data
5. Delete report instance
"""

import json

from api.report_instances import (
    create_report_instance,
    delete_report_instance
)

from api.report_prompts import (
    get_report_prompts
)

from api.prompt_answers import (
    answer_report_prompts
)

from api.report_data import (
    get_report_data
)

from utils.prompt_engine import (
    PromptEngine
)

from utils.printer import Printer
from utils.grid_parser import GridParser


def execute_report(client, report_id):
    """
    Execute a report.

    Parameters
    ----------
    client : MSTRClient

    report_id : str

    Returns
    -------
    dict
    """

    instance = None

    try:

        # --------------------------------------------------
        # Create Report Instance
        # --------------------------------------------------

        print("\nCreating Report Instance...")
        Printer.separator()

        instance = create_report_instance(
            client,
            report_id
        )

        Printer.report_instance(instance)

        # --------------------------------------------------
        # Retrieve Prompt Definitions
        # --------------------------------------------------

        print("\nRetrieving Prompt Definitions...")
        Printer.separator()

        prompts = get_report_prompts(
            client,
            report_id,
            instance["id"]
        )

        # --------------------------------------------------
        # Handle Prompted Reports
        # --------------------------------------------------

        if prompts:

            print(f"\n{len(prompts)} Prompt(s) Found.")

            answer_payload = PromptEngine.collect_answers(
                prompts
            )

            print("\nGenerated Prompt Payload")
            Printer.separator()

            print(
                json.dumps(
                    answer_payload,
                    indent=4
                )
            )

            print("\nSubmitting Prompt Answers...")
            Printer.separator()

            answer_report_prompts(
                client,
                report_id,
                instance["id"],
                answer_payload
            )

            print("\nPrompt Answers Submitted Successfully.")

        else:

            print("\nNo prompts found for this report.")

        # --------------------------------------------------
        # Retrieve Report Data
        # --------------------------------------------------

        print("\nRetrieving Report Data...")
        Printer.separator()

        data = get_report_data(
            client,
            report_id,
            instance["id"]
        )

        # --------------------------------------------------
        # Parse Grid Definition
        # --------------------------------------------------

        grid = GridParser.parse(
            data["definition"]["grid"]
        )

        # Temporary verification during development.
        # Will be replaced by Printer.grid_information()
        # in the next commit.

        # print("\nGrid Information")
        # Printer.separator()
        # print(grid)

        return data

    finally:

        # --------------------------------------------------
        # Delete Report Instance
        # --------------------------------------------------

        if instance is not None:

            print("\nDeleting Report Instance...")
            Printer.separator()

            delete_report_instance(
                client,
                report_id,
                instance["id"]
            )

            print("\nReport Instance Deleted Successfully.")