#!/bin/env python2

from subprocess import call

from platform import uname
import setuptools.command.build_py
from setuptools import setup, find_packages

class BuildPyCommand(setuptools.command.build_py.build_py):
  """Custom build command."""

  def run(self):
    setuptools.command.build_py.build_py.run(self)


setup(
    cmdclass = {
        "build_py": BuildPyCommand,
    },
    include_package_data = True,    # include everything in source control
    name = "orbs-client-sdk",
    version = "0.1.0",
    description = "Orbs Client SDK",
    author = "Orbs Team",
    packages = ["orbs_client"],
    install_requires = ["requests"],
    url = "https://github.com/orbs-network/orbs-client-sdk-python"
)
