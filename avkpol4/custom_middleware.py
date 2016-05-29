from datetime import datetime
from models import RequestLog


class SaveRequestDb():

    def process_request(self, request):

        request_path = request.path
        req = RequestLog(
            requested_url=request.build_absolute_uri(request_path),
            datetime=datetime.now(),
            request_type=request.method,
            request_ip=request.META['REMOTE_ADDR'],
        )
        req.save()


def last_10():

    last_10 = RequestLog.objects.filter().order_by('-datetime')[: 10]

    return last_10