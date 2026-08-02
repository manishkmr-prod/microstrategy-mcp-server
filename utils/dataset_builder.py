"""
Dataset Builder

Builds the final report dataset by combining:

1. Resolved row attributes
2. Metric names
3. Metric values

Current Scope
-------------
- Tabular reports
- Metrics on columns
- Detail rows
- Summary rows

Future Scope
------------
- Cross-tab reports
- Page-by datasets
- Multiple metric axes
- Formatting options
"""


class DatasetBuilder:
    """
    Builds the final dataset from the resolved report structure.
    """

    @staticmethod
    def build(resolved_grid):
        """
        Build a business dataset.

        Parameters
        ----------
        resolved_grid : dict

        Returns
        -------
        list
            List of dictionaries.
        """

        rows = resolved_grid.get(
            "rows",
            []
        )

        metrics = resolved_grid.get(
            "metrics",
            []
        )

        values = resolved_grid.get(
            "raw_values",
            []
        )

        dataset = []

        for row_index, row in enumerate(rows):

            record = dict(row)

            if row_index < len(values):

                metric_row = values[row_index]

                for metric_index, metric_name in enumerate(metrics):

                    if metric_index < len(metric_row):

                        record[metric_name] = metric_row[metric_index]

                    else:

                        record[metric_name] = None

            else:

                for metric_name in metrics:

                    record[metric_name] = None

            dataset.append(record)

        return dataset