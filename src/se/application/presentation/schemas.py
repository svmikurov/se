from pydantic import BaseModel

from se.domain.values import Card


class PresentationSchema(BaseModel):
    presentation: Card
