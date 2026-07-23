from config import settings


def login(client):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "username": settings.MSTR_USERNAME,
        "password": settings.MSTR_PASSWORD,
        "loginMode": 1
    }

    response = client.post(
        "/auth/login",
        headers=headers,
        json=payload
    )

    if response.status_code != 204:
        raise Exception(
            f"Login failed ({response.status_code})\n{response.text}"
        )

    token = response.headers.get("X-MSTR-AuthToken")

    if not token:
        raise Exception("Authentication token not returned.")

    client.set_auth_token(token)

    return token