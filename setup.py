from setuptools import setup

try:
    with open('README.md') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = '<README.md not found>'

setup(
    name='soulstruct',
    version='0.1',
    packages=['soulstruct'],
    description='Inspect and mod FromSoft games.',
    long_description=long_description,
    extras_require={'Interactive': ['IPython'], 'Runtime': ['psutil'], 'ConsoleColor': ['colorama'],
                    "Hotkeys": ['keyboard']},
    author='Scott Mooney',
    author_email='grimrukh@gmail.com',
    url="https://github.com/grimrukh/soulstruct",
    )
