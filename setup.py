import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 
                       "README.rst")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(
    os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-conductor-settings",
    version="0.1",
    packages=find_packages(),
    install_requires=['django',],
    include_package_data=True,
    license="BDS License",
    escription="A django app to store settings for conductor",
    long_description=README,

    url="https://github.com/conductorproject/django-conductor-settings",
    author='Ricardo Garcia Silva',
    author_email='ricardo.garcia.silva@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
