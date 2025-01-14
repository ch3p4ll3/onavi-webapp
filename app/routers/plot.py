from typing import List
from datetime import datetime, timedelta

from fastapi import APIRouter

from ..helpers.influx_helper import InfluxHelper
from ..helpers.utils import Utils
from ..entities.plotly_plot import PlotlyPlot


def get_router():
    router = APIRouter()

    @router.get("/", name="plot", response_model=List[PlotlyPlot])
    async def get_measurements(start: datetime, stop: datetime):
        if (stop - start).total_seconds() > 10 * 60:
            stop = start + timedelta(minutes=10)

        influx_data = await InfluxHelper.query_influxdb(start, stop)

        return Utils.convert_to_plotly_plot(influx_data)

    return router
