# import platform

# def get_system_info():
#     system_info = {
#         'System': platform.system(),
#         'Node Name': platform.node(),
#         'Release': platform.release(),
#         'Version': platform.version(),
#         'Machine': platform.machine(),
#         'Processor': platform.processor()
#     }
#     return system_info

# if name == "main":
#     info = get_system_info()
#     for key, value in info.items():
#         print(f"{key}: {value}")

# import wmi

# def check_fingerprint_reader():
#     c = wmi.WMI()
#     for biometric in c.Win32_Biometric():
#         if 'fingerprint' in biometric.Description.lower():
#             return True
#     return False

# if name == "main":
#     fingerprint_available = check_fingerprint_reader()
#     if fingerprint_available:
#         print("Fingerprint reader is available on this system.")
#     else:
#         print("No fingerprint reader found on this system.")


# import platform

# def get_system_info():
#     system_info = {
#         'System': platform.system(),
#         'Node Name': platform.node(),
#         'Release': platform.release(),
#         'Version': platform.version(),
#         'Machine': platform.machine(),
#         'Processor': platform.processor()
#     }
#     return system_info

# if __name__ == "__main__":
#     info = get_system_info()
#     for key, value in info.items():
#         print(f"{key}: {value}")

# import wmi

# def check_fingerprint_reader():
#     c = wmi.WMI()
#     for biometric in c.Win32_Biometric():
#         if 'fingerprint' in biometric.Description.lower():
#             return True
#     return False

# if __name__ == "__main__":
#     fingerprint_available = check_fingerprint_reader()
#     if fingerprint_available:
#         print("Fingerprint reader is available on this system.")
#     else:
#         print("No fingerprint reader found on this system.")


import platform

def get_system_info():
    system_info = {
        'System': platform.system(),
        'Node Name': platform.node(),
        'Release': platform.release(),
        'Version': platform.version(),
        'Machine': platform.machine(),
        'Processor': platform.processor()
    }
    return system_info

if __name__ == "__main__":
    info = get_system_info()
    for key, value in info.items():
        print(f"{key}: {value}")

try:
    import wmi

    def check_fingerprint_reader():
        c = wmi.WMI()
        for biometric in c.Win32_Biometric():
            if 'fingerprint' in biometric.Description.lower():
                return True
        return False

    if __name__ == "__main__":
        fingerprint_available = check_fingerprint_reader()
        if fingerprint_available:
            print("Fingerprint reader is available on this system.")
        else:
            print("No fingerprint reader found on this system.")
except ImportError:
    print("The 'wmi' module is not available. Please install it.")
except AttributeError:
    print("The 'Win32_Biometric' class is not available on this system.")
