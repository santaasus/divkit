# Generated code. Do not modify.

from __future__ import annotations
from pydivkit.core import BaseDiv, Field
import enum
import typing

from . import div_corners_radius
from . import div_shadow
from . import div_stroke


# Stroke around the element.
class DivBorder(BaseDiv):

    def __init__(
        self, *,
        corner_radius: typing.Optional[int] = None,
        corners_radius: typing.Optional[div_corners_radius.DivCornersRadius] = None,
        has_shadow: typing.Optional[bool] = None,
        shadow: typing.Optional[div_shadow.DivShadow] = None,
        stroke: typing.Optional[div_stroke.DivStroke] = None,
    ):
        super().__init__(
            corner_radius=corner_radius,
            corners_radius=corners_radius,
            has_shadow=has_shadow,
            shadow=shadow,
            stroke=stroke,
        )

    corner_radius: typing.Optional[int] = Field(description='One radius of element and stroke corner rounding. Has a lower priority than`corners_radius`.')
    corners_radius: typing.Optional[div_corners_radius.DivCornersRadius] = Field(description='Multiple radii of element and stroke corner rounding.')
    has_shadow: typing.Optional[bool] = Field(description='Adding shadow.')
    shadow: typing.Optional[div_shadow.DivShadow] = Field(description='Shadow parameters.')
    stroke: typing.Optional[div_stroke.DivStroke] = Field(description='Stroke style.')


DivBorder.update_forward_refs()
