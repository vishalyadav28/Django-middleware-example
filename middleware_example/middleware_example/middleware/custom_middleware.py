from  middleware_example.constants import *        
from django.http import HttpResponseForbidden

class CustomMiddleware:
    ALLOWED_PATHS = [
        '/swagger/',  # Example path to allow
        '/admin/',  # Example path to allow
        # Add more paths here that should bypass the middleware
    ]
        
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

         # Check if the request path is in the allowed paths list
        if request.path in self.ALLOWED_PATHS:
            # If the request path is in the allowed paths list, skip the middleware logic
            return self.get_response(request)

        # Code to be executed for each request before the view (get_response) is called
        token : bool = True if request.META.get('token') else False

        if not token:
            return HttpResponseForbidden("You are not authenticated.")
        
        response = self.get_response(request)
        
        return response
    
    # def process_view(request, view_func, view_args, view_kwargs):
        # This code is executed just before the view is called

    # def process_exception(request, exception):
        # This code is executed if an exception is raised

    # def process_template_response(request, response):
        # This code is executed if the response contains a render() method
        # return response
