import pytest

from logging_http_client_config import (
    enable_request_logging,
    enable_request_body_logging,
    enable_response_logging,
    enable_response_body_logging,
    is_request_logging_enabled,
    is_response_logging_enabled,
    is_request_body_logging_enabled,
    is_response_body_logging_enabled,
)


@pytest.mark.parametrize("switch", [True, False])
def test_enable_request_logging(switch):
    enable_request_logging(switch)
    assert is_request_logging_enabled() == switch


@pytest.mark.parametrize("switch", [True, False])
def test_enable_request_body_logging(switch):
    enable_request_body_logging(switch)
    assert is_request_body_logging_enabled() == switch


@pytest.mark.parametrize("switch", [True, False])
def test_enable_response_logging(switch):
    enable_response_logging(switch)
    assert is_response_logging_enabled() == switch


@pytest.mark.parametrize("switch", [True, False])
def test_enable_response_body_logging(switch):
    enable_response_body_logging(switch)
    assert is_response_body_logging_enabled() == switch
