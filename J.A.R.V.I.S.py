import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import pyautogui
import requests
import random
import psutil
import time
import threading
import glob
import subprocess
import os

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()

jarvis_sleeping = False

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

print("===================================")
print("      JARVIS AI ASSISTANT")
print("===================================")
speak("Jarvis is online.")

 # Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Improve microphone recognition
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8

# Calibrate microphone ONCE
with sr.Microphone() as source:
    print("Calibrating microphone...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

print("Microphone ready.")

def open_app(app):
    apps = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "google chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "explorer": "explorer.exe",
        "command prompt": "cmd.exe",
        "cmd": "cmd.exe"
    }

    app = app.lower().strip()

    if app in apps:
        try:
            subprocess.Popen(apps[app])
            speak(f"Opening {app}")
        except Exception as e:
            print(e)
            speak("I could not open that application.")
    else:
        speak("I don't know that application yet.")

def open_folder(folder_name):
    try:
        folders = {
            "desktop": "Desktop",
            "downloads": "Downloads",
            "documents": "Documents",
            "pictures": "Pictures",
            "videos": "Videos",
            "music": "Music"
        }

        folder_name = folder_name.lower().strip()

        if folder_name in folders:
            subprocess.Popen(["explorer.exe", folders[folder_name]])
            speak("Opening " + folder_name)
        else:
            speak("Folder not found.")

    except Exception as e:
        print("Folder Error:", e)
        speak("Something went wrong.")

def create_folder(folder_name):
    try:
        folder_name = folder_name.strip()

        if not folder_name:
            speak("Please provide a folder name.")
            return

        desktop = r"C:\Users\shahh\OneDrive\Desktop"
        folder_path = os.path.join(desktop, folder_name)

        os.makedirs(folder_path, exist_ok=True)

        print("Created:", folder_path)
        speak("Folder " + folder_name + " created on the desktop.")

    except Exception as e:
        print("Create Folder Error:", e)
        speak("I could not create the folder.")

def open_named_folder(folder_name):
    try:
        base_path = r"C:\Users\shahh\OneDrive\Desktop"
        folder_path = os.path.join(base_path, folder_name)

        if os.path.exists(folder_path):
            os.startfile(folder_path)
            speak("Opening " + folder_name)
        else:
            speak("I could not find the folder " + folder_name)

    except Exception as e:
        print("Open Folder Error:", e)
        speak("Something went wrong.")

while True:

