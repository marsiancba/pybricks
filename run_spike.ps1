# PowerShell script to run formel.py on LEGO Spike Prime
Write-Host "Running formel.py on LEGO Spike Prime..." -ForegroundColor Green
Write-Host ""
Write-Host "Make sure your LEGO Spike Prime is:" -ForegroundColor Yellow
Write-Host "1. Powered on" -ForegroundColor White
Write-Host "2. Connected via USB cable" -ForegroundColor White
Write-Host "3. Running Pybricks firmware" -ForegroundColor White
Write-Host ""

# Check if device is connected
Write-Host "Checking for connected devices..." -ForegroundColor Cyan
try {
    py -m pybricksdev run usb formel.py
} catch {
    Write-Host "Error: Could not connect to LEGO Spike Prime" -ForegroundColor Red
    Write-Host "Please check:" -ForegroundColor Yellow
    Write-Host "- Device is powered on" -ForegroundColor White
    Write-Host "- USB cable is connected" -ForegroundColor White
    Write-Host "- Pybricks firmware is installed" -ForegroundColor White
}

Read-Host "Press Enter to continue"

