# SmartGit Translations Utilities

## Overview

The scripts found here are utility tools designed to efficiently handle the localization files of SmartGit. 

These scripts are designed to migrate localization files to the PO file format and maintain them.

The PO file format originates from GNU gettext, and is now considered one of the de facto standards for localization files, being supported by many translation support tools. 
By doing so, it is expected that the use of many translation support tools will be possible, leading to improvements in translation efficiency and quality.

Translation support tools such as Poedit, Virtaal, and Lokalize are expected to be used.

## Scripts

### Scripts for po file operations

#### import_unknown.py
Imports the content of 'unknown.*' into 'messages.pot'.

#### import_mismatch.py
Imports the content of 'mismatch.*' into 'messages.pot'.

#### delete_extracted_comments.py
Deletes all extracted-comments included in 'messages.pot'.
These extracted-comments contain the operation history just before unknown keys are detected.

#### import_pot.py
Imports the content of 'messages.pot' into all '&lt;locale_code&gt;.po'.

#### format_po_files.py
Corrects the format of '&lt;locale_code&gt;.po'.

### Script for migration from legacy format to po format

#### locale2po.py

Converts the mapping file (mapping, mapping.dev, mapping.state) for SmartGit 23.1 to the PO file format. The files to be converted and the destination are automatically specified by the relative reference from where the script is placed, and all languages are automatically processed. No command line arguments are required.

The input files are 'mapping' at the root of the repository, and 'mapping.dev','mapping.state' in the locale folder.
The converted files are output to the following location:

&lt;repository root&gt;/po/&lt;locale code&gt;.po

&lt;locale code&gt; is a locale code such as ja_JP, zh_CN.po.

#### master2pot.py

Converts the mapping file at the root of the repository (master mapping file where the original sentences are stored) for SmartGit 23.1 to the POT file format.
The files to be converted and the destination are automatically specified by the relative reference from where the script is placed. No command line arguments are required.

The input file is 'mapping' at the root of the repository.
The converted file is output to the following location:

&lt;repository root&gt;/po/messages.pot


## initial setup

These scripts are designed for use in environments that use Python installed in the standard way and the combined venv. We have not verified the environment using Anaconda and others.

1. Install Python
    
    Please download and install Python from the official page.
    Verification has been performed with the Windows version of Python 3.10.

    https://www.python.org/

1. Setup venv
    
    Please run the bat file below.
    This will automatically create a venv virtual environment, activate venv, install dependency libraries, etc. 
    Then, a command prompt with activated venv will open, and the user will be able to execute any script.
    ```
    <Repository_root>/src/setup_venv.bat
    ```
    The dependent libraries to be installed are described in `requirements.txt`.

  > [!NOTE]
  > If multiple versions of Python are installed on the system, the system's default version will be used.
  > If you want to change, please change the following line on the second line of the bat file to `PYTHON=py -3.11`.
  > Available versions can be confirmed by running `py -0` in command prompts etc.
  > 
  >Before
  > ```bat
  >     if "%PYTHON%"=="" set PYTHON=python
  > ```
  > After
  > ```bat
  >     if "%PYTHON%"=="" set PYTHON=py -3.11
  > ```

## How to use

Just like the initial setup, run `setup_venv.bat`, and open a command prompt with activated venv.

In the command prompt, simply execute `python locale2po.py` or `python master2pot.py`. 
