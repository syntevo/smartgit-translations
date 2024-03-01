import sgpo
from path_finder import PoPathFinder


def main():
    # Get file path
    finder = PoPathFinder()
    pot_file = finder.get_pot_file()
    unknown_file = finder.get_unknown_file()

    print(f'    pot file:\t{pot_file}')
    print(f'unknown file:\t{unknown_file}')

    # Open pot/po files
    try:
        pot = sgpo.pofile(pot_file)
        unknown = sgpo.pofile(unknown_file)
    except FileNotFoundError as e:
        print(e)
        exit(-1)

    # Import and specific format
    pot.import_unknown(unknown)
    pot.sort()
    pot.format()

    # Save pot file
    pot.save(pot_file)


if __name__ == "__main__":
    main()
