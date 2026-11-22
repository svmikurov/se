"""Domain layer."""

__all__ = [
    # === Interfaces ===
    #  - object fields
    'HasIdentifier',
    'HasDefinition',
    'HasExplanation',
    # - object-values
    'PresentationCardProto',
    # - entities
    'TermProto',
    # - services
    'PresentationDomainProto',
    #
    # === Implementation ===
    #  - value-objects
    'PresentationCard',
    # - entities
    'Term',
    # - services
    'PresentationDomain',
    #
    # === Exceptions ===
    'NoItemsForExercise',
]

from .exceptions import (
    NoItemsForExercise,
)
from .models import (
    PresentationDomain,
    Term,
)
from .protocols import (
    HasDefinition,
    HasExplanation,
    HasIdentifier,
    PresentationCardProto,
    PresentationDomainProto,
    TermProto,
)
from .values import (
    PresentationCard,
)
