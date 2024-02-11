import sgpo
from path_finder import PoPathFinder


def main():
    finder = PoPathFinder()
    po_files = finder.get_po_files(translation_file_only=True)

    for po_file in po_files:
        try:
            po = sgpo.pofile(po_file)
            print(f' po file:\t{po_file}')
        except FileNotFoundError as e:
            print(e)
            exit(-1)

        po.format()
        po.save(po_file)

if __name__ == "__main__":
    main()
