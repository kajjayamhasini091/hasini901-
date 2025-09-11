import pywhatkit as kit
import datetime

# Enter details
phone_number = "+911234567890"   # Replace with recipient’s number (include country code)
message = "Hello! This is an automated message from Python 🤖"
time_hour = datetime.datetime.now().hour
time_minute = datetime.datetime.now().minute + 2   # send 2 minutes from now

# Send WhatsApp Message
kit.sendwhatmsg(phone_number, message, time_hour, time_minute)

print("✅ Message scheduled! WhatsApp Web will open automatically.")
