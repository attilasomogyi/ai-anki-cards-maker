# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Anki Card Maker"""

from ankicardmaker.modules.main.run import MainRun


def main():
    """Run the Anki Card Maker."""
    MainRun().run()


if __name__ == "__main__":
    main()
