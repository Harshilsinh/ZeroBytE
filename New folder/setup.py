from setuptools import setup, find_packages

setup(
    name="ZeroBytE",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Harshil",
    author_email="harshilsinh1516@gmail.com",
    description="A Python library for food inventory and waste management",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/harshilsinh/zerobyte",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
