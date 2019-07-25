from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
        name='gameoflife',
        version='0.0.1',
        description='Conway\'s Game of Life',
        long_description=readme,
        author='Peter Hall',
        author_email='ph@ll.id.au',
        url='https://github.com/peterkh/gameoflife-py',
        license=license,
        packages=find_packages(exclude=('tests'))
        )

