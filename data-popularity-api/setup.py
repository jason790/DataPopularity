from setuptools import setup, find_packages

setup(
    name='data-popularity-api',
    version='0.1',
    url='',
    license='',
    packages=find_packages(),
    author='mikhail91',
    author_email='mikhail91@yandex-team.ru',
    description='Api service for DataPopularity module',
    install_requires=[
        'flask',
        'flask-restful',
        'Werkzeug',
        'rep==0.5.0',
        'DataPopularity==0.2'
    ],
)