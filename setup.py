# -*- coding: utf-8 -*-
import io
import os

import setuptools  # type: ignore

package_root = os.path.abspath(os.path.dirname(__file__))

name = "cloudquery-plugin-pb"

description = "CloudQuery Plugin client and server library"

dependencies = [
    "grpcio >= 1.56.0",
    "grpcio-tools >= 1.56.0",
    "protobuf >= 4.23.4",
]
url = "https://github.com/cloudquery/plugin-pb-python"

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

packages = [
    package
    for package in setuptools.PEP420PackageFinder.find()
    if package.startswith("cloudquery")
]
setuptools.setup(
    name=name,
    version="0.0.4",
    description=description,
    long_description=readme,
    author="CloudQuery LTD",
    author_email="pypi-packages@cloudquery.io",
    license="MPL-2.0",
    url=url,
    classifiers=[
        # release_status,
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Topic :: Internet",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=packages,
    python_requires=">=3.7",
    namespace_packages=["cloudquery"],
    # namespace_packages=namespaces,
    install_requires=dependencies,
    include_package_data=True,
    zip_safe=False,
)