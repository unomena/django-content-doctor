from setuptools import setup, find_packages

setup(
    name='django-content-doctor',
    version='0.0.1',
    description='Django Content Doctor Application',
    author='Unomena',
    author_email='dev@unomena.com',
    url='http://unomena.com',
    packages = find_packages(),
    include_package_data=True,
    install_requires = [],
    zip_safe=False,
)
