# -*- coding: utf-8 -*-
def hello() -> str:
    """Return hello world."""
    return "Hello, world!"


def say_hello() -> None:
    """Print hello world."""
    print(hello())


if __name__ == "__main__":
    say_hello()  # pragma: no cover
