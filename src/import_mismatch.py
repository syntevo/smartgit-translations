from path_finder import PoPathFinder
import sgpo


def main():
    # Get file path
    finder = PoPathFinder()
    pot_file = finder.get_pot_file()
    mismatch_file = finder.get_mismatch_file()

    print(f'     pot file:\t{pot_file}')
    print(f'mismatch file:\t{mismatch_file}')

    # Open pot/po files
    try:
        pot = sgpo.pofile(pot_file)
        mismatch = sgpo.pofile(mismatch_file)
    except FileNotFoundError as e:
        print(e)
        exit(-1)

    # Import and specific format
    pot.import_mismatch(mismatch)
    pot.sort()

    # Save pot file
    pot.save(pot_file)


if __name__ == "__main__":
    main()
