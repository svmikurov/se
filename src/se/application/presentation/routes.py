from dataclasses import asdict
from typing import Annotated, Any

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from . import PresentationUseCaseProto
from .di import Container
from .schemas import PresentationSchema

router = APIRouter(prefix='/presentation')


@router.get('/', response_model=PresentationSchema)
@inject
def presentation(
    use_case: Annotated[
        PresentationUseCaseProto,
        Depends(Provide[Container.use_case]),
    ],
) -> dict[str, Any]:
    card = use_case.handle()
    return {'presentation': asdict(card)}  # type: ignore[call-overload]
