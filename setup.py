from setuptools import find_packages, setup

setup(
    name='project_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'PyYAML'
    ],
)