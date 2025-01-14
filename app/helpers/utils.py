from typing import List

from ..entities.measurement import Measurement
from ..entities.plotly_plot import PlotlyPlot


class Utils:
    @staticmethod
    def convert_to_plotly_plot(data: List[Measurement]) -> List[PlotlyPlot]:
        x = PlotlyPlot(name="X")
        y = PlotlyPlot(name="Y")
        z = PlotlyPlot(name="Z")
        magnitude = PlotlyPlot(name="Magnitude")

        for i in data:
            x.x.append(i.time)
            y.x.append(i.time)
            z.x.append(i.time)
            magnitude.x.append(i.time)

            x.y.append(i.x)
            y.y.append(i.y)
            z.y.append(i.z)
            magnitude.y.append(i.magnitude)
        
        return [x, y, z, magnitude]
