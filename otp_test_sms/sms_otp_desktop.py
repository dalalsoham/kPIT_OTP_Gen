from plyer import notification
import random

# Generate a random OTP (You can use your OTP generation logic)
otp = str(random.randint(1000, 9999))

# Message to be sent in the notification
message = f"Your OTP is: {otp}"

# Create a notification
notification.notify(
    title="OTP Notification",
    message=message,
)

