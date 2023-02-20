# SmartGit Localization - SmartGit Translation Files

This repository contains translation files for the Git client SmartGit:

https://www.syntevo.com/smartgit/download/

# How does SmartGit's localization work?

SmartGit contains the various UI texts ('strings') directly in the source code. Many of these strings are dynamically composed. The main UI components have keys assigned which are used to look up translations from mapping files. The root `mapping` file ('master mapping') contains all currently known keys with their English original texts. For all currently supported locales, corresponding sub-directories contains a `mapping.dev` file with appropriate translations and/or comments on not-yet translated keys or keys which may require a new translation. There is also an auxiliary `mapping.state` file.

The master mapping will be updated by us from SmartGit sources in regular intervals. `mapping.dev` and `mapping.state` will be updated primarily by contributers and synchronized back by us to SmartGit sources.

For every SmartGit version, there is a separate branch, like `smartgit-22.1`.

# How to contribute?

You can contribute to the localization of SmartGit in two ways:

* **Help to translate**: add/improve translations in `mapping.dev` language mappings
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

Every single new translation is welcome! To contribute, follow these steps:

1. Perform the preparations, as explained above
1. Check for pending pull requests, to see which translations are currently in progress
1. Use `mapping.dev` to determine which text you want to translate.
   For keys which require a (re-)translation, `mapping.dev` contains special comment lines (`#`) with the `!=`-marker directly below the key-line.
   The text after the `!=`-marker is taken from the master mapping and represents the English original text, which the translation should reflect.
   For example, if there is no translation present yet, this may look like:

   ```
   dlgProgress.lbl"Please wait ..."=
   #                              !=Please wait ...
   ```

   If there is already a translation, but the English original text has changed, this may look like:

   ```
   dlgProgress.lbl"Please wait ..."=你得等一等
   #                              !=Please wait ...
   ```
1. In `mapping.dev` apply the proper translation and remove the comment line.
   For the above examples, this may look like:
   ```
   dlgProgress.lbl"Please wait ..."=请稍等 ...
   ```
1. In `mapping.state` locate the key which you have translated and update/set the English original text to which your translations now corresponds to.
   This should be the identical English text which is present in the master mapping and which was present in the `!=`-comment.
   For the above examples, this may look like:
   ```
   dlgProgress.lbl"Please wait ..."=Please wait ...
   ```
1. Have a single commit including both files
   1. Prefix your commit message by `Chinese translation updated: ` (or the appropriate language name)
1. Send us a pull request, again with `Chinese translation update: ` prefix (or the appropriate language name)

> **Note!** Please make sure that your pull request does not contain any unrelated formatting changes (like line endings) or any other unnecessary changes, like re-orderings (keys are automatically sorted by us).

### Details on the syntax

If the translation of a specific text should remain identical to the original English text, prefix the text by `=`. For example:

> *.btn"OK"==OK

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
1. SmartGit will now have created several new files in the specified `development`-directory, most importantly:
   1. `unknown.*`, which contains not yet known keys, i.e. keys for which there is no matching entry in the master mapping file yet
   1. `mismatch.code.*`, which contains already known keys and represents the current state in the code
   1. `mismatch.mapping.*`, which contains already known keys and represents the obsolete state in the master mapping
   1. Note that all three files are ignored and thus 'owned' by you
1. Shutdown SmartGit
1. From time to time, check these files, compress them and send us to `smartgit@syntevo.com`
   1. Prefix your email by "Language mappings: new/changed keys"
1. **Remove all three files**, to start collecting new keys from scratch
1. Restart SmartGit and continue collecting new keys

## Help to review

Pending pull requests and existing translations in `mapping.dev` may sometimes need refinement. Review comments and suggestions to improve existing translations are welcome!