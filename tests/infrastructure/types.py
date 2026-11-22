from typing import Protocol

from se.application.presentation import HasAdd, HasList
from se.domain import Term


class RepoProto(HasAdd[Term], HasList[Term], Protocol): ...
