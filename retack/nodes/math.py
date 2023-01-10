import typing

import enum

import pandas as pd
import pydantic

from retack.nodes.base import BaseNode, InputConnectionModel, OutputConnectionModel

###############################################################
# Math Metadata Models
###############################################################


class MathOperator(str, enum.Enum):
    SUM = "+"
    SUB = "-"
    DIVISION = "/"
    MULTIPLY = "*"


class MathMetadataModel(pydantic.BaseModel):
    operator: typing.Optional[MathOperator] = MathOperator.SUM


###############################################################
# Math Inputs and Outputs
###############################################################


class MathInputsModel(pydantic.BaseModel):
    input_value_0: InputConnectionModel
    input_value_1: InputConnectionModel


class MathOutputsModel(pydantic.BaseModel):
    output_value: OutputConnectionModel


###############################################################
# Math Node
###############################################################


class Math(BaseNode):
    data: MathMetadataModel
    inputs: MathInputsModel
    outputs: MathOutputsModel

    @property
    def node_type(self) -> str:
        return "logic.math"

    def run(
        self,
        input_value_0: pd.Series,
        input_value_1: pd.Series,
    ) -> typing.Dict[str, pd.Series]:
        if self.data.operator == MathOperator.SUM:
            return {"output_value": input_value_0 + input_value_1}
        elif self.data.operator == MathOperator.SUB:
            return {"output_value": input_value_0 - input_value_1}
        elif self.data.operator == MathOperator.DIVISION:
            return {"output_value": input_value_0 * input_value_1}
        elif self.data.operator == MathOperator.MULTIPLY:
            return {"output_value": input_value_0 / input_value_1}
        else:
            raise ValueError("Unknown operator")