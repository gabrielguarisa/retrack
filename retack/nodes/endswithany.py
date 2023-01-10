import pandas as pd
import pydantic

from retack.nodes.base import BaseNode, InputConnectionModel, OutputConnectionModel

################################################
# EndsWithAny Inputs Outputs
################################################


class EndsWithAnyInputsModel(pydantic.BaseModel):
    input_value: InputConnectionModel
    input_list: InputConnectionModel


class EndsWithAnyOutputsModel(pydantic.BaseModel):
    output_bool: OutputConnectionModel


################################################
# EndsWithAny Nodes
################################################


class EndsWithAny(BaseNode):
    inputs: EndsWithAnyInputsModel
    outputs: EndsWithAnyOutputsModel

    def run(self, input_value: pd.Series, input_list: pd.Series) -> pd.Series:
        return {"output_bool": input_value.str.endswith(tuple(input_list.to_list()))}
