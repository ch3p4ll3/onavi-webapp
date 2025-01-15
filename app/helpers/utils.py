from typing import List
from io import BytesIO, TextIOWrapper
from csv import reader

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

    @staticmethod
    async def import_csv_file(data: BytesIO) -> List[Measurement]:
        measurements = []
        csv_file = TextIOWrapper(data, encoding="utf-8")

        spamreader = reader(csv_file, delimiter=',')

        next(spamreader) # skip header

        for row in spamreader:
            measurements.append(
                Measurement(
                    time=float(row[0]) * 1e9,
                    x=float(row[1]),
                    y=float(row[2]),
                    z=float(row[3])
                )
            )

        return measurements
