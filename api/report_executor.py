"""
Report Executor

Responsible for executing a report from start to finish.
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
from utils.element_resolver import ElementResolver
from utils.dataset_builder import DatasetBuilder
from utils.report_renderer import ReportRenderer


def execute_report(client, report_id):

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
        # Prompt Handling
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

        response = get_report_data(
            client,
            report_id,
            instance["id"]
        )

        # --------------------------------------------------
        # Parse Report Metadata
        # --------------------------------------------------

        grid = GridParser.parse(
            response["definition"]["grid"]
        )

        headers = HeaderParser.parse(
            response
        )

        metrics = MetricParser.parse(
            response["definition"]["grid"]
        )

        # --------------------------------------------------
        # Resolve Grid
        # --------------------------------------------------

        resolved_grid = ElementResolver.resolve(
            response["definition"]["grid"],
            response
        )

        # --------------------------------------------------
        # Build Dataset
        # --------------------------------------------------

        dataset = DatasetBuilder.build(
            resolved_grid
        )

        # --------------------------------------------------
        # Render Report
        # --------------------------------------------------

        ReportRenderer.render(
            response.get("name", "Report"),
            dataset
        )

        # --------------------------------------------------
        # Build Report Model
        # --------------------------------------------------

        report = {
            "grid": grid,
            "headers": headers,
            "metrics": metrics,
            "dataset": dataset
        }

        return report

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