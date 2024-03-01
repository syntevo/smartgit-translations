# SmartGit Translations Utilities

## Overview

ここにあるスクリプトは、SmartGit のローカリゼーションファイルを効率よく取り扱うためのユーティリティツールです。

SmartGitのローカリゼーションファイルをpoファイルフォーマットに移行することと、そのメンテナンスを目的として作成されました。

poファイルフォーマットはGNU gettext に由来するファイルフォーマットですが、現在ではローカリゼーションファイルのデファクトスタンダードの一つとなっており、多くの翻訳支援ツールでサポートされています。
これにより、多くの翻訳支援ツールの使用が可能になり、翻訳の効率化と品質向上ができることを期待しています。

翻訳支援ツールにはPoedit、Virtaal、Lokalizeなどが使用されることを想定しています。

## Scripts

### Scripts for po file operations

#### import_unknown.py
'unknown.*' の内容を 'messages.pot' に取り込みます。

#### import_mismatch.py
'mismatch.*' の内容を 'messages.pot' に取り込みます。

#### delete_extracted_comments.py
'messages.pot' に含まれる extracted-comments を全て削除します。
extracted-comments には未知のキーが検出される直前の操作履歴が含まれています。

#### import_pot.py
'messages.pot' の内容を 全ての'&lt;locale_code&gt;.po' に取り込みます。

#### format_po_files.py
'&lt;locale_code&gt;.po' のフォーマットを修正します。

### Script for migration from legacy format to po format

#### locale2po.py

SmartGit 23.1 用のmappingファイル(mapping,mapping.dev,mapping.state)をpoファイルフォーマットへ変換します。
変換対象のファイルと出力先はスクリプトの配置先からの相対位置で自動的に指定され、全ての言語が自動的に処理されます。
コマンドライン引数などは必要ありません。

入力ファイルはRepositoryのルートにある'mapping'と、ローケルのフォルダにある'mapping.dev','mapping.state'です。
変換されたファイルは、以下の場所に出力されます。

&lt;repository root&gt;/po/&lt;locale code&gt;.po

&lt;locale code&gt; は ja_JP、zh_CN.po などのローケルコードです。 

#### master2pot.py

SmartGit 23.1 用のリポジトリのルートにあるmappingファイル(原文が格納されているmaster mappingファイル)をpotファイルフォーマットへ変換します。
変換対象のファイルと出力先はスクリプトの配置先から相対位置で自動的に指定されます。
コマンドライン引数などは必要ありません。

入力ファイルはRepositoryのルートにある'mapping' です。
変換されたファイルは以下の場所に出力されます。

&lt;repository root&gt;/po/messages.pot 


## initial setup

このスクリプトは標準的な方法でインストールされたPythonとvenvを組み合わせた環境での使用を想定しています。
Anaconda などを使用した環境での検証はしていません。

1. Install Python
    
    Python を公式ページからダウンロード、インストールしてください。
    動作確認はWindows版のPython 3.10 で行われています。

    https://www.python.org/

1. Setup venv
    
    以下のbatファイルを実行してください。
    自動的にvenv による仮想環境の作成、venvのアクティベーション、依存関係ライブラリのインストールなどが行われます。
    その後、venvをアクティーベション済みのコマンドプロンプトが開き、ユーザが任意のスクリプトを実行できるようになります。
    ```
    <Repository_root>/src/setup_venv.bat
    ```
    依存関係のライブラリは `requirements.txt` に記述されたものがインストールされます。

  > [!NOTE]
  > システムに複数のバージョンのPythonがインストールされている場合、システムのデフォルトのバージョンが使用されます。 
  > 変更したい場合はbatファイルの2行目にある以下の行を `PYTHON=py -3.11` のように変更します。
  > 利用可能なバージョンは、コマンドプロンプトなどで`py -0`を実行することで確認できます。
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

初期セットアップと同様に`setup_venv.bat`を実行し、venvをアクティーベション済のコマンドプロンプトを開きます。

コマンドプロンプトでそのまま `python locale2po.py` などのようにスクリプトを実行します。



