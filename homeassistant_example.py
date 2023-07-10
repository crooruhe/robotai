from homeassistant.core import HomeAssistant
from homeassistant.const import STATE_ON
from homeassistant.exceptions import HomeAssistantError

# Establish a connection to your Home Assistant instance
try:
    # Specify the URL and API token for your Home Assistant instance
    ha = HomeAssistant("http://localhost:8123", "YOUR_API_TOKEN")
except HomeAssistantError as err:
    print(f"Error connecting to Home Assistant: {err}")

async def turn_on_light():
    try:
        # Call the service to turn on the light
        await ha.services.async_call(
            "light",
            "turn_on",
            {"entity_id": "light.your_light_entity_id"},
        )
        print("Light turned on successfully!")
    except HomeAssistantError as err:
        print(f"Error turning on light: {err}")

# Call the function to turn on the light
ha.loop.run_until_complete(turn_on_light())
