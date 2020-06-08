import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyControl4",  # Replace with your own username
    version="0.0.1",
    author="lawtancool",
    author_email="contact@lawrencetan.ml",
    description="Python library for interfacing with Control4 systems via C4soap",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lawtancool/pyControl4",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
