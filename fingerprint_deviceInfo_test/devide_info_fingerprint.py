import platform
import pyzk 

# Get the device's machine type
machine_type = platform.machine()

# Get the device's machine name
machine_name = platform.node()

# Get the device's operating system
operating_system = platform.system()

# Get the device's operating system version
operating_system_version = platform.version()

# Get the device's processor type
processor_type = platform.processor()

# Get the device's Python version
python_version = platform.python_version()

# Check if fingerprint reader is available
try:
    # Connect to the biometric device
    conn = pyzk.ZKConnection()
    conn.connect("localhost", 4370)

    # Check if the biometric device has a fingerprint sensor
    if conn.get_sensor_type() == pyzk.SENSOR_TYPE_FINGERPRINT:
        fingerprint_reader_available = True
    else:
        fingerprint_reader_available = False

    # Disconnect from the biometric device
    conn.disconnect()
except Exception as e:
    # If there is an exception, fingerprint reader is not available
    fingerprint_reader_available = False

# Print the device information and biometric device information
print(f"Machine type: {machine_type}")
print(f"Machine name: {machine_name}")
print(f"Operating system: {operating_system}")
print(f"Operating system version: {operating_system_version}")
print(f"Processor type: {processor_type}")
print(f"Python version: {python_version}")
print(f"Fingerprint reader available: {fingerprint_reader_available}")