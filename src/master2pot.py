from sgpo_common import *
from sgv23_mapping import SgMap


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    master_map_file = get_master_mapping_file(base_dir)
    po_dir = get_po_dir(base_dir)
    if not os.path.exists(po_dir):
        os.makedirs(po_dir)

    pot_file = os.path.join(po_dir, "messages.pot")

    # Load mapping files
    master_map = SgMap(master_map_file, 'en_US')

    print("# of items:")
    print(f"\tmaster: {str(master_map.number_of_entries)}")

    # Convert and save to pot file.
    SgMap_to_pot_file(master_map, pot_file)


# ======================================================================
def SgMap_to_pot_file(master_map: SgMap, pot_file_path: str) -> None:
    pot = polib.POFile()
    pot.wrapwidth = 1000

    meta_dict = create_meta_dict(master_map.locale_code)

    for key, value in meta_dict.items():
        pot.metadata[key] = value

    for map_entry in master_map.get_values():
        entry = polib.POEntry(
            msgctxt=map_entry.key, msgid=map_entry.value, msgstr="")

        # convert to optimized entry
        entry = optimize_po_entry(entry)

        pot.append(entry)

    pot.save(pot_file_path)


if __name__ == "__main__":
    main()
