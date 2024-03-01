import sgpo
from path_finder import PoPathFinder


def main():
    # Get file path
    finder = PoPathFinder()
    pot_file = finder.get_pot_file()
    po_files = finder.get_po_files(translation_file_only=True)

    try:
        pot = sgpo.pofile(pot_file)
    except FileNotFoundError as e:
        print(e)
        exit(-1)

    print(f'pot file:\t{pot_file}')

    for po_file in po_files:
        try:
            po = sgpo.pofile(po_file)
            print(f' po file:\t{po_file}')
        except FileNotFoundError as e:
            print(e)
            exit(-1)

        # Import and specific format
        po.import_pot(pot)
        po.sort()
        po.format()

        # Save pot file
        po.save(po_file)


if __name__ == "__main__":
    main()
