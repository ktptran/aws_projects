from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='Kevin Tran',
    author_email='kevint24@uw.edu',
    description='Webotron 80 is a tool to deploy static websites to AWS.',
    license='GPLv3+',
    packages=['webotron'],
    url='https://github.com/ktptran/aws_projects/tree/master/automating-aws-with-python/01-webotron',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)
