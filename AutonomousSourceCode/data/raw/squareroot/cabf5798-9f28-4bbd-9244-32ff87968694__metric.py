"""
Log metrics to a [Cube](http://square.github.com/cube/) server.

"""
import os
from cloudly.metric import event

LOG_METRICS = os.environ.get("LOG_METRICS", False)


def evt(evt_type, data=None, request=None):
    if not LOG_METRICS:
        return

    if request:
        if not data:
            data = {}
        data['path'] = request.path
        data['root'] = request.url_root
        data['method'] = request.method
    event(evt_type, data)
