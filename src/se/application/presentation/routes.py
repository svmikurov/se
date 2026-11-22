from dataclasses import asdict
from typing import Annotated, Any

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Response, status

from . import PresentationUseCaseProto
from .di import Container
from .schemas import PresentationSchema

router = APIRouter(prefix='/presentation')


@router.get(
    '/',
    response_model=PresentationSchema,
    responses={204: {'description': 'No content'}},
)
@inject
def presentation(
    use_case: Annotated[
        PresentationUseCaseProto,
        Depends(Provide[Container.use_case]),
    ],
) -> dict[str, Any] | Response:
    card = use_case.handle()
    if not card:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return {'presentation': asdict(card)}  # type: ignore[call-overload]
