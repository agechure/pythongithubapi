from setuptools import setup 

setup(
    name='python_github_api',
    version='0.0.1'
    description='Simple methods to get most starred python github repositories',
    url='https://github.com/agechure/python-github-api',
    author='Abel Gechure',
    author_email='agechure@fubo.tv',
    license='MIT',
    packages=['python_github_api']
    install_requires=['requests','plotly']

)