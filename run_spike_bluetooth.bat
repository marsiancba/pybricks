@echo off
echo Running formel.py on LEGO Spike Prime via Bluetooth...
echo.
echo Make sure your LEGO Spike Prime is:
echo 1. Powered on
echo 2. Paired with your computer via Bluetooth
echo 3. Running Pybricks firmware
echo.
pause
py -m pybricksdev run ble formel.py
pause
