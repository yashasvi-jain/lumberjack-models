from setuptools import find_packages, setup
from models import __version__

setup(
    name='Models',
    version=__version__,
    description='The Lumberjack Models library.',
    keywords=['lumberjack', 'models', 'package'],
    packages=find_packages(),
    install_requires=[
        'pydantic',
        'python-dotenv'
    ]
)
