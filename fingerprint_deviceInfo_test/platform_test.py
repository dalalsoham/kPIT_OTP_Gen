# # import platform

# # def get_system_info():
# #     system_info = {
# #         'System': platform.system(),
# #         'Node Name': platform.node(),
# #         'Release': platform.release(),
# #         'Version': platform.version(),
# #         'Machine': platform.machine(),
# #         'Processor': platform.processor()
# #     }
# #     return system_info

# # if name == "main":
# #     info = get_system_info()
# #     for key, value in info.items():
# #         print(f"{key}: {value}")

# # import wmi

# # def check_fingerprint_reader():
# #     c = wmi.WMI()
# #     for biometric in c.Win32_Biometric():
# #         if 'fingerprint' in biometric.Description.lower():
# #             return True
# #     return False

# # if name == "main":
# #     fingerprint_available = check_fingerprint_reader()
# #     if fingerprint_available:
# #         print("Fingerprint reader is available on this system.")
# #     else:
# #         print("No fingerprint reader found on this system.")


# # import platform

# # def get_system_info():
# #     system_info = {
# #         'System': platform.system(),
# #         'Node Name': platform.node(),
# #         'Release': platform.release(),
# #         'Version': platform.version(),
# #         'Machine': platform.machine(),
# #         'Processor': platform.processor()
# #     }
# #     return system_info

# # if __name__ == "__main__":
# #     info = get_system_info()
# #     for key, value in info.items():
# #         print(f"{key}: {value}")

# # import wmi

# # def check_fingerprint_reader():
# #     c = wmi.WMI()
# #     for biometric in c.Win32_Biometric():
# #         if 'fingerprint' in biometric.Description.lower():
# #             return True
# #     return False

# # if __name__ == "__main__":
# #     fingerprint_available = check_fingerprint_reader()
# #     if fingerprint_available:
# #         print("Fingerprint reader is available on this system.")
# #     else:
# #         print("No fingerprint reader found on this system.")


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

#     def check_fingerprint_reader():
#         c = wmi.WMI()
#         for biometric in c.Win32_Biometric():
#             if 'fingerprint' in biometric.Description.lower():
#                 return True
#         return False

#     if __name__ == "__main__":
#         fingerprint_available = check_fingerprint_reader()
#         if fingerprint_available:
#             print("Fingerprint reader is available on this system.")
#         else:
#             print("No fingerprint reader found on this system.")
# except ImportError:
#     print("The 'wmi' module is not available. Please install it.")
# except AttributeError:
#     print("The 'Win32_Biometric' class is not available on this system.")


import platform
import subprocess
import wmi

def get_serial_number():
    system = platform.system()
    if system == 'Windows':
        try:
            c = wmi.WMI()
            for item in c.Win32_BIOS():
                return item.SerialNumber
        except Exception as e:
            print("Error occurred while fetching serial number using WMI:", e)
            try:
                output = subprocess.check_output(['wmic', 'bios', 'get', 'serialnumber']).decode().split('\n')
                return output[1].strip()
            except Exception as e:
                print("Error occurred while fetching serial number using WMIC command:", e)
                return "Serial Number not found"
    elif system == 'Linux':
        try:
            with open('/sys/class/dmi/id/product_serial') as f:
                return f.read().strip()
        except FileNotFoundError:
            try:
                output = subprocess.check_output(['dmidecode', '-s', 'system-serial-number']).decode().strip()
                return output
            except Exception as e:
                print("Error occurred while fetching serial number on Linux:", e)
                return "Serial Number not found"
    elif system == 'Darwin':  # For MacOS
        try:
            output = subprocess.check_output(["system_profiler", "SPHardwareDataType"])
            output = output.decode("utf-8")
            serial_number = list(filter(lambda x: "Serial Number" in x, output.split("\n")))[0].split(":")[1].strip()
            return serial_number
        except Exception as e:
            print("Error occurred while fetching serial number on MacOS:", e)
            return "Serial Number not found"
    else:
        return "Platform not supported"

print("Device Serial Number:", get_serial_number())