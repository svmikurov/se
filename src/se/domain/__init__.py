"""Domain layer."""

__all__ = [
    # === Interfaces ===
    'HasID',
    'HasDefinitionID',
    'HasMeaningID',
    'HasDefinition',
    'HasMeaning',
    'HasQuestion',
    'HasAnswer',
    'Displayed',
    'Learnable',
    'PresentationProto',
    #
    # === Implementation ===
    'Card',
    'Term',
    'PresentationDomain',
    #
    # === Exceptions ===
    'NoItemsForExercise',
]

from .entities import (
    PresentationDomain,
    Term,
)
from .exceptions import (
    NoItemsForExercise,
)
from .protocols import (
    Displayed,
    HasAnswer,
    HasDefinition,
    HasDefinitionID,
    HasID,
    HasMeaning,
    HasMeaningID,
    HasQuestion,
    Learnable,
    PresentationProto,
)
from .values import (
    Card,
)
