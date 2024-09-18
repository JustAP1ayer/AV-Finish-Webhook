try:
    import pyautogui # cause of opencv for confidence
    import logging
    from PIL import Image, ImageGrab # pillow
    from io import BytesIO
    import json
    import os
    import time
    from discord_webhook import DiscordWebhook, DiscordEmbed
    import pygetwindow as gw
except ImportError:
    os.system("pip install pillow opencv-python discord-webhook pygetwindow pyautogui")


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

logging.warning("Remember, your UI Scale must be 1 in Anime Vanguards!")

with open("config.json", "r") as config_file:
    config = json.load(config_file)

show_full_screen = config.get("screenshot_full_screen", False)
player_ids = config.get("player_id_to_ping", [])
checkcooldown = config.get("resend_timeout", 100)
send_webhook_delay = config.get("send_webhook_delay", 0.5)
screenshot_delay = config.get("screenshot_delay", 0.5)

player_ping_string = " ".join([f"<@{i}>" for i in player_ids]) if config.get("ping_players", False) else ""
logging.info(f"Players to ping: '{player_ping_string}'")

def send_webhook(webhook_url, embed, content, screenshot_bytes=None):
    webhook = DiscordWebhook(webhook_url, content=content)
    webhook.add_embed(embed)
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/rbx-anime-vanguards/images/7/71/AnimeVanguards.png/revision/latest?cb=20240531035940")
    embed.set_timestamp()

    if screenshot_bytes:
        webhook.add_file(file=screenshot_bytes, filename='screenshot.png')
        embed.set_image(url="attachment://screenshot.png")

    response = webhook.execute()
    logging.info("Webhook message sent successfully.")

def capture_window(window_title):
    try:
        if show_full_screen:
            return ImageGrab.grab()

        roblox_window = next((win for win in gw.getWindowsWithTitle(window_title)), None)
        if roblox_window and roblox_window.isActive:
            logging.info("Found Roblox Window!")
            bbox = (roblox_window.left + 10, roblox_window.top + 10, roblox_window.right - 10, roblox_window.bottom - 10)
            return ImageGrab.grab(bbox)
        
        logging.warning(f"Window titled '{window_title}' not found. Using placeholder image.")
        return Image.open('placeholder.png')
    
    except Exception as e:
        logging.error(f"Error capturing window '{window_title}': {e}. Using placeholder image.")
        return Image.open('placeholder.png')

image_prototypes = ["replay1.png", "replay2.png", "return1.png", "return2.png"] 
last_webhook_sent = 0
webhooks_sent = 1

while True:
    try:
        for image_file in image_prototypes:
            button_location = pyautogui.locateCenterOnScreen(image_file, confidence=0.75)
            if button_location:
                logging.info(f"Found image: '{image_file}' at {button_location}")
                
                time.sleep(screenshot_delay)
                screenshot = capture_window("Roblox")
                screenshot_bytes = BytesIO()
                screenshot.save(screenshot_bytes, format='PNG')
                screenshot_bytes.seek(0)

                description_text = f"``` ```\n> # Map Finished!\n> ## {webhooks_sent} Webhook Update{'s' if webhooks_sent != 1 else ''} Sent!"

                if webhooks_sent > 1:
                    time_now = time.time()  
                    time_elapsed = time_now - last_webhook_sent
                    minutes, seconds = divmod(time_elapsed, 60)
                    description_text += f"\n> ### Time since last update: {int(minutes)} minutes, {seconds:.2f} seconds."

                last_webhook_sent = time.time()

                embed = DiscordEmbed(
                    title="Game Finish UI Spotted!",
                    description=description_text
                )

                logging.info("Found Finished Game UI, creating Discord Embed.")
                time.sleep(send_webhook_delay)
                
                for webhook_url in config.get("discord_webhook", []):
                    send_webhook(webhook_url, embed, player_ping_string, screenshot_bytes.getvalue())
                
                webhooks_sent += 1
                logging.info(f"Waiting {checkcooldown}s before sending another message.")
                time.sleep(checkcooldown)
                
            time.sleep(0.1)
    
    except pyautogui.ImageNotFoundException:
        logging.error("Could not find image!")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        time.sleep(1)
    
    time.sleep(0.1)
