from setuptools import find_packages, setup

setup(
    name='jackmodels',
    version='0.0.1',
    description='The Lumberjack Models library.',
    keywords=['lumberjack', 'models', 'package'],
    url='https://github.com/yashasvi-jain/lumberjack-models',
    packages=find_packages(),
    install_requires=[
        'pydantic',
        'python-dotenv'
    ]
)
