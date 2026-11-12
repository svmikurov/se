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
    # Scope
    'Scope',
    'DefinitionScope',
    # Tag
    'Tag',
    'DefinitionTag',
]

from .scope import DefinitionScope, Scope
from .source import Author, Source
from .tag import DefinitionTag, Tag
from .term import Definition, Explanation, Term, TermLink
