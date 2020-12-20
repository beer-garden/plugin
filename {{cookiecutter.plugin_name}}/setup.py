import re

from setuptools import setup


def find_version(version_file):
    version_line = open(version_file, "rt").read()
    match_object = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_line, re.M)

    if not match_object:
        raise RuntimeError("Unable to find version string in %s" % version_file)

    return match_object.group(1)


setup(
    name="{{ cookiecutter.plugin_name }}",
    version=find_version("{{ cookiecutter.package_name }}/__version__.py"),
    description="{{ cookiecutter.description }}",
    url="{{ cookiecutter.url }}",
    author="{{ cookiecutter.author }}",
    author_email=" ",
    license="{{ cookiecutter.license }}",
    packages=["{{ cookiecutter.package_name }}"],
    install_requires=["brewtils"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
