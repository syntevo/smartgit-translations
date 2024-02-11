import os
import unittest

import sgpo
from path_finder import get_repository_root
from sgpo.sgpo import SgPo, Key_tuple


def get_test_data_dir() -> str:
    return os.path.join(get_repository_root(), "src", "tests", "data", "test_sgpo")


def get_test_data_path(*paths: str) -> str:
    return os.path.join(get_test_data_dir(), *paths)


class TestSgpo(unittest.TestCase):
    def test_init_sgpo(self):
        obj = SgPo()
        self.assertIsNotNone(obj)

    def test_from_file_sgpo(self):
        po_file = get_test_data_path('common', 'language.po')
        po = sgpo.pofile(po_file)
        print(f"\n{po}")
        self.assertIsNotNone(po)

    def test_from_text_sgpo(self):
        po_file = get_test_data_path('common', 'language.po')
        with open(po_file, 'r') as file:
            content = file.read()

        po = sgpo.pofile_from_text(content)
        print(f"\n{po}")
        self.assertIsNotNone(po)

    def test_find_by_key_sgpo_key_type1(self):
        po_file = get_test_data_path('common', 'language.po')
        po = sgpo.pofile(po_file)
        msgctxt = 'context:'
        msgid = 'msgid_2'
        expected_msgstr = 'msgstr_2'
        result = po.find_by_key(msgctxt, msgid)

        print(f"\n{result}")

        self.assertIsNotNone(result)
        self.assertEqual(expected_msgstr, result.msgstr)

    def test_find_by_key_sgpo_key_type2(self):
        po_file = get_test_data_path('common', 'language.po')
        po = sgpo.pofile(po_file)
        msgctxt = 'unique_key_2'
        msgid = 'unique_msgid_2'
        expected_msgstr = 'unique_msgstr_2'
        result = po.find_by_key(msgctxt, msgid)

        print(f"\n{result}")

        self.assertIsNotNone(result)
        self.assertEqual(expected_msgstr, result.msgstr)

    def test_sort_sgpo(self):
        normal_po_file = get_test_data_path('sort', 'normal_order.po')
        reverse_po_file = get_test_data_path('sort', 'reverse_order.po')

        po = sgpo.pofile(normal_po_file)
        po_reverse = sgpo.pofile(reverse_po_file)

        print("\nBefore:")
        print(po_reverse.get_key_list())
        print(po.get_key_list())
        self.assertNotEqual(po_reverse.get_key_list(), po.get_key_list())

        po_reverse.sort(reverse=False)

        print("\nAfter:")
        print(po_reverse.get_key_list())
        print(po.get_key_list())

        self.assertEqual(po_reverse.get_key_list(), po.get_key_list())

    def test_sort_sgpo_reverse(self):
        normal_po_file = get_test_data_path('sort', 'normal_order.po')
        reverse_po_file = get_test_data_path('sort', 'reverse_order.po')

        po = sgpo.pofile(normal_po_file)
        reverse_order_po = sgpo.pofile(reverse_po_file)

        print("\nBefore:")
        print(reverse_order_po.get_key_list())
        print(po.get_key_list())
        self.assertNotEqual(reverse_order_po.get_key_list(), po.get_key_list())

        po.sort(reverse=True)
        print("\nAfter:")
        print(reverse_order_po.get_key_list())
        print(po.get_key_list())
        self.assertEqual(reverse_order_po.get_key_list(), po.get_key_list())

    def test_format_sgpo_with_no_header_po(self):
        po_file = get_test_data_path('format', 'formatted.po')
        po_header_less_file = get_test_data_path('format', 'header_less.po')

        po = sgpo.pofile(po_file)
        header_less_po = sgpo.pofile(po_header_less_file)

        print(f"\n#### Before ####\n{header_less_po}")
        header_less_po.format()
        print(f"\n#### After ####\n{header_less_po}")

        self.assertEqual(po.__unicode__(), header_less_po.__unicode__())

    def test_format_sgpo_with_unnecessary_header_items(self):
        po_file = get_test_data_path('format', 'formatted.po')
        unnecessary_header_po_file = get_test_data_path('format', 'unnecessary_header.po')

        po = sgpo.pofile(po_file)
        unnecessary_header_po = sgpo.pofile(unnecessary_header_po_file)

        print(f"\n#### Before ####\n{unnecessary_header_po}")
        unnecessary_header_po.format()
        print(f"\n#### After ####\n{unnecessary_header_po}")

        self.assertEqual(po.__unicode__(), unnecessary_header_po.__unicode__())

    def test_format_sgpo_with_abnormal_header_order(self):
        po_file = get_test_data_path('format', 'formatted.po')
        abnormal_order_header_po_file = get_test_data_path('format', 'abnormal_order_header.po')
        po = sgpo.pofile(po_file)
        abnormal_order_header_po = sgpo.pofile(abnormal_order_header_po_file)

        print(f"\n#### Before ####\n{abnormal_order_header_po}")
        abnormal_order_header_po.format()
        print(f"\n#### After ####\n{abnormal_order_header_po}")

        self.assertEqual(po.__unicode__(), abnormal_order_header_po.__unicode__())

    def test_get_key_list_sgpo(self):
        pot = sgpo.pofile_from_text(get_key_list_test_data)
        result = pot.get_key_list()

        print(f"\n{result}")

        self.assertEqual(expected_key_list, result)

    def test_import_unknown_sgpo_case1(self):
        """
        No conflict between the pot file and the unknown file
        """
        pot_file = get_test_data_path('import_unknown', 'case_1_messages.pot')
        unknown_file = get_test_data_path('import_unknown', 'case_1_unknown.24_1')
        expected_result_file = get_test_data_path('import_unknown', 'case_1_expected_result.pot')

        pot = sgpo.pofile(pot_file)
        unknown = sgpo.pofile(unknown_file)
        expected_result = sgpo.pofile(expected_result_file)

        pot.import_unknown(unknown)
        pot.sort()
        print("\n======== New pot content ========\n")
        print(pot)

        self.assertEqual(expected_result.__unicode__(), pot.__unicode__())

    def test_import_unknown_sgpo_case2(self):
        """
        Conflicting entries between the pot file and the unknown file
        """
        pot_file = get_test_data_path('import_unknown', 'case_2_messages.pot')
        unknown_file = get_test_data_path('import_unknown', 'case_2_unknown.24_1')
        expected_result_file = get_test_data_path('import_unknown', 'case_2_expected_result.pot')

        pot = sgpo.pofile(pot_file)
        unknown = sgpo.pofile(unknown_file)
        expected_result = sgpo.pofile(expected_result_file)

        pot.import_unknown(unknown)
        pot.sort()
        print("\n======== New pot content ========\n")
        print(pot)

        self.assertEqual(expected_result.__unicode__(), pot.__unicode__())

    def test_import_unknown_sgpo_case3(self):
        """
        Conflicting entries between the pot file and the unknown file
        """
        pot_file = get_test_data_path('import_unknown', 'case_3_messages.pot')
        unknown_file = get_test_data_path('import_unknown', 'case_3_unknown.24_1')
        expected_result_file = get_test_data_path('import_unknown', 'case_3_expected_result.pot')

        pot = sgpo.pofile(pot_file)
        unknown = sgpo.pofile(unknown_file)
        expected_result = sgpo.pofile(expected_result_file)

        pot.import_unknown(unknown)
        pot.sort()
        print("\n======== New pot content ========\n")
        print(pot)

        self.assertEqual(expected_result.__unicode__(), pot.__unicode__())

    def test_import_mismatch_sgpo(self):
        pot_file = get_test_data_path('import_mismatch', 'case_1_messages.pot')
        mismatch_file = get_test_data_path('import_mismatch', 'case_1_mismatch.24_1')
        expected_result_file = get_test_data_path('import_mismatch', 'case_1_expected_result.pot')

        pot = sgpo.pofile(pot_file)
        mismatch = sgpo.pofile(mismatch_file)
        expected_result = sgpo.pofile(expected_result_file)

        pot.import_mismatch(mismatch)
        pot.sort()
        print("\n======== New pot content ========\n")
        print(pot)

        self.assertEqual(expected_result.__unicode__(), pot.__unicode__())

    def test_import_pot_sgpo_case1(self):
        """
        Only new entries are added.
        """
        pot_file = get_test_data_path('import_pot', 'case_1_messages.pot')
        po_file = get_test_data_path('import_pot', 'case_1_language.po')
        expected_result_file = get_test_data_path('import_pot', 'case_1_expected_result.po')

        pot = sgpo.pofile(pot_file)
        po = sgpo.pofile(po_file)
        expected_result = sgpo.pofile(expected_result_file)

        po.import_pot(pot)
        po.sort()
        print("\n======== New pot content ========\n")
        print(po)

        self.assertEqual(expected_result.__unicode__(), po.__unicode__())

    def test_import_pot_sgpo_case2(self):
        """
        Changes occurred in the original text (msgid)
        """
        pot_file = get_test_data_path('import_pot', 'case_2_messages.pot')
        po_file = get_test_data_path('import_pot', 'case_2_language.po')
        expected_result_file = get_test_data_path('import_pot', 'case_2_expected_result.po')

        pot = sgpo.pofile(pot_file)
        po = sgpo.pofile(po_file)
        expected_result = sgpo.pofile(expected_result_file)

        po.import_pot(pot)
        po.sort()
        print("\n======== New pot content ========\n")
        print(po)

        self.assertEqual(expected_result.__unicode__(), po.__unicode__())

    def test_import_pot_sgpo_case3(self):
        """
        The po contains entries that were deleted from the pot
        """
        pot_file = get_test_data_path('import_pot', 'case_3_messages.pot')
        po_file = get_test_data_path('import_pot', 'case_3_language.po')
        expected_result_file = get_test_data_path('import_pot', 'case_3_expected_result.po')

        pot = sgpo.pofile(pot_file)
        po = sgpo.pofile(po_file)
        expected_result = sgpo.pofile(expected_result_file)

        po.import_pot(pot)
        po.sort()
        print("\n======== New pot content ========\n")
        print(po)

        self.assertEqual(expected_result.__unicode__(), po.__unicode__())

    def test_delete_extracted_comments(self):
        pot_file = get_test_data_path('delete_extracted_comments', 'messages.pot')
        expected_result_file = get_test_data_path('delete_extracted_comments', 'expected_result.pot')
        pot = sgpo.pofile(pot_file)
        expected_result_pot = sgpo.pofile(expected_result_file)

        print("\n======== Input ========")
        print(pot)

        pot.delete_extracted_comments()
        print("\n======== Output ========")
        print(pot)

        self.assertEqual(expected_result_pot.__unicode__(), pot.__unicode__())


# ====== Test data ====
get_key_list_test_data = r"""#
msgctxt "context:"
msgid "msgid_1"
msgstr ""

msgctxt "context:"
msgid "msgid_2"
msgstr ""

msgctxt "unique_key_1"
msgid "unique_msgid_1"
msgstr ""

msgctxt "unique_key_2"
msgid "unique_msgid_2"
msgstr ""
"""

expected_key_list = [Key_tuple(msgctxt='context:', msgid='msgid_1'),
                     Key_tuple(msgctxt='context:', msgid='msgid_2'),
                     Key_tuple(msgctxt='unique_key_1', msgid=None),
                     Key_tuple(msgctxt='unique_key_2', msgid=None)]
