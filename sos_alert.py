import requests
from twilio.rest import Client
import os

# Twilio API Credentials (Replace with actual values)
TWILIO_SID = "AC92e25d774628ba283d01219e67621efc"
TWILIO_AUTH_TOKEN = "d7730196c765311139eb61ff4336ad5f"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"

# Emergency Contacts
MOTHER_WHATSAPP = "whatsapp:+917276651586"
FATHER_WHATSAPP = "whatsapp:+917841840950"

# Function to get approximate location using IP
def get_live_location():
    url = "http://ip-api.com/json/"
    response = requests.get(url)
    location = response.json()

    lat = location.get("lat", "Unknown")
    lon = location.get("lon", "Unknown")
    city = location.get("city", "Unknown City")
    region = location.get("regionName", "Unknown Region")
    country = location.get("country", "Unknown Country")

    map_url = f"https://maps.google.com/?q={lat},{lon}"
    return f"📍 Location: {city}, {region}, {country}\n🔗 {map_url}"

# Generate live location link
location_info = get_live_location()

# SOS Alert Message
sos_message = f"🚨 *SOS Alert!* 🚨\n\nHelp needed! Please check immediately.\n{location_info}"

# Initialize Twilio Client
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# Send SOS Alert
for contact in [MOTHER_WHATSAPP, FATHER_WHATSAPP]:
    message = client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        to=contact,
        body=sos_message
    )
    print(f"🚀 SOS Alert Sent! Message SID: {message.sid}")
