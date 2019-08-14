import autotest
from setuptools import find_packages, setup


def read(path):
    with open(path, 'rb') as fid:
        return fid.read().decode('utf-8')


setup(
    name="autotest",
    version=autotest.__VERSION__,
    url="https://github.com/kumarvaradarajulu/autotest",
    author='Kumar',
    author_email="kumar.varadarajulu@test.com",
    description='AI tool for Auto unit Test generation',
    download_url=(
    ),
    include_package_data=True,
    packages=find_packages(),
    package_data={'autotest': ['README.rst']},
    zip_safe=False,
    install_requires=[
        'setuptools',
        'sh',
        'argparse',
        'six',
        'mock',
        'simplejson',
        'funcsigs',
        'codegen',
    ],
    entry_points={
        'console_scripts': [
            'autotest=autotest.main:main'
        ]
    },
    dependency_links=[]
)
