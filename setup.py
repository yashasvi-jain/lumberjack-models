from setuptools import find_packages, setup

__version__ = '0.0.3'

setup(
    name='Models',
    version=__version__,
    description='The Lumberjack Models library.',
    keywords=['lumberjack', 'models', 'package'],
    url='https://github.com/yashasvi-jain/lumberjack-models',
    packages=find_packages(),
    install_requires=[
        'pydantic',
        'python-dotenv'
    ]
)
