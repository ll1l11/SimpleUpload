from distutils.core import setup

setup(
    name='HTTPUploadFile',
    version='0.0.1',
    packages=[''],
    url='https://github.com/codeif/HTTPUploadFile',
    license='MIT',
    author='codeif',
    author_email='me@codeif.com',
    description='Upload file via HTTP.',
    entry_point={
        'console_scripts': [
            'uplocal = http_upload.local:main',
            'upserver = http_upload.server:main'
        ]
    }
)
