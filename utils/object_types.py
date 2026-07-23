from enum import Enum


class ObjectType(Enum):
    """
    MicroStrategy Object Types
    """

    REPORT = 3

    METRIC = 4

    FILTER = 6

    TEMPLATE = 7

    FOLDER = 8

    PROMPT = 10

    ATTRIBUTE = 12

    FACT = 13

    DOCUMENT = 55

    SEARCH_ALL = None