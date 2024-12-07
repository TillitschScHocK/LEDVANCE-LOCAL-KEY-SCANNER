@echo off
REM Überprüfe, ob Python installiert ist
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Python ist nicht installiert.
    timeout /T 1 >NUL
    echo Bitte gehen Sie in den Microsoft Store und laden Sie die neueste Python-Version herunter.
    timeout /T 1 >NUL
    echo Führen Sie danach dieses Skript erneut aus.
    timeout /T 1 >NUL
    echo Sie werden jetzt in den Microsoft Store weitergeleitet.
    timeout /T 1 >NUL
    start ms-windows-store://search/?query=python
    pause
    exit /b 1
)

for /f "tokens=2" %%V in ('python --version 2^>^&1') do set PYTHON_VERSION=%%V

echo Python %PYTHON_VERSION% ist installiert.

REM Überprüfe, ob pycryptodome und requests installiert sind, und installiere sie bei Bedarf
python -c "import Crypto" 2>NUL || (echo "PyCryptodome wird installiert..." && pip install pycryptodome)
python -c "import requests" 2>NUL || (echo "Requests wird installiert..." && pip install requests)

REM Starte das Python-Skript mit GUI
start /B pythonw ledvance-key-DE.py
exit
