import typing

import pandas as pd
import pydantic

from retrack.nodes.base import (
    BaseNode,
    InputConnectionModel,
    NodeKind,
    OutputConnectionModel,
)

################################################
# If Inputs and Outputs
################################################


class IfInputsModel(pydantic.BaseModel):
    input_bool: InputConnectionModel


class IfOutputsModel(pydantic.BaseModel):
    output_then_filter: OutputConnectionModel
    output_else_filter: OutputConnectionModel


################################################
# If Node
################################################


class If(BaseNode):
    inputs: IfInputsModel
    outputs: IfOutputsModel

    def kind(self) -> NodeKind:
        return NodeKind.FILTER

    def run(self, input_bool: pd.Series) -> typing.Dict[str, pd.Series]:
        return {
            f"output_then_filter": input_bool,
            f"output_else_filter": ~input_bool,
        }
