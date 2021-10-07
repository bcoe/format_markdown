import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

dependencies = [
    "xmltodict",
    "markdown",
]

setuptools.setup(
    name="format_markdown",
    version="0.0.1",
    author="Benjamin Coe",
    author_email="bencoe@gmail.com",
    description="make release note format consistent across languages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bcoe/format-markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=dependencies,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
