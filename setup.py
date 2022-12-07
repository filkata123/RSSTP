"""Package configuration."""
from setuptools import find_packages, setup

setup(
    name="RSSTP",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'numpy>=1.23.4',
        'shapely>=1.8.5.post1',
        'matplotlib>=3.6.2'
    ],
)