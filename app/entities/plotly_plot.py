from typing import List

from pydantic import BaseModel, Field


class PlotlyPlot(BaseModel):
    name: str
    x: List[float] = Field(default_factory=list)
    y: List[float] = Field(default_factory=list)
    type: str = "scatter"
