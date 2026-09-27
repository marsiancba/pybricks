@echo off
echo Running formel.py on LEGO Spike Prime...
echo.
echo Make sure your LEGO Spike Prime is:
echo 1. Powered on
echo 2. Connected via USB cable
echo 3. Running Pybricks firmware
echo.
pause
py -m pybricksdev run usb formel.py
pause

