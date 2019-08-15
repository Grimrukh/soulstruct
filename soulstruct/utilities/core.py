import textwrap

__all__ = ['auto_wrap']


def auto_wrap(string, line_limit=50):
    return '\n'.join(textwrap.wrap(string, line_limit))
