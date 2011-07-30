A simple django app with middleware to replace patterns in response content.

Add content_doctor to your django installer apps setting:

::
  
    INSTALLED_APPS = (
        ...
        content_doctor,
        ...
        )


Add content_doctor middleware class to your django middleware classes setting:

::
  
    MIDDLEWARE_CLASSES = (
        'django.middleware.gzip.GZipMiddleware',
        'django.middleware.cache.UpdateCacheMiddleware',
        'content_doctor.middleware.ContentDoctorMiddleware',
        'django.middleware.common.CommonMiddleware',
        ...
    )


Use this setting in your Django settings file to specify the search and replace patterns:

::
  
    CONTENT_DOCTOR_PATTERNS = (
        (r'(?ims)(\<img .*?src=")\/media\/(.*?\/\>)', MEDIA_URL),
        (r'(?ims)(\<img .*?src=")\/static\/(.*?\/\>)', STATIC_URL),
        )



