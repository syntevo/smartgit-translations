# SmartGit Localization - SmartGit Translation Files

This repository contains translation files for the Git client SmartGit:

https://www.syntevo.com/smartgit/download/

# How does SmartGit's localization work?

SmartGit includes various UI texts ('strings') directly in its source code. Many of these strings are dynamically composed. Major UI components are assigned keys, which are used to search for translations from localization files.
The `./po` directory contains a `messages.pot` file ('master mapping') which includes all currently known keys and their original English texts. Localization files for all currently supported locales, named `<locale_code>.po`, contain similar keys and original texts, along with their translations (or are yet to be translated).

The 'master mapping' is updated by us from the SmartGit source at regular intervals. `<locale_code>.po` files are primarily updated by contributors and then synchronized with the SmartGit source by us.

The translations for the latest Preview release are managed in the `master` branch, and each stable version of SmartGit has its separate branch, like `smartgit-23.1`.

> [!NOTE] 
> Starting with SmartGit 24.1, we have migrated the format of localization files to one of the de facto standard formats, the PO file format. For previous versions, please refer to the README.md of each version's branch.

# How to contribute?

You can contribute to the localization of SmartGit in two ways:

* **Help to translate**: add/improve translations in your language's `<locale_code>.po` file
* **Help to collect**: collect not yet known keys to populate the master mapping

## Preparation

### Clone the Repository

In either case, you'll need to fork and clone this repository, ensuring you're on the appropriate branch:

1. Use the latest release or the current preview version of SmartGit
1. Fork the repository
1. Clone your fork, e.g. to `C:\temp\smartgit-translations.git`
1. Checkout the appropriate branch:
   1. `master` contains translations for the current Preview version
   1. `smartgit-...` contains translations for the corresponding SmartGit version

> [!IMPORTANT]
> Please only send pull requests for one of these two versions. 

### Enable Viewing Translation Results in the Actual GUI

This is not mandatory for translation-only contributions, but it enables you to work while checking how your translations appear in the actual GUI.

1. Open SmartGit's configuration directory. (Help -> About SmartGit, Information Tab)
1. Exit SmartGit. (Repository -> Exit)
1. Find `smartgit.properties` in the configuration directory and add the following lines:
   ```
   smartgit.i18n=<locale>
   smartgit.debug.i18n.development=<path-to-localization-directory>
   ```
   Set `<locale>` to one of the locales like `zh_CN`, `ja_JP`.

   For example, if the repository is cloned to the location shown and you are translating for the `zh_CN` locale, it would look like this:
   ```
   smartgit.i18n=zh_CN
   smartgit.debug.i18n.development=C\:/temp/smartgit-translations.git/po
   ```

`smartgit.properties` also has options to display marks on UI elements of the GUI with untranslated sections or unknown keys, which is especially useful for key collection, so activate it as needed.
For more details, refer to [About smartgit.properties](docs/about_smartgit_properties.md).

> [!IMPORTANT]
> This setting is mandatory when collecting keys.

### Prepare Your Editor

For translating po files, a basic text editor is possible, but you may find translation support tools like the following convenient. Use whichever tool you prefer:

* [Poedit](https://poedit.net)
* [Virtaal](https://virtaal.translatehouse.org)
* [Lokalize](https://apps.kde.org/lokalize/)

## Contributing to Translation

All new translations are welcome! To contribute, please follow these steps:

### If Using a Text Editor

1. Prepare as described above
1. Check pending pull requests to see which translations are in progress

1. Review the contents of `<locale_code>.po` to find the text to translate.

1. Translate the text.
   Here's an example entry to explain:
   ```
   msgctxt "(wndLog|wndProject).lblStatusBarMessage:"
   msgid "Please wait ..."
   msgstr ""
   ```
   In po files, `msgctxt` is a string for identifying context, `msgid` serves as both the key and original text, and the translated message is written in `msgstr`.
   In SmartGit, every entry has a `msgctxt` and `msgid`, which are used internally as the key.
 
1. Write your translated message in `msgstr`.
   ```
   msgctxt "(wndLog|wndProject).lblStatusBarMessage:"
   msgid "Please wait ..."
   msgstr "请稍等..."
   ```

1. Send a pull request with a prefix like `Chinese translation update: ` (or the appropriate language name)

> [!IMPORTANT]
> Ensure your pull request does not include unnecessary changes like end-of-line alterations (e.g., newline) or reordering (entry are automatically sorted by us).

#### Syntax Details

##### Untranslated Entries

Below is an example of an untranslated entry. Entries where `msgstr` is an empty string.

```
msgctxt "(wndLog|wndProject).lblStatusBarMessage:"
msgid "Please wait ..."
msgstr ""
```
#### Entries That Do Not Require Translation

For items that should remain as the original text, like product names, set `msgstr` to the same string as `msgid`.

```
msgctxt "dlgSgHostingProviderEdit.tle:"
msgid "GitHub"
msgstr "GitHub"
```

#### Entries That Require Verification or Modification

Entries deemed to need verification for some reason are tagged with the `fuzzy` flag.
Also, entries whose original text has changed will have the previous original text written in a comment line starting with `#| msgid`.
Review the content and adjust `msgstr` as needed.

```
#, fuzzy
#| msgid "Edit the effective repository settings"
msgctxt "dlgSgRepositorySettings.hdl"
msgid "Edit the repository settings"
msgstr "编辑有效的仓库设置"
```

Once verification or modification is complete, remove the 'fuzzy' flag and the previous original text line.
```
msgctxt "dlgSgRepositorySettings.hdl"
msgid "Edit the repository settings"
msgstr "编辑仓库设置"
```

### If Using Translation Support Software (Example with Poedit)

1. Prepare as described above
1. Check pending pull requests to see which translations are in progress
1. Open Poedit and set it not to wrap words.
1. Open `<locale_code>.po` and proceed with the translation.
1. In Poedit, 'Needs work' corresponds to the 'fuzzy' flag in the file. Remove the flag once verified.
1. Check the file differences, and revert any changes made to the header by Poedit. 
1. Send a pull request with a prefix like `Chinese translation update: ` (or the appropriate language name)

> [!IMPORTANT]
> * To avoid conflicts due to unnecessary changes, always revert header changes before committing.
> * Change your editor settings not to wrap words.
>   * In Poedit, go to File -> Preferences..., open the Advanced tab, and turn on 'Preserving formatting of existing files'.
>   * If word wrapping has changed, turn off 'Preserving formatting of existing files' and set 'Wrap at' to a sufficiently large value like 1000, then save the po file over it.

## Contributing to Key Collection

Since SmartGit dynamically generates texts, the master mapping does not include *all* keys, only those *currently known* to us and contributors collected. To help collect keys:

1. Prepare as described above (enable viewing translation results in the actual GUI).
1. Restart SmartGit.
1. SmartGit will create several new files in the specified `development` directory. The most important ones are:
   1. `unknown.*`, containing yet unknown keys, i.e., keys without a matching entry in the master mapping file
   1. `mismatch.*`, containing already known keys with differences in the original text between the code and master mapping file.
   1. These two files are yours to ignore, hence 'you own them'.
1. Shut down SmartGit.
1. Occasionally check two files, compress them, and send them to `smartgit@syntevo.com`
   1. Prefix your email with "Language mappings: new/changed keys"
1. **Delete all two files**, to start collecting new keys again
1. Restart SmartGit and continue collecting new keys

## Contributing through Review

We need reviews by native speakers of each language.
Pending pull requests and existing translations in `mapping.dev` may sometimes need refinement.
We welcome review comments and suggestions for improving existing translations!
