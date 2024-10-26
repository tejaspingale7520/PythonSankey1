# middleware.py

from django.http import JsonResponse
from django.conf import settings
from base64 import b64decode

def UserAccessPermission(get_response):
    def middleware(request):
        # Check if the request method is one that requires authentication
        if request.method in ['POST', 'GET', 'PUT', 'PATCH','DELETE']:
            auth_header = request.META.get('HTTP_AUTHORIZATION')

            if not auth_header or not auth_header.startswith('Basic '):
                return JsonResponse({'error': 'Unauthorized'}, status=401)

            try:
                # Decode the credentials
                credentials = b64decode(auth_header[6:]).decode('utf-8')
                username, password = credentials.split(':', 1)

                # Validate credentials
                if username == settings.BASIC_AUTH_USERNAME and password == settings.BASIC_AUTH_PASSWORD:
                    # Credentials are valid, proceed to the view
                    response = get_response(request)
                    return response
                else:
                    return JsonResponse({'error': 'Unauthorized'}, status=401)

            except (ValueError, TypeError):
                return JsonResponse({'error': 'Unauthorized'}, status=401)

        return get_response(request)

    return middleware
