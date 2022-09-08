from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse,HttpResponseRedirect
class mymiddleware(MiddlewareMixin):
     def process_request(self, request):
        # print("in my middleware")
        if not request.user.is_authenticated  and request.path  not in ["/home/products/","/home/login/"]:
            print(request.path)
            return HttpResponse("forbidden")