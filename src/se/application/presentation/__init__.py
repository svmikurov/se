"""Presentation service."""

__all__ = [
    # Interface
    'PresentationUseCaseProto',
    'HasList',
    'HasAdd',
    'PresentationRepositoryProto',
]

from .protocols import (
    HasAdd,
    HasList,
    PresentationRepositoryProto,
    PresentationUseCaseProto,
)
