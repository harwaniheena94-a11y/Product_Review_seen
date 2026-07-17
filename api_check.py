import requests

url = "https://app.solarcrm.com.au/backend/api/leads/import/excel/internal"

headers = {
    "X-Internal-Secret": "eb0bb2bca4b3bfcb9bd821d1a01170bf404c37eff941e51e55c62097a87789bf",
    "OrganizationId": "2"
}

files = {
    "files[]": ("first.xlsx", open("first.xlsx", "rb"))
}

response = requests.post(
    url,
    headers=headers,
    files=files
)

print(response.status_code)
print(response.text)