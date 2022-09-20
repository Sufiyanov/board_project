from urllib import request, response
from datetime import datetime
from django.core.exceptions import PermissionDenied

class AccessLogging(object):
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR') # Get client IP address
        query = request.META.get('QUERY_STRING')
        dt_now = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
        response = self.get_response(request)

        f = open("log.txt", "a")
        f.write(f'[{ dt_now }], user ip:{ ip } { request.method } { request.path } { response.status_code }\n')
        f.close()

        return response