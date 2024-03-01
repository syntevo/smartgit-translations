import unittest

from sgv23_mapping import SgMap


class TestSgMap(unittest.TestCase):
    def test_standard_entry(self):
        test_data = ("entry1_key=entry1_value\n"
                     "entry2_key=entry2_value\n"
                     "entry3_key=entry3_value\n"
                     )

        test_map = SgMap.from_text(test_data, 'en_US')
        map_dict = test_map.get_dictionary()

        entry1 = map_dict.get('entry1_key', None)
        self.assertIsNotNone(entry1)
        self.assertEqual('entry1_value', entry1.value)
        self.assertEqual('', entry1.comment)
        self.assertFalse(entry1.no_translation_needed)

        entry2 = map_dict.get('entry2_key', None)
        self.assertIsNotNone(entry2)
        self.assertEqual('entry2_value', entry2.value)
        self.assertEqual('', entry2.comment)
        self.assertFalse(entry2.no_translation_needed)

        entry3 = map_dict.get('entry3_key', None)
        self.assertIsNotNone(entry3)
        self.assertEqual('entry3_value', entry3.value)
        self.assertEqual('', entry3.comment)
        self.assertFalse(entry3.no_translation_needed)

    def test_standard_entry_with_comment(self):
        test_data = ("entry1_key=entry1_value\n"
                     "entry2_key=entry2_value\n"
                     "# entry2_comment\n"
                     "entry3_key=entry3_value\n"
                     )

        test_map = SgMap.from_text(test_data, 'en_US')
        map_dict = test_map.get_dictionary()

        entry1 = map_dict.get('entry1_key', None)
        self.assertIsNotNone(entry1)
        self.assertEqual('entry1_value', entry1.value)
        self.assertEqual('', entry1.comment)
        self.assertFalse(entry1.no_translation_needed)

        entry2 = map_dict.get('entry2_key', None)
        self.assertIsNotNone(entry2)
        self.assertEqual('entry2_value', entry2.value)
        self.assertEqual('entry2_comment', entry2.comment)
        self.assertFalse(entry2.no_translation_needed)

        entry3 = map_dict.get('entry3_key', None)
        self.assertIsNotNone(entry3)
        self.assertEqual('entry3_value', entry3.value)
        self.assertEqual('', entry3.comment)
        self.assertFalse(entry3.no_translation_needed)

    def test_untranslated_entries(self):
        test_data = ("entry1_key=entry1_value\n"
                     "entry2_key=\n"
                     "#         !=entry2_value(original)\n"
                     "entry3_key=entry3_value\n"
                     )

        test_map = SgMap.from_text(test_data, 'en_US')
        map_dict = test_map.get_dictionary()

        entry1 = map_dict.get('entry1_key', None)
        self.assertIsNotNone(entry1)
        self.assertEqual('entry1_value', entry1.value)
        self.assertEqual('', entry1.comment)
        self.assertFalse(entry1.no_translation_needed)

        entry2 = map_dict.get('entry2_key', None)
        self.assertIsNotNone(entry2)
        self.assertEqual('', entry2.value)
        self.assertEqual('!=entry2_value(original)', entry2.comment)
        self.assertFalse(entry2.no_translation_needed)

        entry3 = map_dict.get('entry3_key', None)
        self.assertIsNotNone(entry3)
        self.assertEqual('entry3_value', entry3.value)
        self.assertEqual('', entry3.comment)
        self.assertFalse(entry3.no_translation_needed)

    def test_no_translation_entry(self):
        test_data = ("entry1_key=entry1_value\n"
                     "entry2_key==entry2_value\n"
                     "entry3_key=entry3_value\n"
                     )

        test_map = SgMap.from_text(test_data, 'en_US')
        map_dict = test_map.get_dictionary()

        entry1 = map_dict.get('entry1_key', None)
        self.assertIsNotNone(entry1)
        self.assertEqual('entry1_value', entry1.value)
        self.assertEqual('', entry1.comment)
        self.assertFalse(entry1.no_translation_needed)

        entry2 = map_dict.get('entry2_key', None)
        self.assertIsNotNone(entry2)
        self.assertEqual('entry2_value', entry2.value)
        self.assertEqual('', entry2.comment)
        self.assertTrue(entry2.no_translation_needed)

        entry3 = map_dict.get('entry3_key', None)
        self.assertIsNotNone(entry3)
        self.assertEqual('entry3_value', entry3.value)
        self.assertEqual('', entry3.comment)
        self.assertFalse(entry3.no_translation_needed)

    def test_split_line_entry(self):
        test_data = ("entry1_key=entry1_value\n"
                     "entry2_key=\\\n"
                     " entry2_value\n"
                     "entry3_key=entry3_value\n"
                     )

        test_map = SgMap.from_text(test_data, 'en_US')
        map_dict = test_map.get_dictionary()

        entry1 = map_dict.get('entry1_key', None)
        self.assertIsNotNone(entry1)
        self.assertEqual('entry1_value', entry1.value)

        entry2 = map_dict.get('entry2_key', None)
        self.assertIsNotNone(entry2)
        self.assertEqual('entry2_value', entry2.value)

        entry3 = map_dict.get('entry3_key', None)
        self.assertIsNotNone(entry3)
        self.assertEqual('entry3_value', entry3.value)
    def test_split_line_entry2(self):
        test_data = ("entry1_key=entry1_value\n"
                     "entry2_key=\\\n"
                     "entry2_value\n"
                     "entry3_key=entry3_value\n"
                     )

        test_map = SgMap.from_text(test_data, 'en_US')
        map_dict = test_map.get_dictionary()

        entry1 = map_dict.get('entry1_key', None)
        self.assertIsNotNone(entry1)
        self.assertEqual('entry1_value', entry1.value)

        entry2 = map_dict.get('entry2_key', None)
        self.assertIsNotNone(entry2)
        self.assertEqual('entry2_value', entry2.value)

        entry3 = map_dict.get('entry3_key', None)
        self.assertIsNotNone(entry3)
        self.assertEqual('entry3_value', entry3.value)

    def test_key_contains_escape_sequence(self):
        test_data = ("entry1_key=entry1_value\n"
                     "entry2\\=key=entry2_value\n"
                     "entry3_key=entry3_value\n"
                     )

        test_map = SgMap.from_text(test_data, 'en_US')
        map_dict = test_map.get_dictionary()

        entry1 = map_dict.get('entry1_key', None)
        self.assertIsNotNone(entry1)
        self.assertEqual('entry1_value', entry1.value)

        entry2 = map_dict.get('entry2\\=key', None)
        self.assertIsNotNone(entry2)
        self.assertEqual('entry2_value', entry2.value)

        entry3 = map_dict.get('entry3_key', None)
        self.assertIsNotNone(entry3)
        self.assertEqual('entry3_value', entry3.value)

    def test_header_comment(self):
        test_data = ("# header comment1\n"
                     "# header comment2\n"
                     "entry1_key=entry1_value\n"
                     "# entry1_comment\n"
                     )

        test_map = SgMap.from_text(test_data, 'en_US')
        map_dict = test_map.get_dictionary()

        entry1 = map_dict.get('entry1_key', None)
        self.assertIsNotNone(entry1)
        self.assertEqual('entry1_value', entry1.value)
        self.assertEqual('entry1_comment', entry1.comment)
        self.assertFalse(entry1.no_translation_needed)


if __name__ == '__main__':
    unittest.main()
