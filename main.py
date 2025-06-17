"""
Update the Discord bot's avatar using an image file.

This script loads the avatar path and bot token from environment variables,
reads the avatar file, encodes it to base64, and sends a PATCH request
to update the bot's avatar.

Environment Variables:
- AVATAR_PATH (str): The path to the avatar image file.
- TOKEN (str): The Discord bot token.

Raises:
- Exception: If reading the file, encoding, or the HTTP request fails.
"""

import base64
import os

import requests
from dotenv import load_dotenv

load_dotenv()


try:
    with open(os.getenv("AVATAR_PATH"), "rb") as file:
        avatar_data = base64.b64encode(file.read()).decode("utf-8")
    response = requests.patch(
        "https://discord.com/api/v10/users/@me",
        headers={
            "Authorization": f"Bot {os.getenv('TOKEN')}",
            "Content-Type": "application/json",
        },
        json={"avatar": f"data:image/gif;base64,{avatar_data}"},
    )
    if response.ok:
        print("Avatar Updated!")
    else:
        print(f"Failed to Update Avatar: {response.status_code}")
        print(f"Response body: {response.text}")

except Exception as e:
    print(f"There is an Error here: {e}")
