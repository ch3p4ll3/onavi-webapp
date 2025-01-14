from datetime import datetime
from typing import List

from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync

from ..entities.measurement import Measurement

# InfluxDB connection details
url = "http://10.188.26.12:8086"
token = "8l8-oOgUaLbY9K-clEVJ9cHOGLeVxpVJq2ZKIO-HxIoCIrLnMiVx0UiJ_IYu4iorkg6BmtqrXCiBsGiBlzJJng=="
org = "org"
bucket = "seismograph"


class InfluxHelper:
    @staticmethod
    async def query_influxdb(start: datetime, stop: datetime):
        data = {}
        async with InfluxDBClientAsync(url=url, token=token, org=org, timeout=90000) as client:
            query_api = client.query_api()
            records = await query_api.query_stream(f'from(bucket:"{bucket}") '
                                                f'|> range(start: {start.isoformat()}, stop: {stop.isoformat()})'
                                                '|> filter(fn: (r) => r["_measurement"] == "MssMeasurement")')

            async for record in records:
                if data.get(record.get_time()) is None:
                    data[record.get_time()] = {
                        record.get_field(): record.get_value()
                    }
                else:
                    data[record.get_time()][record.get_field()] = record.get_value()
        
        return InfluxHelper.parse_data(data)

    @staticmethod
    def parse_data(data: dict) -> List[Measurement]:
        to_ret = []
        for i in data:
            to_ret.append(Measurement(
                    x=data[i].get("x"),
                    y=data[i].get("y"),
                    z=data[i].get("z"),
                    time=i.timestamp()
                )
            )

        return to_ret
