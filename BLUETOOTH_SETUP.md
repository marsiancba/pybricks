# Bluetooth Setup for LEGO Spike Prime

This guide will help you connect your LEGO Spike Prime to your computer via Bluetooth for wireless programming and debugging.

## Prerequisites

1. **LEGO Spike Prime Hub** with Pybricks firmware installed
2. **Computer with Bluetooth** capability
3. **Windows 10/11** (this guide is for Windows)

## Step 1: Prepare Your LEGO Spike Prime

1. **Power on** your LEGO Spike Prime hub
2. **Ensure Pybricks firmware** is installed (if not, install it first)
3. The hub should be in **pairing mode** automatically when powered on

## Step 2: Pair with Windows

### Method 1: Windows Settings (Recommended)

1. **Open Windows Settings**:
   - Press `Windows + I`
   - Go to **Devices** → **Bluetooth & other devices**

2. **Add a new device**:
   - Click **"Add Bluetooth or other device"**
   - Select **"Bluetooth"**

3. **Find your LEGO Spike Prime**:
   - Look for a device named something like:
     - `LEGO Hub` or `LEGO Hub 1234`
     - `Pybricks Hub`
     - `Spike Prime Hub`
   - The exact name may vary

4. **Complete pairing**:
   - Click on your device when it appears
   - Follow any on-screen prompts
   - The device should now show as "Connected"

### Method 2: Device Manager (Alternative)

1. **Open Device Manager**:
   - Press `Windows + X`
   - Select **"Device Manager"**

2. **Scan for devices**:
   - Click **"Action"** → **"Scan for hardware changes"**
   - Look for your LEGO device under **"Bluetooth"** or **"Other devices"**

## Step 3: Test the Connection

### Quick Test
Run this command to test if your device is discoverable:

```bash
py -m pybricksdev run ble formel.py
```

### Using the Scripts
1. **Double-click** `run_spike_bluetooth.bat`
2. Or run `run_spike_bluetooth.ps1` in PowerShell

### Using VS Code
1. Open this folder in VS Code
2. Press `F5`
3. Select **"Run on LEGO Spike Prime (Bluetooth)"** or **"Debug on LEGO Spike Prime (Bluetooth)"**

## Troubleshooting

### Device Not Found
- **Check Bluetooth is enabled** on your computer
- **Restart the LEGO Spike Prime** hub
- **Remove and re-pair** the device in Windows settings
- **Check Windows Bluetooth drivers** are up to date

### Connection Failed
- **Move closer** to the device (Bluetooth range is limited)
- **Remove other Bluetooth devices** that might interfere
- **Restart Bluetooth** on your computer
- **Try USB connection** as a fallback

### Permission Issues
- **Run PowerShell as Administrator** if needed
- **Check Windows Firewall** settings
- **Ensure Bluetooth permissions** are granted

## Bluetooth vs USB Comparison

| Feature | Bluetooth | USB |
|---------|-----------|-----|
| **Range** | ~10 meters | Cable length |
| **Setup** | Requires pairing | Plug and play |
| **Reliability** | Can drop connection | Very stable |
| **Speed** | Slower | Faster |
| **Convenience** | Wireless | Wired |

## Tips for Best Results

1. **Keep devices close** during initial setup
2. **Use USB for debugging** (more reliable)
3. **Use Bluetooth for final testing** (wireless freedom)
4. **Pair once, use many times** - no need to re-pair each session
5. **Check battery level** on the LEGO hub

## Advanced: Using Specific Device Names

If you have multiple LEGO devices, you can specify which one to connect to:

```bash
py -m pybricksdev run ble -n "LEGO Hub 1234" formel.py
```

Replace `"LEGO Hub 1234"` with your actual device name from Windows Bluetooth settings.
