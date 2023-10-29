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

# try:
#     import wmi

#     def check_biometric_devices():
#         c = wmi.WMI()
#         biometric_devices = []
#         for device in c.Win32_PnPEntity():
#             if 'biometric' in device.Caption.lower():
#                 biometric_devices.append(device.Caption)
#         return biometric_devices

#     if __name__ == "__main__":
#         biometric_devices = check_biometric_devices()
#         if biometric_devices:
#             print("Biometric devices found on this system:")
#             for device in biometric_devices:
#                 print(device)
#         else:
#             print("No biometric devices found on this system.")
# except ImportError:
#     print("The 'wmi' module is not available. Please install it.")




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

    def check_biometric_devices():
        c = wmi.WMI()
        biometric_devices = []
        for device in c.Win32_PnPEntity():
            if device.Caption is not None and 'biometric' in device.Caption.lower():
                biometric_devices.append(device.Caption)
        return biometric_devices

    if __name__ == "__main__":
        biometric_devices = check_biometric_devices()
        if biometric_devices:
            print("Biometric devices found on this system:")
            for device in biometric_devices:
                print(device)
        else:
            print("No biometric devices found on this system.")
except ImportError:
    print("The 'wmi' module is not available. Please install it.")

