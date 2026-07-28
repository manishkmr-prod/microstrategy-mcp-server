from mstr_client import MSTRClient
from api.authentication import login
from api.reports import get_report_definition

REPORT_ID = "FCADA26250481A63BA92FB8DD18497C8"

client = MSTRClient()

login(client)

client.set_project("205BABE083484404399FBBA37BAA874A")

report = get_report_definition(
    client,
    REPORT_ID
)

print(report)