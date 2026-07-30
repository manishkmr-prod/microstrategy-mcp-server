"""
Prompt Engine

Responsible for collecting answers for MicroStrategy prompts.

This class is intentionally independent from REST API calls.
It only transforms prompt definitions into an answer payload
that can be submitted back to MicroStrategy.
"""


class PromptEngine:

    @staticmethod
    def collect_answers(prompts):
        """
        Collect answers for all prompts.

        Parameters
        ----------
        prompts : list
            Prompt definitions returned by MicroStrategy.

        Returns
        -------
        dict
            Payload ready for
            PUT /reports/{reportId}/instances/{instanceId}/prompts/answers
        """

        answered_prompts = []

        for prompt in prompts:

            prompt_type = prompt.get("type")

            if prompt_type == "ELEMENTS":

                answered_prompt = PromptEngine._answer_elements_prompt(
                    prompt
                )

                answered_prompts.append(answered_prompt)

            else:

                print()
                print(
                    f"Skipping unsupported prompt type: "
                    f"{prompt_type}"
                )

        return {
            "prompts": answered_prompts
        }

    # --------------------------------------------------
    # ELEMENTS Prompt
    # --------------------------------------------------

    @staticmethod
    def _answer_elements_prompt(prompt):

        print()
        print("=" * 60)
        print(prompt.get("title", "Prompt"))
        print("=" * 60)

        answers = prompt.get("answers", [])

        for index, answer in enumerate(
            answers,
            start=1
        ):

            print(
                f"{index}. "
                f"{answer.get('name')}"
            )

        while True:

            try:

                choice = int(
                    input("\nSelect option : ")
                )

                if 1 <= choice <= len(answers):
                    break

                print(
                    "Invalid choice. Try again."
                )

            except ValueError:

                print(
                    "Please enter a number."
                )

        selected_answer = answers[
            choice - 1
        ]

        return {
        "name": prompt.get("name"),
        "type": prompt.get("type"),
        "required": prompt.get("required"),
        "closed": prompt.get("closed"),
        "source": prompt.get("source"),
        "answers": [
            selected_answer
        ]
    }