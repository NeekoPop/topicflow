@echo off
echo ========================================
echo TopicFlow - AI Educational Assistant
echo ========================================
echo.

echo [1/3] Upgrading OpenAI library...
pip install --upgrade openai
echo.

echo [2/3] Installing other dependencies...
pip install -r requirements.txt
echo.

echo [3/3] Starting TopicFlow application...
echo.
python app.py

pause
