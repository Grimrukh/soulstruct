from setuptools import setup, find_packages

try:
    with open("README.md") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "<README.md not found>"


def _get_version():
    with open("VERSION") as vfp:
        return vfp.read().strip()


setup(
    name="soulstruct",
    version=_get_version(),
    packages=find_packages(),
    description="Inspect and mod FromSoftware games.",
    long_description=long_description,
    extras_require={
        "Interactive": ["IPython"],
        "Runtime": ["psutil"],
        "ConsoleColor": ["colorama"],
        "Graphs": ["numpy", "matplotlib"],
        "Translate": ["googletrans>=3.1.0a0"],
    },
    author="Scott Mooney (Grimrukh)",
    author_email="grimrukh@gmail.com",
    url="https://github.com/grimrukh/soulstruct",
)