#Jarvis Standby Mode
    if jarvis_sleeping:
        print("\nJarvis is sleeping...")

        with sr.Microphone() as source:
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print("You:", command)

            if "jarvis wake up" in command or "wake up jarvis" in command:
                jarvis_sleeping = False
                speak("I am awake. How can I help you?")

        except sr.UnknownValueError:
            pass

        continue

    try:

        with sr.Microphone() as source:
            print("\nListening...")

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        command = recognizer.recognize_google(audio).lower()
        print("You:", command)

        # Your existing commands start here

        # Greeting
        if "hello" in command:
            speak("Hello Sir! How can I help you?")

        elif "test voice" in command:
            print("Testing voice...")
            engine.say("This is a voice test.")
            engine.runAndWait()
            print("Voice test finished.")

        # Time
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The time is " + current_time)

        # Date
        elif "date" in command:
            today = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + today)

        # Jarvis Sleep Mode
        elif "jarvis sleep" in command:
            speak("Going into standby mode.")
            jarvis_sleeping = True

        # How are you
        elif "how are you" in command:
            speak("I am doing great. Thank you for asking.")

        # Open Google
        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        # Search Google
        elif "search google for" in command:
            search = command.replace("search google for", "")
            speak("Searching Google for " + search)
            webbrowser.open(f"https://www.google.com/search?q={search}")

        # YouTube
        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        # Google Gemini
        elif "gemini" in command:
            speak("Opening Google Gemini")
            webbrowser.open("https://gemini.google.com")

        # Calculator
        elif "open calculator" in command:
            speak("Opening Calculator")
            os.system("calc")

        # Notepad
        elif "open notepad" in command:
            speak("Opening Notepad")
            os.system("notepad")

        # File Explorer
        elif "open file explorer" in command:
            speak("Opening File Explorer")
            os.system("explorer")

        # Command Prompt
        elif "open command prompt" in command:
            speak("Opening Command Prompt")
            os.system("start cmd")

        # VS Code
        elif "open vs code" in command:
            speak("Opening Visual Studio Code")
            os.system("code")

        elif "open chrome" in command:
            open_app("chrome")

        elif "open edge" in command:
            open_app("edge")

        elif "open notepad" in command:
            open_app("notepad")

        elif "open calculator" in command:
            open_app("calculator")

        elif "open paint" in command:
            open_app("paint")

        elif "open explorer" in command:
            open_app("explorer")

        elif "open command prompt" in command or "open cmd" in command:
            open_app("cmd")

        elif "open documents" in command:
            open_folder("documents")

        elif "open desktop" in command:
            open_folder("desktop")

        elif "open pictures" in command:
            open_folder("pictures")

        elif "open videos" in command:
            open_folder("videos")

        elif "open music" in command:
            open_folder("music")

        elif "create folder" in command:
            folder_name = command.replace("create folder", "").strip()
            create_folder(folder_name)

        elif "open folder" in command:
            folder_name = command.replace("open folder", "").strip()
            open_named_folder(folder_name)

    #Screenshot
        elif "take screenshot" in command:
            image = pyautogui.screenshot()

            filename = "screenshot.png"
            image.save(filename)

            import os
            print("Saved to:", os.path.abspath(filename))

            speak("Screenshot saved.")

        # Music
        elif "play music" in command:
            speak("Opening YouTube Music")
            webbrowser.open("https://music.youtube.com")

        # Joke
        elif "tell me a joke" in command:
            speak("Why do programmers prefer dark mode? Because light attracts bugs.")

        # Shutdown
        elif "shutdown computer" in command:
            speak("Shutting down computer in ten seconds.")
            os.system("shutdown /s /t 10")

        # Restart
        elif "restart computer" in command:
            speak("Restarting computer in ten seconds.")
            os.system("shutdown /r /t 10")

        # Paint
        elif "open paint" in command:
            speak("Opening Paint")
            os.system("mspaint")

        # Camera
        elif "open camera" in command:
            speak("Opening Camera")
            os.system("start microsoft.windows.camera:")

        # Settings   
        elif "open settings" in command:
            speak("Opening Settings")
            os.system("start ms-settings:")

        # Task Manager
        elif "open task manager" in command:
            speak("Opening Task Manager")
            os.system("taskmgr")

        # Control Panel
        elif "open control panel" in command:
            speak("Opening Control Panel")
            os.system("control")

        # Lock Computer    
        elif "lock computer" in command:
            speak("Locking your computer")
            os.system("rundll32.exe user32.dll,LockWorkStation")

        # Sleep Computer    
        elif "sleep computer" in command:
            speak("Putting computer to sleep")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        # Flip Coin
        elif "flip coin" in command:
            speak(random.choice(["Heads", "Tails"]))

        # Roll Dice
        elif "roll dice" in command:
            speak(f"You got {random.randint(1,6)}")

        # Weather
        elif "weather" in command:
            speak("Please specify the city.")
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source)

            city = recognizer.recognize_google(audio).lower()
            speak("Opening weather for " + city)
            webbrowser.open(f"https://www.google.com/search?q=weather+{city}")
        elif "weather in" in command:
            city = command.replace("weather in", "").strip()
            speak("Opening weather for " + city)
            webbrowser.open(
                  f"https://www.google.com/search?q=weather+{city}" )

        # Voice Calculator
        elif "calculate" in command or "what is" in command:
            try:
                expression = command.replace("calculate", "")
                expression = expression.replace("what is", "")

                expression = expression.replace("multiplied by", "*")
                expression = expression.replace("multiply", "*")
                expression = expression.replace("times", "*")
                expression = expression.replace(" x ", "*")
                expression = expression.replace("plus", "+")
                expression = expression.replace("minus", "-")
                expression = expression.replace("divided by", "/")

                expression = expression.strip()

                result = eval(expression)

                speak(f"The answer is {result}")

            except Exception as e:
                print("Calculator error:", e)
                speak("I could not calculate that.")

        # System Status
        elif "system status" in command:
            try:
                battery = psutil.sensors_battery()
                cpu = psutil.cpu_percent()
                ram = psutil.virtual_memory().percent

                if battery:
                    battery_level = battery.percent

                    if battery.power_plugged:
                        charging = "and the laptop is charging"
                    else:
                        charging = "and the laptop is not charging"

                    speak(
                        f"Battery is {battery_level} percent, "
                        f"CPU usage is {cpu} percent, "
                        f"RAM usage is {ram} percent, "
                        f"{charging}"
                    )

                else:
                    speak(
                        f"CPU usage is {cpu} percent "
                        f"and RAM usage is {ram} percent"
                    )

            except Exception as e:
                print("System status error:", e)
                speak("I could not get the system status.")

        # Reminder
        elif "remind me" in command:
            reminder = command.replace("remind me", "").strip()

            if reminder:
                speak("Reminder saved: " + reminder)

                def reminder_message():
                    time.sleep(10)
                    speak("Reminder: " + reminder)

                threading.Thread(target=reminder_message).start()

            else:
                speak("What should I remind you about?")

        # Search File
        elif "search file" in command:
            try:
                filename = command.replace("search file", "").strip()

                speak("Searching for " + filename)

                search_path = os.path.expanduser("~")

                matches = []

                for root, dirs, files in os.walk(search_path):
                    for file in files:
                        if filename.lower() in file.lower():
                            matches.append(os.path.join(root, file))

                if matches:
                    speak(f"I found {len(matches)} files.")

                    for file in matches[:5]:
                        print(file)

                    speak("I found the files and displayed their locations on the screen.")

                else:
                    speak("I could not find that file.")

            except Exception as e:
                print("File search error:", e)
                speak("Something went wrong while searching.")

         # Media Controls
        elif "pause music" in command or "pause video" in command:
            speak("Pausing")
            pyautogui.press("playpause")

        elif "play music" in command or "resume music" in command:
            speak("Playing")
            pyautogui.press("playpause")

        elif "next song" in command or "next video" in command:
            speak("Next")
            pyautogui.press("nexttrack")

        elif "previous song" in command or "previous video" in command:
            speak("Previous")
            pyautogui.press("prevtrack")

        elif "mute" in command:
            speak("Muting")
            pyautogui.press("volumemute")

        elif "volume up" in command or "increase volume" in command:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            speak("Volume increased")

        elif "volume down" in command or "decrease volume" in command:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            speak("Volume decreased")

         # Open Downloads
        elif "open downloads" in command:
            speak("Opening Downloads")
            os.startfile(os.path.expanduser("~/Downloads"))

        # Open Documents
        elif "open documents" in command:
            speak("Opening Documents")
            os.startfile(os.path.expanduser("~/Documents"))

        # Open Desktop
        elif "open desktop" in command:
            speak("Opening Desktop")
            os.startfile(os.path.expanduser("~/Desktop"))

        # Open Pictures
        elif "open pictures" in command:
            speak("Opening Pictures")
            os.startfile(os.path.expanduser("~/Pictures"))

        # Open Videos
        elif "open videos" in command:
            speak("Opening Videos")
            os.startfile(os.path.expanduser("~/Videos"))

        # Open Music Folder
        elif "open music folder" in command:
            speak("Opening Music folder")
            os.startfile(os.path.expanduser("~/Music"))

                # Open Specific File
        elif "open file" in command:
            try:
                filename = command.replace("open file", "").strip()

                speak("Searching for " + filename)

                # Get actual user folders
                home = os.path.expanduser("~")

                search_folders = [
                    os.path.join(home, "Desktop"),
                    os.path.join(home, "OneDrive", "Desktop"),
                    os.path.join(home, "Documents"),
                    os.path.join(home, "OneDrive", "Documents"),
                    os.path.join(home, "Downloads")
                ]

                found = []

                for folder in search_folders:

                    if not os.path.exists(folder):
                        continue

                    print("Searching:", folder)

                    for root, dirs, files in os.walk(folder):

                        for file in files:

                            if filename.lower() in file.lower():

                                filepath = os.path.abspath(
                                    os.path.join(root, file)
                                )

                                if os.path.isfile(filepath):
                                    found.append(filepath)

                if found:

                    print("\nFiles found:")

                    for i, file in enumerate(found[:5], 1):
                        print(i, file)

                    filepath = found[0]

                    print("Opening:", filepath)

                    speak("File found. Opening it.")

                    os.startfile(filepath)

                else:
                    print("No file found.")
                    speak("I could not find that file.")

            except Exception as e:
                print("File error:", e)
                speak("Something went wrong.")

                # Create Text File
        elif "create text file" in command:
            try:
                filename = command.replace("create text file", "").strip()

                if not filename:
                    speak("Please tell me the file name.")
                    continue

                if not filename.endswith(".txt"):
                    filename += ".txt"

                home = os.path.expanduser("~")

               # Check possible Desktop locations
                desktop_locations = [
                    os.path.join(home, "Desktop"),
                    os.path.join(home, "OneDrive", "Desktop")
                ]

                desktop = None

                for location in desktop_locations:
                    if os.path.exists(location):
                        desktop = location
                        break

                if desktop is None:
                    speak("I could not find your Desktop folder.")
                    print("Desktop folder not found.")
                    continue

                filepath = os.path.join(desktop, filename)

                with open(filepath, "w", encoding="utf-8") as file:
                    file.write("")

                print("Created:", filepath)
                speak("Text file created successfully.")

            except Exception as e:
                print("Text file error:", e)
                speak("I could not create the text file.")

               # Write to Text File
        elif (
            "write to" in command
            or "write two" in command
            or "right to" in command
            or "right two" in command
        ):
            try:
                filename = command

                filename = filename.replace("write to", "")
                filename = filename.replace("write two", "")
                filename = filename.replace("right to", "")
                filename = filename.replace("right two", "")

                filename = filename.strip()

                if not filename:
                    speak("Please tell me the file name.")
                    continue

                if not filename.endswith(".txt"):
                    filename += ".txt"

                home = os.path.expanduser("~")

                desktop_locations = [
                    os.path.join(home, "Desktop"),
                    os.path.join(home, "OneDrive", "Desktop")
                ]

                desktop = None

                for location in desktop_locations:
                    if os.path.exists(location):
                        desktop = location
                        break

                if desktop is None:
                    speak("I could not find your Desktop folder.")
                    print("Desktop folder not found.")
                    continue

                filepath = os.path.join(desktop, filename)

                if not os.path.exists(filepath):
                    speak("That text file does not exist.")
                    continue

                speak("I am listening. Tell me what to write.")

                with sr.Microphone() as source:
                    print("Listening for text...")
                    audio = recognizer.listen(
                        source,
                        timeout=5,
                        phrase_time_limit=30
                    )

                text = recognizer.recognize_google(audio)

                print("Text:", text)

                with open(filepath, "a", encoding="utf-8") as file:
                    file.write(text + "\n")

                speak("Text written successfully.")

            except sr.UnknownValueError:
                speak("I could not understand the text.")

            except Exception as e:
                print("Write file error:", e)
                speak("I could not write to the file.")

                        # Read Text File
        elif "read" in command:
            try:
                filename = command.replace("read", "").strip()

                if not filename:
                    speak("Please tell me the file name.")
                    continue

                if not filename.endswith(".txt"):
                    filename += ".txt"

                home = os.path.expanduser("~")

                desktop_locations = [
                    os.path.join(home, "Desktop"),
                    os.path.join(home, "OneDrive", "Desktop")
                ]

                filepath = None

                for desktop in desktop_locations:
                    possible_file = os.path.join(desktop, filename)

                    if os.path.exists(possible_file):
                        filepath = possible_file
                        break

                if filepath is None:
                    speak("I could not find that text file.")
                    continue

                with open(filepath, "r", encoding="utf-8") as file:
                    text = file.read()

                if not text.strip():
                    speak("The file is empty.")
                    continue

                print("\nFile contents:")
                print(text)

                # Read the file aloud
                speak(text)

            except Exception as e:
                print("Read file error:", e)
                speak("I could not read the file.")
               
            # Rename Text File
        elif "rename file" in command:
            try:
                text = command.replace("rename file", "").strip()

                if " to " not in text:
                    speak("Please say the old name and the new name.")
                    continue

                old_name, new_name = text.split(" to ", 1)

                old_name = old_name.strip()
                new_name = new_name.strip()

                if not old_name or not new_name:
                    speak("Please provide both file names.")
                    continue

                if not old_name.endswith(".txt"):
                    old_name += ".txt"

                if not new_name.endswith(".txt"):
                    new_name += ".txt"

                home = os.path.expanduser("~")

                desktop_locations = [
                    os.path.join(home, "Desktop"),
                    os.path.join(home, "OneDrive", "Desktop")
                ]

                old_path = None

                for desktop in desktop_locations:
                    possible_path = os.path.join(desktop, old_name)

                    if os.path.exists(possible_path):
                        old_path = possible_path
                        break

                if old_path is None:
                    speak("I could not find the file.")
                    continue

                new_path = os.path.join(
                    os.path.dirname(old_path),
                    new_name
                )

                if os.path.exists(new_path):
                    speak("A file with the new name already exists.")
                    continue

                os.rename(old_path, new_path)

                print("Renamed:")
                print(old_path)
                print("to")
                print(new_path)

                speak("File renamed successfully.")

            except Exception as e:
                print("Rename error:", e)
                speak("I could not rename the file.")

                # Move File
        elif "move file" in command:
            try:
                text = command.replace("move file", "").strip()

                if " to " not in text:
                    speak("Please say the file name and destination folder.")
                    continue

                filename, folder_name = text.split(" to ", 1)

                filename = filename.strip()
                folder_name = folder_name.strip()

                if not filename or not folder_name:
                    speak("Please provide both names.")
                    continue

                if not filename.endswith(".txt"):
                    filename += ".txt"

                home = os.path.expanduser("~")

                desktop_locations = [
                    os.path.join(home, "Desktop"),
                    os.path.join(home, "OneDrive", "Desktop")
                ]

                desktop = None

                for location in desktop_locations:
                    if os.path.exists(location):
                        desktop = location
                        break

                if desktop is None:
                    speak("I could not find your Desktop.")
                    continue

                # Find the file
                source = None

                for root, dirs, files in os.walk(desktop):
                    if filename in files:
                        source = os.path.join(root, filename)
                        break

                if source is None:
                    speak("I could not find that file.")
                    continue

                # Find destination folder
                destination = os.path.join(desktop, folder_name)

                if not os.path.exists(destination):
                    speak("I could not find that folder.")
                    continue

                new_path = os.path.join(destination, filename)

                if os.path.exists(new_path):
                    speak("That file already exists in the destination folder.")
                    continue

                os.rename(source, new_path)

                print("Moved:", source)
                print("To:", new_path)

                speak("File moved successfully.")

            except Exception as e:
                print("Move file error:", e)
                speak("I could not move the file.")
         
        # Exit
        elif "exit" in command or "goodbye" in command:
            speak("Goodbye Sir.")
            break
        else:
            speak("Sorry, I don't know that command yet.")

    except sr.UnknownValueError:
        speak("Please repeat that.")

    except Exception as e:
        print(e)
        speak("Something went wrong.")
