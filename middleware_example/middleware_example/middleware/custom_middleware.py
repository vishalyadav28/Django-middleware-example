from  middleware_example.constants import *
class CustomMiddleware:
    def custom_header_check(self, *args, **kwargs):
        custom_header : bool = True if self.headers.get('custom_header') else "error: Authentication"

        return True if custom_header else False
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization code goes here (optional)
    



    

    def __call__(self, request):
        # Code to be executed for each request before the view (optional)

        # response = self.get_response(request)
        print('+++++++++++++++++++++++++')
        if not CustomMiddleware.custom_header_check(request):
                return JsonResponse({'status':0 , 'error':{'message':INVALID_TOKEN,'error_code':STATUS_USER_ERROR}}, status=STATUS_FAILED)
        

        

        # Code to be executed for each request/response after the view (optional)
        


        
    
