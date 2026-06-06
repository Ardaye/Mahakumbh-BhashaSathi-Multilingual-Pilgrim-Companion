@echo off
cd /d "%~dp0"
if exist ..\.venv\Scripts\python.exe (
  ..\.venv\Scripts\python.exe maha_kumbh_assistant.py
) else (
  python maha_kumbh_assistant.py
)
pause
