"""HTTP client interface."""

__all__ = [
    # Interface
    'HttpClientProto',
    # implementation
    'HasJson',
    'HttpClient',
]

from .impl import HttpClient
from .protocol import HasJson, HttpClientProto
