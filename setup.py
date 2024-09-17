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
    "pyarrow >= 13.0.0",
]
url = "https://github.com/cloudquery/plugin-pb-python"

package_root = os.path.abspath(os.path.dirname(__file__))

long_description = """
Python Low Level Client for CloudQuery Plugin
================================================

Overview
-----------

This is low level gRPC APIs for CloudQuery Plugin. Please see more on [github.com/cloudquery/plugin-pb-python](https://github.com/cloudquery/plugin-pb-python)
"""

packages = [
    package
    for package in setuptools.PEP420PackageFinder.find()
    if package.startswith("cloudquery")
]
setuptools.setup(
    name=name,
    version="0.0.35",
    description=description,
    long_description=long_description,
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
    package_data={
        "cloudquery": [
            "plugin_v3/py.typed",
            "plugin_v3/*.pyi",
            "discovery_v1/py.typed",
            "discovery_v1/*.pyi",
        ]
    },
    zip_safe=False,
)
