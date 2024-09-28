---

# AV-Finish-Webhook
This script sends notifications via Discord webhooks when you finish a game in *Anime Vanguards*.

---

## Ingame Settings

Graphics: Max (Roblox Setting)  
Can be lowered after 1 run, but must always be max on the first attempt  

Low Detail Mode: On (In-Game Anime Vanguard Setting)  

Camera Shake: Off (In-Raid Anime Vanguard Setting. Will not let you change this in the lobby)  

UI Scale: 1

---

## Required Python Libraries

To run the script, the following Python libraries (wrappers) are required. Each library’s purpose and installation method are summarized below.

### Installation Instructions
Run the following command to install all required libraries:

```bash
pip install pillow pyautogui opencv-python discord-webhook pygetwindow
```

---

## Python Libraries Used

### 1. `logging`
- **Installation**: Pre-installed with Python.
- **Summary**: Provides detailed logging information, including time-stamped messages at various levels (INFO, WARNING, ERROR).

### 2. `Pillow (PIL)`
- **Installation**: `pip install pillow`
- **Summary**: A powerful image processing library used for capturing screenshots, handling images, and manipulating them in memory (e.g., with `BytesIO`).

### 3. `json`
- **Installation**: Pre-installed with Python.
- **Summary**: Handles reading and writing JSON data, such as loading configuration settings from the `config.json` file.

### 4. `os`
- **Installation**: Pre-installed with Python.
- **Summary**: Provides interaction with the operating system for file/path management and executing system commands.

### 5. `time`
- **Installation**: Pre-installed with Python.
- **Summary**: Provides time-related functions, such as pausing execution (`sleep`) and measuring intervals.

### 6. `discord-webhook`
- **Installation**: `pip install discord-webhook`
- **Summary**: Simplifies sending messages, embeds, and files via Discord webhooks, including detailed messages and screenshots.

### 7. `pyautogui`
- **Installation**: `pip install pyautogui opencv-python`
- **Summary**: Used for GUI automation, including locating elements on the screen through image matching. It relies on OpenCV for better detection using the `confidence` parameter.

### 8. `pygetwindow`
- **Installation**: `pip install pygetwindow`
- **Summary**: Allows access and manipulation of application windows, such as getting window titles and capturing screenshots from specific windows.

### 9. `ImageGrab (Pillow)`
- **Installation**: Part of Pillow (installed via `pip install pillow`).
- **Summary**: Captures screenshots of the entire screen or a specific region.

### 10. `BytesIO`
- **Installation**: Pre-installed with Python.
- **Summary**: Handles binary data in memory as a file. Used to manage image data before saving to disk.

### 11. `opencv-python`
- **Installation**: `pip install opencv-python`
- **Summary**: A computer vision library used by `pyautogui` for image detection with confidence-based matching.

---

## Configuration (`config.json`)

The `config.json` file contains settings for the webhook and screenshot behaviors. Here’s what each configuration does:

```json
{
    "discord_webhook": ["https://discord.com/api/webhooks/"],
    "send_webhook_delay": 0.1,
    "screenshot_delay": 0.5,
    "ping_players": true,
    "player_id_to_ping": ["1234567890"],
    "resend_timeout": 100,
    "screenshot_full_screen": false
}
```

### Configuration Details:

1. **`discord_webhook`**  
   - **Type**: List of strings  
   - **Purpose**: Contains the URL(s) of the Discord webhook(s) to which messages are sent.  
   - **Example**: 
     ```json
     "discord_webhook": ["https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"]
     ```

2. **`send_webhook_delay`**  
   - **Type**: Float  
   - **Purpose**: Delay (in seconds) before sending a message after detecting the game UI, to prevent spamming.  
   - **Example**: 
     ```json
     "send_webhook_delay": 0.1
     ```

3. **`screenshot_delay`**  
   - **Type**: Float  
   - **Purpose**: Delay (in seconds) between detecting the UI and capturing a screenshot, ensuring the right moment is captured.  
   - **Example**: 
     ```json
     "screenshot_delay": 0.5
     ```

4. **`ping_players`**  
   - **Type**: Boolean  
   - **Purpose**: Whether to ping specific players in the Discord message. If `true`, the `player_id_to_ping` list will be used.  
   - **Example**: 
     ```json
     "ping_players": true
     ```

5. **`player_id_to_ping`**  
   - **Type**: List of strings  
   - **Purpose**: Discord IDs of players to ping in the webhook message, used if `ping_players` is set to `true`.  
   - **Example**: 
     ```json
     "player_id_to_ping": ["1234567890"]
     ```

6. **`resend_timeout`**  
   - **Type**: Integer  
   - **Purpose**: Cooldown period (in seconds) before sending another webhook message, preventing spam.  
   - **Example**: 
     ```json
     "resend_timeout": 100
     ```

7. **`screenshot_full_screen`**  
   - **Type**: Boolean  
   - **Purpose**: Whether to capture the full screen or just the Roblox window. If `true`, the full screen is captured; otherwise, only the target window is.  
   - **Example**: 
     ```json
     "screenshot_full_screen": false
     ```

--- 
