import ctypes

def check_fingerprint_reader():
    try:
        # Load the Advapi32.dll library
        advapi32 = ctypes.windll.LoadLibrary('Advapi32.dll')

        # Define the constants for registry access
        KEY_WOW64_64KEY = 0x0100
        KEY_READ = 0x20019

        # Open the registry key for Goodix Fingerprint SPI device
        hKey = ctypes.c_void_p()
        result = advapi32.RegOpenKeyExW(
            ctypes.c_uint(0x80000002),  # HKEY_LOCAL_MACHINE
            "SYSTEM\\CurrentControlSet\\Enum\\USB\\VID_27C6&PID_538B",
            0,
            KEY_READ | KEY_WOW64_64KEY,
            ctypes.byref(hKey)
        )

        # Check if the registry key was opened successfully
        if result == 0:
            advapi32.RegCloseKey(hKey)
            return True
    except Exception as e:
        print(f"An error occurred: {e}")

    return False

if __name__ == "__main__":
    fingerprint_available = check_fingerprint_reader()
    if fingerprint_available:
        print("Goodix Fingerprint SPI device is available on this system.")
    else:
        print("No Goodix Fingerprint SPI device found on this system.")
