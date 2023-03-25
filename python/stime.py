__author__ = "AIT HASSOU Mohamed, ALLEMEERSCH Maxime, CAVRENNE Louis, PANS Benjamin, PASTORI Lucas"

import sys

PY_VERSION_MAJOR = 3
PY_VERSION_MINOR = 10


def main():
    # Version check
    if not (sys.version_info[0] == PY_VERSION_MAJOR and sys.version_info[1] >= PY_VERSION_MINOR):
        raise Exception(f"This project requires Python {PY_VERSION_MAJOR}.{PY_VERSION_MINOR} or higher")

    print("Hello World!")


if __name__ == "__main__":
    main()
