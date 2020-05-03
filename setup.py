import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easedl-devbihari", # Replace with your own username
    version="0.0.1",
    author="Amit Jha",
    author_email="amit.jha6700@gmail.com",
    description="A package to generate deep learning model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devbihari/EasyDL",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)