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
from utils.header_parser import HeaderParser
from utils.metric_parser import MetricParser
from utils.data_parser import DataParser
from utils.data_parser import DataParser


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

        # --------------------------------------------------
        # Parse Report Headers
        # --------------------------------------------------

        headers = HeaderParser.parse(
            data["definition"]["grid"]
        )

        # --------------------------------------------------
        # Parse Report Metrics
        # --------------------------------------------------

        metrics = MetricParser.parse(
            data["definition"]["grid"]
        )

        # --------------------------------------------------
        # Parse Report Data
        # --------------------------------------------------

        rows = DataParser.parse(
            data
        )

        # --------------------------------------------------
        # Parse Report Data
        # --------------------------------------------------

        rows = DataParser.parse(
            data
        )

        # --------------------------------------------------
        # Temporary Verification
        # --------------------------------------------------
        #
        # GridParser, HeaderParser, MetricParser and
        # DataParser are intentionally executed but not
        # displayed. Future commits will use these parsed
        # objects to build a production-quality report
        # output.
        #
        # print(grid)
        # print(headers)
        # print(metrics)
        # print(rows)

        print("\n===== DATA SECTION =====")
        print(
            json.dumps(
                data.get("data", {}),
                indent=4
            )
        )

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