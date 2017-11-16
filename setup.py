from distutils.core import setup

setup(
    name='HTTPUploadFile',
    version='0.0.1',
    packages=['simple_upload'],
    url='https://github.com/codeif/SimpleUpload',
    license='MIT',
    author='codeif',
    author_email='me@codeif.com',
    description='Upload file via HTTP.',
    install_requires=['Flask']
)
