from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="diversipy",
    version="0.8",
    author="Simon Wessing",
    description="Sample in hypercubes, select diverse subsets, and measure diversity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DavidWalz/diversipy",
    packages=find_packages(),
    python_requires=">=3.5",
    install_requires=["numpy", "scipy"],
)
