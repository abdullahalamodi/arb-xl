from setuptools import setup, find_packages

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="arb-xl",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openpyxl",
    ],
    entry_points={
        "console_scripts": [
            "arb-xl=arb_xl.main:main"
        ]
    },
    long_description=long_description,  # Add this
    long_description_content_type="text/markdown",  # Specify Markdown format
    author="alamodi",
    author_email="alamodi326@gmail.com",
    description="A CLI tool to convert JSON/ARB translation files to Excel and vice versa.",
    url="https://github.com/abdullahalamodi/arb-xl",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
