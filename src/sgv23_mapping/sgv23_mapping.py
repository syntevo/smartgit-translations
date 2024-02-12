#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This module reads the SmartGit mapping file and returns a list of namedtuple containing key-value pairs.
"""
import os
from collections import namedtuple
from typing import Dict, List, Tuple

from pyparsing import (CharsNotIn, restOfLine, LineEnd, Suppress, Group, ZeroOrMore, OneOrMore, StringEnd,
                       ParseException, Combine, Literal, MatchFirst, White, Optional)


# The following class is intended only to clarify the fields of namedtuple and does nothing else.
class ParsedEntry(namedtuple('ParsedEntry', ['key', 'value', 'comment', 'no_translation_needed'])):
    """
    This namedtuple has the following items.

    key  :str
    value  :str
    comment  :str
    no_translation_needed :bool
    """
    pass


class CombinedEntry(namedtuple('CombinedEntry',
                               ['key', 'original_msg', 'translated_msg', 'comment', 'fuzzy', 'no_translation_needed',
                                'previous_original_msg', 'previous_translated_msg'])):
    """
    This namedtuple has the following items.

    key:  str
    original_msg:  str
    translated_msg:  str
    comment:  str
    fuzzy:  bool
    no_translation_needed:  bool
    previous_original_msg:  str
    previous_translated_msg:  str
    """
    pass


class SgMap:
    """This class reads the SmartGit 23.1 mapping file

    Initialize by one of the following methods
      sg_map_instance = SgMap(<File path>,<locale_code>)
      sg_map_instance = SgMap.from_file(<File content>,<locale_code>)

    <locale_code> is a combination of ISO 639 two-letter language code (lowercase) and ISO 3166 two-letter country(region) code (uppercase).
    For example: zh_CN

    The initialized class will hold a Key-Value pair of type Dict.
    Value is a namedtuple of type 'ParsedEntry'.
    """

    def __init__(self, file_path: str, locale_code: str) -> None:
        self.dictionary: Dict[str, ParsedEntry] = self._validate_and_read_file(file_path)
        self.locale_code = locale_code

    @classmethod
    def from_text(cls, text_data: str, locale_code: str):
        """Generates and initializes objects from text data
        """
        instance = cls.__new__(cls)
        instance.dictionary = instance._read_text(text_data)
        instance.locale_code = locale_code
        return instance

    def get_key_list(self) -> List[str]:
        return list(self.dictionary.keys())

    def get_values(self):
        return self.dictionary.values()

    def get_dictionary(self) -> Dict[str, ParsedEntry]:
        """
        The value of a dictionary contains the following elements
        key,value,comment,no_translation_needed
        """
        return self.dictionary

    def export_to_tsv(self, output_file: str) -> None:
        with open(output_file, "w", encoding="UTF-8", newline="\n") as file:
            file.write("key\tvalue\tcomment\tspecial_flag\n")
            item_count = 1
            for entry in self.dictionary.values():
                file.write(f"{item_count}\t{entry.key}\t{entry.value}\t{entry.no_translation_needed}\n")
                item_count = item_count + 1

    def _validate_and_read_file(self, file_path: str):
        if not file_path:
            raise ValueError("File path cannot be None")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        return self._read_file(file_path)

    def _read_file(self, input_file: str) -> Dict[str, ParsedEntry]:
        with open(input_file, "r", encoding="UTF-8") as file:
            file_content = file.read()
        return self._read_text(file_content)

    def _read_text(self, text: str) -> Dict[str, ParsedEntry]:
        entries = list(self._parse_content(text))
        # Returns parsed results in Dict type.
        return {entry.key: entry for entry in entries}

    @staticmethod
    def _create_parser():

        equals = MatchFirst([
            Literal('=\\').setResultsName('split_line_operator') + LineEnd() + Optional(White()),
            Literal('==').setResultsName('double_equals'),
            Literal('=').setResultsName('single_equal')
        ])

        # Define key content
        key_characters = CharsNotIn('=', exact=1)
        escaped_equal = Literal('\\=')
        key_content = Combine(ZeroOrMore(escaped_equal | key_characters))

        # Define value
        value = restOfLine

        # Define comment
        comment_prefix = Suppress('#')
        comment = Group(comment_prefix + White() + restOfLine('comment'))

        # Define key-value pair
        key_value_pair = Group(key_content('key') + equals + value('value') + LineEnd())

        parser = OneOrMore(comment | key_value_pair) + StringEnd()

        return parser

    def _parse_content(self, file_content):
        parser = self._create_parser()

        try:
            output_entry = None

            parsed_items = list(parser.parseString(file_content))
            for single_item in parsed_items:
                if 'comment' in single_item:

                    if output_entry:
                        output_entry = output_entry._replace(comment=single_item.comment)
                        yield output_entry
                        output_entry = None

                else:
                    # If the item is a Key-Value pair
                    if output_entry:
                        yield output_entry

                    key = single_item.key
                    value = single_item.value

                    # <key>==<value> indicates that no translation is needed.
                    no_translation_needed = 'double_equals' in single_item

                    # For items with no translation, the parser returns value=None,
                    # Since value is assumed to be a str, it is set to an empty string.
                    if value is None:
                        value = ''

                    output_entry = ParsedEntry(
                        key=key, value=value, comment='', no_translation_needed=no_translation_needed)

            if output_entry:
                yield output_entry

        except ParseException as pe:
            print("Parsing failed:", pe)

    def print_entries(self):
        item_count = 0
        for entry in self.dictionary.values():
            item_count += 1
            entry_text = (f'#{format(item_count, "04d")}\t{entry.key}\n'
                          f'\tValue: {entry.value}\n'
                          f'\tComment: {entry.comment}\n'
                          f'\tNo translation needed:{entry.no_translation_needed}')
            print(entry_text)

    @property
    def number_of_entries(self) -> int:
        return len(self.dictionary)


class CombinedSgMap:
    def __init__(self, master_map: SgMap, locale_map: SgMap, state_map: SgMap = None):
        self.dictionary = self._combine_entries(master_map, locale_map, state_map)
        self.locale_code = locale_map.locale_code

    def get_dictionary(self):
        return self.dictionary

    def get_values(self) -> list[CombinedEntry]:
        return list(self.dictionary.values())

    @staticmethod
    def _determine_comment(master_entry: ParsedEntry, locale_entry: ParsedEntry) -> str:
        if (locale_entry.comment.startswith('!=')) and (locale_entry.comment[2:] == master_entry.value):
            comment = ''
        else:
            comment = locale_entry.comment

        return comment

    @staticmethod
    def _determine_previous_original_msg(master_entry: ParsedEntry, locale_entry: ParsedEntry,
                                         state_entry: ParsedEntry) -> str:
        if (state_entry.value != '') and (state_entry.value != master_entry.value):
            previous_original_msg = state_entry.value
        else:
            previous_original_msg = None
        if locale_entry.value == '':
            previous_original_msg = None

        return previous_original_msg

    @staticmethod
    def _get_map_entry_tuple(key: str, master_map: SgMap, locale_map: SgMap, state_map: SgMap) \
            -> Tuple[ParsedEntry, ParsedEntry, ParsedEntry]:

        master_entry = master_map.dictionary[key]
        locale_entry = locale_map.dictionary.get(key, None)
        state_entry = state_map.dictionary.get(key, None)

        if locale_entry is None:
            locale_entry = master_entry
            locale_entry = locale_entry._replace(value="")
        if state_entry is None:
            state_entry = master_entry

        return master_entry, locale_entry, state_entry

    @staticmethod
    def _combine_entries(master_map: SgMap, locale_map: SgMap, state_map: SgMap = None):

        if state_map is None:
            state_map = master_map

        combined_dict = {}
        for key in master_map.get_key_list():
            master_entry, locale_entry, state_entry = \
                CombinedSgMap._get_map_entry_tuple(key, master_map, locale_map, state_map)

            comment = \
                CombinedSgMap._determine_comment(master_entry, locale_entry)

            previous_original_msg = \
                CombinedSgMap._determine_previous_original_msg(master_entry, locale_entry, state_entry)

            fuzzy = False
            if previous_original_msg is not None:
                fuzzy = True
            elif locale_entry.comment != '':
                fuzzy = True
            if locale_entry.value == '':
                fuzzy = False

            combined_entry = CombinedEntry(key=key,
                                           original_msg=master_entry.value,
                                           translated_msg=locale_entry.value,
                                           comment=comment,
                                           no_translation_needed=locale_entry.no_translation_needed,
                                           fuzzy=fuzzy,
                                           previous_original_msg=previous_original_msg,
                                           previous_translated_msg=''
                                           )
            combined_dict[key] = combined_entry

        return combined_dict
