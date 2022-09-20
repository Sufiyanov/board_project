from urllib import request, response
from django.core.exceptions import PermissionDenied

class FilterIPMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        allowed_ips = ['127.0.0.1'] # Authorized ip's
        ip = request.META.get('REMOTE_ADDR') # Get client IP address
        if ip not in allowed_ips:
            raise PermissionDenied # If user is not allowed raise Error
        
        response = self.get_response(request)

        return response
