import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requirements = [
    "django>=1.8",
]

setup(
    name='django-blogconnector',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='An easy way to show the contents of a blog in your Django app.',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://www.github.com/avryhof/django-blogconnector',
    author='Amos Vryhof',
    author_email='amos@vryhofresearch.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django',
        'requests',
        'xmltodict'
    ]
)
