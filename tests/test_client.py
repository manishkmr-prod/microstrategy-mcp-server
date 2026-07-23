from mstr_client import MSTRClient

client = MSTRClient()

print("Base URL :", client.base_url)
print("SSL      :", client.verify_ssl)
print("Session  :", client.session)