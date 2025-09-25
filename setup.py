#!/usr/bin/env python3
"""
Setup script for Python Math Calculator
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="python-math-calculator",
    version="1.0.0",
    author="SDLC Agent",
    author_email="your.email@example.com",
    description="A production-ready command-line calculator utility for basic math operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shyamnarayan2001/python-math-calculator-1",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "dev": requirements,
        "test": ["pytest>=7.0.0", "pytest-cov>=4.0.0"],
    },
    entry_points={
        "console_scripts": [
            "calculator=calculator_main:main",
        ],
    },
    keywords="calculator, math, command-line, cli, addition, subtraction, sdlc",
    project_urls={
        "Bug Reports": "https://github.com/shyamnarayan2001/python-math-calculator-1/issues",
        "Source": "https://github.com/shyamnarayan2001/python-math-calculator-1",
        "Documentation": "https://github.com/shyamnarayan2001/python-math-calculator-1/blob/main/README.md",
    },
)