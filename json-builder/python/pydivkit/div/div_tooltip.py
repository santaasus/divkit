# Generated code. Do not modify.

from __future__ import annotations
from pydivkit.core import BaseDiv, Field
import enum
import typing

from . import div
from . import div_animation
from . import div_point


# Tooltip.
class DivTooltip(BaseDiv):

    def __init__(
        self, *,
        div: div.Div,
        id: str,
        position: DivTooltipPosition,
        animation_in: typing.Optional[div_animation.DivAnimation] = None,
        animation_out: typing.Optional[div_animation.DivAnimation] = None,
        duration: typing.Optional[int] = None,
        offset: typing.Optional[div_point.DivPoint] = None,
    ):
        super().__init__(
            animation_in=animation_in,
            animation_out=animation_out,
            div=div,
            duration=duration,
            id=id,
            offset=offset,
            position=position,
        )

    animation_in: typing.Optional[div_animation.DivAnimation] = Field(description='Tooltip appearance animation. By default, the tooltip will be appearing graduallywith an offset from the anchor point by 10 dp.')
    animation_out: typing.Optional[div_animation.DivAnimation] = Field(description='Tooltip disappearance animation. By default, the tooltip will disappear graduallywith an offset from the anchor point by 10 dp.')
    div: div.Div = Field(description='An element that will be shown in a tooltip. If there are tooltips inside anelement, they won\'t be shown.')
    duration: typing.Optional[int] = Field(description='Duration of the tooltip visibility in milliseconds. When the value is set to `0`,the tooltip will be visible until the user hides it.')
    id: str = Field(min_length=1, description='Tooltip ID. It is used to avoid re-showing. It must be unique for all elementtooltips.')
    offset: typing.Optional[div_point.DivPoint] = Field(description='Shift relative to an anchor point.')
    position: DivTooltipPosition = Field(description='The position of a tooltip relative to an element it belongs to.')


class DivTooltipPosition(str, enum.Enum):
    LEFT = 'left'
    TOP_LEFT = 'top-left'
    TOP = 'top'
    TOP_RIGHT = 'top-right'
    RIGHT = 'right'
    BOTTOM_RIGHT = 'bottom-right'
    BOTTOM = 'bottom'
    BOTTOM_LEFT = 'bottom-left'


DivTooltip.update_forward_refs()
