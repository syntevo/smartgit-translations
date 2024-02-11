import sgpo
from path_finder import PoPathFinder


def main():
    finder = PoPathFinder()
    pot_file = finder.get_pot_file()
    print(f'    pot file:\t{pot_file}')

    try:
        pot = sgpo.pofile(pot_file)
    except FileNotFoundError as e:
        print(e)
        exit(-1)

    pot.delete_extracted_comments()
    pot.save(pot_file)

if __name__ == "__main__":
    main()
