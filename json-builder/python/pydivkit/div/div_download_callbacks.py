# Generated code. Do not modify.

from __future__ import annotations
from pydivkit.core import BaseDiv, Field
import enum
import typing

from . import div_action


# Callbacks that are called after [data
# loading](../../interaction.dita#loading-data).
class DivDownloadCallbacks(BaseDiv):

    def __init__(
        self, *,
        on_fail_actions: typing.Optional[typing.List[div_action.DivAction]] = None,
        on_success_actions: typing.Optional[typing.List[div_action.DivAction]] = None,
    ):
        super().__init__(
            on_fail_actions=on_fail_actions,
            on_success_actions=on_success_actions,
        )

    on_fail_actions: typing.Optional[typing.List[div_action.DivAction]] = Field(min_items=1, description='Actions in case of unsuccessful loading if the host reported it or the waitingtime expired.')
    on_success_actions: typing.Optional[typing.List[div_action.DivAction]] = Field(min_items=1, description='Actions in case of successful loading.')


DivDownloadCallbacks.update_forward_refs()
