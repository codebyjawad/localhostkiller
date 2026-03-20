from setuptools import setup, find_packages

setup(
    name="localhostkiller",
    version="0.1.0",
    description="Kill localhost processes with style",
    author="Jawad",
    author_email="jawad@makeworking.com",
    url="https://github.com/jawad/localhostkiller",
    py_modules=["lhk"],
    install_requires=[
        "rich>=13.0.0",
        "psutil>=5.9.0",
    ],
    entry_points={
        "console_scripts": [
            "lhk=lhk:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)
