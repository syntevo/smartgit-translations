# SmartGit Localization - SmartGit Translation Files

This repository contains translation files for the Git client SmartGit:

https://www.syntevo.com/smartgit/download/

# How does SmartGit's localization work?

SmartGit contains the various UI texts ('strings') directly in the source code. Many of these strings are dynamically composed. The main UI components have keys assigned which are used to look up translations from mapping files. The root `mapping` file ('master mapping') contains all currently known keys with their original, English texts. For all currently supported locales, corresponding sub-directories contain mapping files with appropriate translations:

* `mapping_dev.*` contains translations for all keys (not yet translated texts will show up in English)
* `mapping_todo_new.*` contains only not yet translated texts (with their original English text); this file is auto-generated and only present to make looking up missing translations easier

The master mapping will be updated by us from SmartGit sources in regular intervals. `mapping_dev.*` will be updated by contributers and synchronized back by us to SmartGit sources.

For every SmartGit version, there is a separate branch, like `smartgit-20.2`.

# How to contribute?

You can contribute to the localization of SmartGit in two ways:

* **Help to translate**: translate not yet translated texts from `mapping_todo_new.*` language mappings
* **Help to collect**: collect not yet known keys to populate the master mapping

## Preparations

In either case, you have to fork and clone this repository and ensure that you are in the correct branch:

1. Be sure to use the latest released or the current preview version of SmartGit
1. Fork the repository
1. Clone your fork, e.g. to `C:\temp\smartgit-translations.git`
1. Checkout the appropriate branch:
   1. `master` contains translations for the current Preview version
   1. `smartgit-...` contains translations for the corresponding SmartGit version

> **Note!** Please only send pull requests for one of these two versions.

## Help to translate

All keys in `mapping_todo_new.*` need translation and every single new translation is welcome!

1. Follow the preparations, as explained above
1. Check for pending pull requests, to see which translations are currently in progress
1. Use `mapping_todo_new.*` to determine which text you want to translate
1. Perform the translation in `mapping_dev.*`, i.e. only this file should be modified
1. Prefix your commit message by `Chinese translation updated: `
1. Send us a pull request, again with `Chinese translation update: ` prefix

> **Note!** Please make sure that your pull request does not contain any unrelated formatting changes (like line endings) or any other unnecessary changes, like re-orderings (keys are automatically sorted by us).

## Help to collect

Due to the dynamic generation of SmartGit texts, the master mapping does not contain *all* keys, but only *all currently known* keys which have been 'collected' by our contributors and us. To help collecting keys:

1. Follow the preparations, as explained above
1. Make sure SmartGit is not running (Repository|Exit)
1. Locate `smartgit.properties` in SmartGit's settings directory (see About dialog) and add following lines there:
   ```
   smartgit.i18n=<locale>
   smartgit.debug.i18n.development=<path-to-localization-directory>
   smartgit.debug.i18n.master=<path-to-master-mapping>
   ```
   For the above example directory and Chinese locale, this will be:
   ```
   smartgit.i18n=zh_CN
   smartgit.debug.i18n.development=C\:/temp/smartgit-translations.git/zh-CN
   smartgit.debug.i18n.master=C\:/temp/smartgit-translations.git/mapping
   ```
1. Restart SmartGit
1. SmartGit will now have created several new files in the specified `development`directory, most importantly `unknown.*` which contains not yet known keys, i.e. keys for which there is no matching entry in the master mapping file yet; note that `unknown.*` is an ignored file which is 'owned' by you
1. From time to time, check the `unknown.*` file and send us a pull request:
1. Pull the latest changes, to be sure you have the latest version of `mappings_unknown`
1. Shutdown SmartGit
1. Update `mappings_unknown` from `unknown.*`:
   1. Copy new keys over, e.g. using a file compare tool
   1. Review your changes to `mappings_unknown` for possible sensitive information, like server names, and replace by 'XXX'
   1. Prefix your commit message by `mappings_unknown updated: `    
1. Send us a pull request, again with `mappings_unknown updated: ` prefix 
1. **Remove your `unknown.*`-file**, to start collecting new keys from scratch
1. Restart SmartGit and continue collecting new keys

## Help to review

Pending pull requests and existing translations in `mapping_dev.*` may sometimes need refinement. Review comments and suggestions to improve existing translations are welcome!