set VENV=.\.venv
if "%PYTHON%"=="" set PYTHON=python
if not exist "%VENV%\Scripts\activate" %PYTHON% -m venv %VENV%
call %VENV%\Scripts\activate

python -m pip install --upgrade pip
pip install -r .\requirements.txt

set PATH=%cd%;%PATH%
set PYTHONPATH=%cd%;%PYTHONPATH%

call cmd
