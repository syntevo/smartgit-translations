import unittest
import sgpo
from test_import_unknown_data import *


class TestImportUnknown(unittest.TestCase):
    def test_import_unknown(self):
        pot = sgpo.pofile_from_text(messages_pot_1)
        unknown = sgpo.pofile_from_text(unknown_1)
        pot.import_unknown(unknown)
        pot.sort()
        print("\n======== New pot content ========\n")
        print(pot)
        content_as_string = pot.__unicode__()

        self.assertEqual(expected_result_import_unknown_1, content_as_string)
