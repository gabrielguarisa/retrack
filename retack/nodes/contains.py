import pandas as pd
import pydantic

from retack.nodes.base import BaseNode, InputConnectionModel, OutputConnectionModel

################################################
# Contains Inputs Outputs
################################################


class ContainsInputsModel(pydantic.BaseModel):
    input_list: InputConnectionModel
    input_value: InputConnectionModel


class ContainsOutputsModel(pydantic.BaseModel):
    output_bool: OutputConnectionModel


################################################
# Contains Nodes
################################################


class Contains(BaseNode):
    inputs: ContainsInputsModel
    outputs: ContainsOutputsModel

    def run(self, input_list: pd.Series, input_value: pd.Series) -> pd.Series:
        return {"output_bool": input_value.isin(input_list.to_list())}
