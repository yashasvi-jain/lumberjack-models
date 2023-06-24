from setuptools import setup

setup(
    name='Models',
    version='1.0.0',
    description='The Lumberjack Models library.',
    keywords=['lumberjack', 'models', 'package'],
    packages=[
        'models',
        ],
    install_requires=[
        'pydantic',
        'python-dotenv'
    ]
)