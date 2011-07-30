import re

from django.conf import settings


class ContentDoctorMiddleware(object):
    """
    Django middleware to replace patterns in response content.
    """
    def process_response(self, request, response):
        if response.status_code == 200 and response["content-type"].startswith("text/html"):
            for search, replace in settings.CONTENT_DOCTOR_PATTERNS:
                response.content = re.sub(search, '\\1%s\\2' % replace, response.content)
        return response
    
    