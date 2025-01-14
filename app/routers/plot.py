from typing import List
from datetime import datetime, timedelta

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from ..helpers.influx_helper import InfluxHelper
from ..entities.measurement import Measurement

def get_router():
    router = APIRouter()

    @router.get("/", response_model=List[Measurement])
    async def get_measurements(start: datetime, stop: datetime):
        if (stop - start).total_seconds() > 10 * 60:
            stop = start + timedelta(minutes=10)

        return StreamingResponse(InfluxHelper.query_influxdb(start, stop), media_type="application/json")

    return router
