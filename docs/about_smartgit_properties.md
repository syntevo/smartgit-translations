# About smartgit.properties

`smartgit.properties` is a configuration file located in the SmartGit settings directory. The following options are intended for developers and translators of SmartGit, and their specifications may change.

| #  | Key | Type | Default | Description |
|----|-----|------|---------|-------------|
| 1  | smartgit.debug.i18n.markTranslatable | boolean | false | A specific mark will be displayed at the beginning of the translation for UI elements not yet included in `messages.pot`. |
| 2  | smartgit.debug.i18n.markUntranslated | boolean | false | A specific mark will be displayed at the beginning of the translation for UI elements that have not yet been translated. |
| 3  | smartgit.debug.i18n.markerTranslatable | string | ✨ | Specifies the character to be displayed when `i18n.markTranslatable` is true in option 1. |
| 4  | smartgit.debug.i18n.markerUntranslated | string | ■ | Specifies the character to be displayed when `i18n.markUntranslated` is true in option 2. |

Despite setting options 3 and 4, strings that remain in the original language on the GUI are currently untranslatable and require modifications to the SmartGit source code to become translatable.
