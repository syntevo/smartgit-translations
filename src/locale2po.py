from sgpo_common import *
from sgv23_mapping import SgMap, CombinedSgMap



def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    master_map_file = os.path.normpath(os.path.join(base_dir, "mapping"))
    po_dir = get_po_dir(base_dir)

    if not os.path.exists(po_dir):
        os.makedirs(po_dir)

    for locale_code, locale_dir in LOCALE_NAME_DIR_DICT.items():
        locale_map_file = os.path.normpath(os.path.join(base_dir, f".\\{locale_dir}\\mapping.dev"))
        state_map_file = os.path.normpath(os.path.join(base_dir, f".\\{locale_dir}\\mapping.state"))
        output_file = os.path.normpath(os.path.join(po_dir, f"{locale_code}.po"))

        print('Loading mapping files...')
        # Load mapping files
        master_map = SgMap(master_map_file, 'en_US')
        locale_map = SgMap(locale_map_file, locale_code)
        state_map = SgMap(state_map_file, locale_code)

        print(f'{locale_code} loaded.')
        print("# of items:")
        print(f"\tmaster: {str(master_map.number_of_entries)}")
        print(f"\tlocale: {str(locale_map.number_of_entries)}")
        print(f"\tstate: {str(state_map.number_of_entries)}")

        # Combine mapping files
        combined_map = CombinedSgMap(master_map, locale_map, state_map)

        # Convert and save to po file.
        po = CombinedSgMap_to_po(combined_map)
        po.save(output_file)
        print('output:' + output_file)


def create_meda_dict(locale_code: str) -> dict:
    meta_data_dict = META_DATA_BASE_DICT
    meta_data_dict['Language'] = locale_code

    return meta_data_dict


# ======================================================================
def CombinedSgMap_to_po(combined_map: CombinedSgMap) -> polib.POFile:
    po = polib.POFile()
    po.wrapwidth = 1000

    meta_dict = create_meta_dict(combined_map.locale_code)

    for key, value in meta_dict.items():
        po.metadata[key] = value

    for map_entry in combined_map.get_values():
        flags = []
        if map_entry.fuzzy:
            flags.append('fuzzy')

        entry = polib.POEntry(
            msgctxt=map_entry.key,
            msgid=map_entry.original_msg,
            msgstr=map_entry.translated_msg,
            previous_msgid=map_entry.previous_original_msg,
            comment=map_entry.comment,
            flags=flags
        )
        entry = optimize_po_entry(entry)
        po.append(entry)

    return po


if __name__ == "__main__":
    main()
