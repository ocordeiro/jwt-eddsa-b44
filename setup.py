import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eddsa-jwt-b44",
    version="0.0.1",
    author="Aveek Das",
    description="Implementation of EdDSA JWT with base44 encoding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                            
    python_requires='>=3.6',
    py_modules=["eddsa-jwt-b44"],
    package_dir={'':'src'},
    install_requires=["cryptography"]
)