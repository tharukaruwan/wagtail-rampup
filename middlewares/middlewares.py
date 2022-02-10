from firebase_admin import auth

# middlewares could be ether class of functional 
# Each middle ware trigger methods 3 times => at application initialisatation, when get request and send response

# Below is a function middleware
def tocken_decode(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        decoded_tocken=False
        try:
            auth_header=request.META.get('HTTP_AUTHORIZATION')
            tocken=auth_header.replace('Bearer ','')
            decoded_tocken=auth.verify_id_token(tocken)
        except:
            decoded_tocken=False
        
        if decoded_tocken:
            request.tocken=decoded_tocken
        else:
            request.tocken=''

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
