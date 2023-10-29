# import pygetwindow as gw

# def check_fingerprint_device():
#     windows = gw.getWindowsWithTitle("Device Manager")

#     if windows:
#         device_manager_window = windows[0]
#         device_manager_window.restore()  # Ensure the window is restored if minimized
#         device_manager_window.activate()  # Activate the window

#         # Wait for a brief moment for the window to fully activate
#         gw.sleep(0.1)

#         # Search for the "Goodix Fingerprint SPI device" string in the window content
#         if "Goodix Fingerprint SPI device" in device_manager_window.text:
#             return True

#     return False

# if __name__ == "__main__":
#     fingerprint_available = check_fingerprint_device()
#     if fingerprint_available:
#         print("Goodix Fingerprint SPI device is available on this system.")
#     else:
#         print("No Goodix Fingerprint SPI device found on this system.")


import winreg

def check_fingerprint_device():
    try:
        # Open the registry key for biometric devices
        key = r"SYSTEM\CurrentControlSet\Enum\USB\VID_27C6&PID_538B"
        hKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key)

        # Check if the registry key was opened successfully
        if hKey:
            return True
    except Exception as e:
        print(f"An error occurred: {e}")

    return False

if __name__ == "__main__":
    fingerprint_available = check_fingerprint_device()
    if fingerprint_available:
        print("Goodix Fingerprint SPI device is available on this system.")
    else:
        print("No Goodix Fingerprint SPI device found on this system.")
