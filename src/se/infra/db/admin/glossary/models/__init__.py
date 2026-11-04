"""Glossary application models."""

__all__ = [
    # Term
    'Definition',
    'Explanation',
    'Term',
    # Source
    'Author',
    'Source',
    'TermLink',
]

from .source import Author, Source
from .term import Definition, Explanation, Term, TermLink
