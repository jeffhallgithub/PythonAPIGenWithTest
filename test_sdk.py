#!/usr/bin/env python3

from EligibilityApiClient import EligibilityApiClient
import datetime
import pytest

def test_verify_eligibility_valid_request():
    client = EligibilityApiClient()
    is_eligible, message = client.isEligible(
        "Super Awesome Insurance",
        "12345",
        "John Doe",
        datetime.date(1990, 1, 1)
    )
    assert is_eligible == True
    assert message == "string"

def test_verify_eligibility_invalid_request_wrong_type():
    client = EligibilityApiClient()
    is_eligible, message = client.isEligible(
        123, # Try and send the request with an int here instead of a string for carrier name, results in 400 on the server
        "12345",
        "John Doe",
        datetime.date(1990, 1, 1)
    )
    assert is_eligible == False
    assert message == "Invalid Request"

def test_verify_eligibility_invalid_request_empty_values():
    client = EligibilityApiClient()
    is_eligible, message = client.isEligible(
        None, # Try and send the request with empty values, should fail and result in a 400
        None,
        None,
        datetime.date(1990, 1, 1),
    )
    assert is_eligible == False
    assert message == "Invalid Request"

def test_verify_eligibility_invalid_request_missing_values():
    with pytest.raises(TypeError):
        client = EligibilityApiClient()
        client.isEligible(
            "Super Awesome Insurance",
            "12345",
            # "John Doe", # Try and call without a full name, should throw a TypeError
            datetime.date(1990, 1, 1)
        )

def test_verify_eligibility_invalid_request_malformed_datetime():
    with pytest.raises(AttributeError):
        client = EligibilityApiClient()
        client.isEligible(
            "Super Awesome Insurance",
            "12345",
            "John Doe",
            "1990-01-01" #Try and call with a string instead of a datetime, should throw an AttributeError
        )