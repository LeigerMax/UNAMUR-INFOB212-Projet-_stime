__author__ = "AIT HASSOU Mohamed, ALLEMEERSCH Maxime, CAVRENNE Louis, PANS Benjamin, PASTORI Lucas"

import sys

from app.controller.menu import welcome_menu
from app.settings import PyVersion


def main():
    # Version check
    if not (sys.version_info[0] >= PyVersion.MAJOR and sys.version_info[1] >= PyVersion.MINOR):
        raise Exception(f"This project requires Python {PyVersion.MAJOR}.{PyVersion.MINOR} or higher")

    welcome_menu()


if __name__ == "__main__":
    main()
