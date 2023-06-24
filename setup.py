from setuptools import find_packages, setup

setup(
    name='Models',
    version='1.0.0',
    description='The Lumberjack Models library.',
    keywords=['lumberjack', 'models', 'package'],
    packages=find_packages(),
    install_requires=[
        'pydantic',
        'python-dotenv'
    ]
)
