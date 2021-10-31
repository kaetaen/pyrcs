from setuptools import setup, find_packages

def read_requirements(file):
    return [req.strip() for req in open(file).readlines()];
    

setup(
    name="pyrcs",
    version="0.2.0",
    description="Lyrics API",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "dev":read_requirements("requirements-dev.txt")
    }
)
