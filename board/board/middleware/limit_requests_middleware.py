from urllib import request, response
from django.core.exceptions import PermissionDenied
import time

#from ratelimit.decorators import ratelimit

ip_buffer = {}
black_list = []

COUNT_REQUESTS = 10 
WAITING_TIME = 5 #SECOND

def dequeue(ip, buffer, now):
    for old_time in buffer[ip]:
        if now - old_time > WAITING_TIME:
            buffer[ip].remove(old_time)
        print(buffer)        
        return buffer


class LimitRequestsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    #@ratelimit(key='ip', rate='5/m', block=True) 
    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR') # Get client IP address
        now = time.time()
        ip_buffer[ip] = ip_buffer.get(ip, []) + [now]
        print(ip_buffer)        
        verified_buffer = dequeue(ip, ip_buffer, now)
        if len(verified_buffer[ip]) >= COUNT_REQUESTS:
            black_list.append(ip)
        
        if ip in black_list:
            raise PermissionDenied
        
        response = self.get_response(request)
        return response

        

