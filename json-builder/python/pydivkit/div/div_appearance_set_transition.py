# Generated code. Do not modify.

from __future__ import annotations
from pydivkit.core import BaseDiv, Field
import enum
import typing

from . import div_appearance_transition


# A set of animations to be applied simultaneously.
class DivAppearanceSetTransition(BaseDiv):

    def __init__(
        self, *,
        items: typing.List[div_appearance_transition.DivAppearanceTransition],
        type: str = 'set',
    ):
        super().__init__(
            type=type,
            items=items,
        )

    type: str = Field(default='set')
    items: typing.List[div_appearance_transition.DivAppearanceTransition] = Field(min_items=1, description='An array of animations.')


DivAppearanceSetTransition.update_forward_refs()
