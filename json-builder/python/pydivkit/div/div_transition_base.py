# Generated code. Do not modify.

from __future__ import annotations
from pydivkit.core import BaseDiv, Field
import enum
import typing

from . import div_animation_interpolator


class DivTransitionBase(BaseDiv):

    def __init__(
        self, *,
        duration: typing.Optional[int] = None,
        interpolator: typing.Optional[div_animation_interpolator.DivAnimationInterpolator] = None,
        start_delay: typing.Optional[int] = None,
    ):
        super().__init__(
            duration=duration,
            interpolator=interpolator,
            start_delay=start_delay,
        )

    duration: typing.Optional[int] = Field(description='Animation duration in milliseconds.')
    interpolator: typing.Optional[div_animation_interpolator.DivAnimationInterpolator] = Field(description='Transition speed nature.')
    start_delay: typing.Optional[int] = Field(description='Delay in milliseconds before animation starts.')


DivTransitionBase.update_forward_refs()
