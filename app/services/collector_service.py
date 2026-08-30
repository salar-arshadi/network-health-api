from app.collectors.linux_collector import LinuxCollector
from app.schemas.device import LinuxCollectorRequest


class CollectorService:

    @staticmethod
    def collect_linux(request: LinuxCollectorRequest):

        collector = LinuxCollector(
            host=request.host,
            username=request.username,
            password=request.password,
            port=request.port,
        )

        return collector.collect()
