import os
import json
import requests
from common.constants import ANONYMIZER_BASE_URL as DEFAULT_BASE_URL

# Read base URL from environment variable or fallback to default
ANONYMIZER_BASE_URL = os.environ.get("ANONYMIZER_BASE_URL", DEFAULT_BASE_URL)

DEFAULT_HEADERS = {"Content-Type": "application/json"}
MULTIPART_HEADERS = {"Content-Type": "multipart/form-data"}

def call_anonymize_endpoint(request_body):
    response = requests.post(
        f"{ANONYMIZER_BASE_URL}/anonymize",
        json=request_body
    )
    return response.status_code, response.json()

def anonymize(data):
    """Send data to /anonymize endpoint."""
    response = requests.post(
        f"{ANONYMIZER_BASE_URL}/anonymize", data=data, headers=DEFAULT_HEADERS
    )
    return response.status_code, response.content


def anonymizers():
    """Get list of available anonymizers."""
    response = requests.get(
        f"{ANONYMIZER_BASE_URL}/anonymizers", headers=DEFAULT_HEADERS
    )
    return response.status_code, response.content


def deanonymize(data):
    """Send data to /deanonymize endpoint."""
    response = requests.post(
        f"{ANONYMIZER_BASE_URL}/deanonymize", data=data, headers=DEFAULT_HEADERS
    )
    return response.status_code, response.content


def __get_redact_payload(color_fill):
    payload = {}
    if color_fill:
        payload = {"data": json.dumps({"color_fill": color_fill})}
    return payload


def __get_multipart_form_data(file):
    multipart_form_data = {}
    if file:
        multipart_form_data = {
            "image": (file.name, file, "multipart/form-data"),
        }
    return multipart_form_data

