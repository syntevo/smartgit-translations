import unittest

from locale2po import CombinedSgMap_to_po
from sgpo_common import *
from sgv23_mapping import SgMap, CombinedSgMap


def create_combined_sg_map(master_str: str, locale_str: str, state_str: str, locale_code: str) -> CombinedSgMap:
    master_map = SgMap.from_text(master_str, 'en_US')
    locale_map = SgMap.from_text(locale_str, locale_code)
    state_map = SgMap.from_text(state_str, locale_code)
    return CombinedSgMap(master_map, locale_map, state_map)


def find_po_entry(po: polib.POFile, msgctxt: str, msgid: str) -> polib.POEntry:
    for entry in po:
        if entry.msgctxt == msgctxt and entry.msgid == msgid:
            return entry
    return None


class TestCombinedSgMapToPoFile(unittest.TestCase):
    def test_untranslated_entry(self):
        combined_map = create_combined_sg_map(master, locale_1, state_1, 'zh_CN')
        po = CombinedSgMap_to_po(combined_map)
        num_of_untranslated_entries = len(po.untranslated_entries())
        num_of_translated_entries = len(po.translated_entries())
        num_of_fuzzy_entries = len(po.fuzzy_entries())

        self.assertEqual(1, num_of_untranslated_entries)
        self.assertEqual(0, num_of_translated_entries)
        self.assertEqual(0, num_of_fuzzy_entries)

        entry = find_po_entry(po, 'dlgQFrameManagerExit.hdl', 'Do you really want to exit SmartGit?')
        self.assertIsNotNone(entry)

        self.assertEqual('dlgQFrameManagerExit.hdl', entry.msgctxt)
        self.assertEqual('Do you really want to exit SmartGit?', entry.msgid)
        self.assertEqual('', entry.msgstr)
        self.assertEqual('', entry.comment)
        self.assertIsNone(entry.previous_msgid)

        # fuzzy=false because it is obvious that work is needed on untranslated entry.
        self.assertFalse(entry.fuzzy)
        print(po)

    def test_translated_entry_with_comment(self):
        combined_map = create_combined_sg_map(master, locale_2, state_1, 'zh_CN')
        po = CombinedSgMap_to_po(combined_map)
        num_of_untranslated_entries = len(po.untranslated_entries())
        num_of_translated_entries = len(po.translated_entries())
        num_of_fuzzy_entries = len(po.fuzzy_entries())

        self.assertEqual(0, num_of_untranslated_entries)
        self.assertEqual(0, num_of_translated_entries)
        self.assertEqual(1, num_of_fuzzy_entries)

        entry = find_po_entry(po, 'dlgQFrameManagerExit.hdl', 'Do you really want to exit SmartGit?')
        self.assertIsNotNone(entry)

        self.assertEqual('dlgQFrameManagerExit.hdl', entry.msgctxt)
        self.assertEqual('Do you really want to exit SmartGit?', entry.msgid)
        self.assertEqual('是否确定要退出 SmartGit ？', entry.msgstr)
        self.assertEqual('', entry.comment)
        self.assertIsNone(entry.previous_msgid)

        # fuzzy = True because the comment line in mapping.dev have not been removed.
        self.assertTrue(entry.fuzzy)
        print(po)

    def test_translated_entry(self):
        combined_map = create_combined_sg_map(master, locale_3, state_1, 'zh_CN')
        po = CombinedSgMap_to_po(combined_map)
        num_of_untranslated_entries = len(po.untranslated_entries())
        num_of_translated_entries = len(po.translated_entries())
        num_of_fuzzy_entries = len(po.fuzzy_entries())

        self.assertEqual(0, num_of_untranslated_entries)
        self.assertEqual(1, num_of_translated_entries)
        self.assertEqual(0, num_of_fuzzy_entries)

        entry = find_po_entry(po, 'dlgQFrameManagerExit.hdl', 'Do you really want to exit SmartGit?')
        self.assertIsNotNone(entry)

        self.assertEqual('dlgQFrameManagerExit.hdl', entry.msgctxt)
        self.assertEqual('Do you really want to exit SmartGit?', entry.msgid)
        self.assertEqual('是否确定要退出 SmartGit ？', entry.msgstr)
        self.assertEqual('', entry.comment)
        self.assertIsNone(entry.previous_msgid)
        self.assertFalse(entry.fuzzy)
        print(po)

    def test_translated_entry_with_unexpected_comment(self):
        combined_map = create_combined_sg_map(master, locale_4, state_1, 'zh_CN')
        po = CombinedSgMap_to_po(combined_map)
        num_of_untranslated_entries = len(po.untranslated_entries())
        num_of_translated_entries = len(po.translated_entries())
        num_of_fuzzy_entries = len(po.fuzzy_entries())

        self.assertEqual(0, num_of_untranslated_entries)
        self.assertEqual(0, num_of_translated_entries)
        self.assertEqual(1, num_of_fuzzy_entries)

        entry = find_po_entry(po, 'dlgQFrameManagerExit.hdl', 'Do you really want to exit SmartGit?')
        self.assertIsNotNone(entry)

        self.assertEqual('dlgQFrameManagerExit.hdl', entry.msgctxt)
        self.assertEqual('Do you really want to exit SmartGit?', entry.msgid)
        self.assertEqual('是否确定要退出 SmartGit ？', entry.msgstr)
        self.assertEqual('!=foo', entry.comment)
        self.assertIsNone(entry.previous_msgid)
        self.assertTrue(entry.fuzzy)
        print(po)

    def test_untranslated_entry_with_original_modified(self):
        combined_map = create_combined_sg_map(master, locale_1, state_2, 'zh_CN')
        po = CombinedSgMap_to_po(combined_map)
        num_of_untranslated_entries = len(po.untranslated_entries())
        num_of_translated_entries = len(po.translated_entries())
        num_of_fuzzy_entries = len(po.fuzzy_entries())

        self.assertEqual(1, num_of_untranslated_entries)
        self.assertEqual(0, num_of_translated_entries)
        self.assertEqual(0, num_of_fuzzy_entries)

        entry = find_po_entry(po, 'dlgQFrameManagerExit.hdl', 'Do you really want to exit SmartGit?')
        self.assertIsNotNone(entry)

        self.assertEqual('dlgQFrameManagerExit.hdl', entry.msgctxt)
        self.assertEqual('Do you really want to exit SmartGit?', entry.msgid)
        self.assertEqual('', entry.msgstr)
        self.assertEqual('', entry.comment)
        self.assertIsNone(entry.previous_msgid)
        self.assertFalse(entry.fuzzy)
        print(po)

    def test_translated_entry_with_comment_and_original_modified(self):
        combined_map = create_combined_sg_map(master, locale_2, state_2, 'zh_CN')
        po = CombinedSgMap_to_po(combined_map)
        num_of_untranslated_entries = len(po.untranslated_entries())
        num_of_translated_entries = len(po.translated_entries())
        num_of_fuzzy_entries = len(po.fuzzy_entries())

        self.assertEqual(0, num_of_untranslated_entries)
        self.assertEqual(0, num_of_translated_entries)
        self.assertEqual(1, num_of_fuzzy_entries)

        entry = find_po_entry(po, 'dlgQFrameManagerExit.hdl', 'Do you really want to exit SmartGit?')
        self.assertIsNotNone(entry)

        self.assertEqual('dlgQFrameManagerExit.hdl', entry.msgctxt)
        self.assertEqual('Do you really want to exit SmartGit?', entry.msgid)
        self.assertEqual('是否确定要退出 SmartGit ？', entry.msgstr)
        self.assertEqual('', entry.comment)
        self.assertEqual('Do you want to exit SmartGit?', entry.previous_msgid)
        self.assertTrue(entry.fuzzy)
        print(po)

    def test_translated_entry_with_original_modified(self):
        combined_map = create_combined_sg_map(master, locale_3, state_2, 'zh_CN')
        po = CombinedSgMap_to_po(combined_map)
        num_of_untranslated_entries = len(po.untranslated_entries())
        num_of_translated_entries = len(po.translated_entries())
        num_of_fuzzy_entries = len(po.fuzzy_entries())

        self.assertEqual(0, num_of_untranslated_entries)
        self.assertEqual(0, num_of_translated_entries)
        self.assertEqual(1, num_of_fuzzy_entries)

        entry = find_po_entry(po, 'dlgQFrameManagerExit.hdl', 'Do you really want to exit SmartGit?')
        self.assertIsNotNone(entry)

        self.assertEqual('dlgQFrameManagerExit.hdl', entry.msgctxt)
        self.assertEqual('Do you really want to exit SmartGit?', entry.msgid)
        self.assertEqual('是否确定要退出 SmartGit ？', entry.msgstr)
        self.assertEqual('', entry.comment)
        self.assertEqual('Do you want to exit SmartGit?', entry.previous_msgid)
        self.assertTrue(entry.fuzzy)
        print(po)

    def test_translated_entry_with_unexpected_comment_and_original_modified(self):
        combined_map = create_combined_sg_map(master, locale_4, state_2, 'zh_CN')
        po = CombinedSgMap_to_po(combined_map)
        num_of_untranslated_entries = len(po.untranslated_entries())
        num_of_translated_entries = len(po.translated_entries())
        num_of_fuzzy_entries = len(po.fuzzy_entries())

        self.assertEqual(0, num_of_untranslated_entries)
        self.assertEqual(0, num_of_translated_entries)
        self.assertEqual(1, num_of_fuzzy_entries)

        entry = find_po_entry(po, 'dlgQFrameManagerExit.hdl', 'Do you really want to exit SmartGit?')
        self.assertIsNotNone(entry)

        self.assertEqual('dlgQFrameManagerExit.hdl', entry.msgctxt)
        self.assertEqual('Do you really want to exit SmartGit?', entry.msgid)
        self.assertEqual('是否确定要退出 SmartGit ？', entry.msgstr)
        self.assertEqual('!=foo', entry.comment)
        self.assertEqual('Do you want to exit SmartGit?', entry.previous_msgid)
        self.assertTrue(entry.fuzzy)
        print(po)


# ======================= Test Data =======================

master = r"""
dlgQFrameManagerExit.hdl=Do you really want to exit SmartGit?
"""

# Untranslated item
locale_1 = r"""
dlgQFrameManagerExit.hdl=
#                        !=Do you really want to exit SmartGit?
"""

# Translated item with comment (Item needs check)
locale_2 = r"""
dlgQFrameManagerExit.hdl=是否确定要退出 SmartGit ？
#                        !=Do you really want to exit SmartGit?
"""

# Translated item
locale_3 = r"""
dlgQFrameManagerExit.hdl=是否确定要退出 SmartGit ？
"""

# Translated item with unexpected comment
locale_4 = r"""
dlgQFrameManagerExit.hdl=是否确定要退出 SmartGit ？
#                      !=foo
"""

# equal master mapping
state_1 = r"""
dlgQFrameManagerExit.hdl=Do you really want to exit SmartGit?
"""

# master mapping modified
state_2 = r"""
dlgQFrameManagerExit.hdl=Do you want to exit SmartGit?
"""

if __name__ == '__main__':
    unittest.main()
