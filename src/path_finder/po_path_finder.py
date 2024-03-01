import os
import glob
from typing import AnyStr


class PoPathFinder:
    """
    This class provides the functionality for returning the paths to each file
    in the repository that is used for translation.
    """

    def __init__(self, repository_root_dir="", version='24_1'):
        self.version = version
        if repository_root_dir == "":
            self.root_dir = get_repository_root()
        else:
            self.root_dir = repository_root_dir

    def get_po_files(self, translation_file_only=True) -> list:
        if translation_file_only:
            pathname = os.path.join(self.get_po_file_dir(), '??_??.po')
        else:
            pathname = os.path.join(self.get_po_file_dir(), '*.po')
        po_files = glob.glob(pathname)

        return po_files

    def get_pot_file(self) -> str:
        return os.path.join(self.get_po_file_dir(), 'messages.pot')

    def get_po_file_dir(self) -> str:
        return os.path.join(self.root_dir, 'po')

    def get_mismatch_file(self) -> str:
        return os.path.join(self.get_po_file_dir(), f'mismatch.{self.version}')

    def get_unknown_file(self) -> str:
        return os.path.join(self.get_po_file_dir(), f'unknown.{self.version}')


def get_repository_root() -> str:
    return dirname(dirname(dirname(os.path.abspath(__file__))))


def dirname(p: os.PathLike[AnyStr]) -> AnyStr:
    """
    Alias for os.path.dirname()
    """

    return os.path.dirname(p)


def main():
    path_finder = PoPathFinder()
    pot_file = path_finder.get_pot_file()
    po_list = path_finder.get_po_files(translation_file_only=True)
    unknown_file = path_finder.get_unknown_file()
    mismatch_file = path_finder.get_mismatch_file()

    print(f"pot file:\t{pot_file}")
    for po_file in po_list:
        print(f"po file:\t{po_file}")

    print(f"unknown file:\t{unknown_file}")
    print(f"mismatch file:\t{mismatch_file}")


if __name__ == "__main__":
    main()
