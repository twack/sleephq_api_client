from setuptools import setup, find_packages

# Read requirements.txt
with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name='sleephq_api_client',
    version='0.1',
    packages=find_packages(),
    description='A Python application to interact with SleepHQ API.',
    author='Todd Wackford',
    author_email='todd@wackford.net',
    url='https://github.com/twack/sleephq_api_client',
    install_requires=required_packages,
)