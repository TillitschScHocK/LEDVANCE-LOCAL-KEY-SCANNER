@echo off
REM Check if Python is installed
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed.
    timeout /T 1 >NUL
    echo Please go to the Microsoft Store and download the latest version of Python.
    timeout /T 1 >NUL
    echo After that, please run this script again.
    timeout /T 1 >NUL
    echo You will now be redirected to the Microsoft Store.
    timeout /T 1 >NUL
    start ms-windows-store://search/?query=python
    pause
    exit /b 1
)

for /f "tokens=2" %%V in ('python --version 2^>^&1') do set PYTHON_VERSION=%%V

echo Python %PYTHON_VERSION% is installed.

REM Check if pycryptodome and requests are installed, and install them if needed
python -c "import Crypto" 2>NUL || (echo "Installing PyCryptodome..." && pip install pycryptodome)
python -c "import requests" 2>NUL || (echo "Installing Requests..." && pip install requests)

REM Start the Python script with GUI
start /B pythonw ledvance-key-EN.py
exit
