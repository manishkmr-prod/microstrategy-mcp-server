from utils.grid_parser import GridParser


def test_grid_parser(response):

    grid = response["definition"]["grid"]

    parsed = GridParser.parse(grid)

    print()

    print("Rows")
    print(parsed["row_attributes"])

    print()

    print("Columns")
    print(parsed["column_attributes"])

    print()

    print("Metrics")
    print(parsed["metrics"])

    print()

    print("Page By")
    print(parsed["page_by"])