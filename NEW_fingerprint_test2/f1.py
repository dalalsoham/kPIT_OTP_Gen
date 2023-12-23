import platform
import pyfingerprint

def get_device_information():
  """Returns a dictionary of device information."""
  device_info = {}
  device_info["system"] = platform.system()
  device_info["release"] = platform.release()
  device_info["version"] = platform.version()
  device_info["machine"] = platform.machine()
  return device_info

def check_fingerprint_reader_availability():
  """Checks if a fingerprint reader is available and returns True or False."""
  try:
    device = pyfingerprint.PyFingerprint()
    device.open()
    device.close()
    return True
  except Exception as e:
    return False

def display_device_information_and_fingerprint_reader_availability():
  """Displays the device information and whether a fingerprint reader is available."""
  device_info = get_device_information()
  fingerprint_reader_available = check_fingerprint_reader_availability()

  print("Device information:")
  for key, value in device_info.items():
    print(f"  {key}: {value}")

  print("Fingerprint reader available:", fingerprint_reader_available)

if name == "main":
  display_device_information_and_fingerprint_reader_availability()