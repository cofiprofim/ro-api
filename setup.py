import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setup_info = {
    "name": "roblox",
    "version": "",
    "author": "",
    "author_email": "",
    "description": ".",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "",
    "packages": setuptools.find_packages(),
    "classifiers": [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: AsyncIO",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Topic :: Software Development :: Libraries"
    ],
    "python_requires": '>=3.7',
    "install_requires": [
        "httpx>=0.21.0"
    ]
}


setuptools.setup(**setup_info)
