import random
import string
import time

import requests

from urls import Urls


def unique_email():
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"auto_{int(time.time() * 1000)}_{suffix}@test.ru"


def unique_name():
    return f"User_{int(time.time() * 1000)}_{random.randint(100, 999)}"


def unique_password():
    return f"Pass_{int(time.time())}_{random.randint(1000, 9999)}"


def _api_url(path):
    return f"{Urls.BASE_URL}{path}"


def register_user(email=None, password=None, name=None):
    payload = {
        "email": email or unique_email(),
        "password": password or unique_password(),
        "name": name or unique_name(),
    }
    response = requests.post(_api_url(Urls.API_REGISTER), json=payload, timeout=30)
    response.raise_for_status()
    body = response.json()
    assert body.get("success") is True, body
    return {
        "email": payload["email"],
        "password": payload["password"],
        "name": payload["name"],
        "access_token": body["accessToken"],
        "refresh_token": body["refreshToken"],
    }


def delete_user(access_token):
    response = requests.delete(
        _api_url(Urls.API_USER),
        headers={"Authorization": access_token},
        timeout=30,
    )
    if response.status_code not in (200, 202):
        response.raise_for_status()
