from settings import *

def appurl(request):
    """Return a APP_URL template context for the current request."""
    if request.is_secure():
        scheme = 'https://'
    else:
        scheme = 'http://'
    return {'APP_URL': scheme + request.get_host() + APP_URL,}
