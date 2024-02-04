# ==== input data ====
messages_pot_1 = """#
msgid ""
msgstr ""

msgctxt "context:"
msgid "msg 1"
msgstr ""

msgctxt "context:"
msgid "msg 2"
msgstr ""

msgctxt "unique_key_1"
msgid "unique msg 1"
msgstr ""

msgctxt "unique_key_2"
msgid "unique msg 2"
msgstr ""
"""

unknown_1 = """#
msgid ""
msgstr ""

msgctxt "context:"
msgid "unknown msg 1"
msgstr ""

msgctxt "context:"
msgid "unknown msg 2"
msgstr ""

msgctxt "unique_key_1"
msgid "unique msg 1"
msgstr ""

msgctxt "unique_key_2"
msgid "unique msg 2 modified"
msgstr ""
"""

expected_result_import_unknown_1 = """#
msgid ""
msgstr ""

msgctxt "context:"
msgid "msg 1"
msgstr ""

msgctxt "context:"
msgid "msg 2"
msgstr ""

msgctxt "context:"
msgid "unknown msg 1"
msgstr ""

msgctxt "context:"
msgid "unknown msg 2"
msgstr ""

msgctxt "unique_key_1"
msgid "unique msg 1"
msgstr ""

msgctxt "unique_key_2"
msgid "unique msg 2"
msgstr ""
"""
