import pyttsx3
import speech_recognition as sr
from pathlib import Path
from datetime import datetime
import webbrowser
import time


WAKE_WORDS = ["Hello jhon", "john", "yo john", "Hey jon"]
WAKE_WORDS = [word.lower() for word in WAKE_WORDS]



def speak(text):
    print("jhon:", text)


# =========================
# TEXT TO SPEECH
# =========================
engine = pyttsx3.init()
engine.setProperty("rate", 170) 
engine.setProperty("volume", 1.0)

def speak(text):
    print("Jhon:", text)
    engine.say(text)
    engine.runAndWait()

# =========================
# SPEECH TO TEXT
# =========================
recognizer = sr.Recognizer()
mic = sr.Microphone()

def listen():
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="us-US")
        print("You: ", text)
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Speech recognition service error")
        return ""

# =========================
# COMMAND HANDLER
# =========================
def handle_command(text):
    if not text:
        return

    if "halo" in text or "hello" in text:
        speak("hello, sir im active")

    elif "jam berapa" in text:
        now = datetime.now().strftime("%H:%M")
        speak(f"Sekarang jam {now}")

    elif "tanggal berapa" in text:
        today = datetime.now().strftime("%d %B %Y")
        speak(f"Hari ini tanggal {today}")

    elif "keluar" in text or "exit" in text:
        speak("Goodbye")
        raise SystemExit

    else:
        speak("sorry sir i cant understand")

# =========================
# DIRECTORY FUNCTION
# =========================
def create_directory(dir_name):
    path = Path(dir_name)
    path.mkdir(parents=True, exist_ok=True)
    print(f"Directory '{dir_name}' created or already exists.")
    return path

# =========================
# MAIN
# =========================
def handle_command(text):
    if not text:
        return

    wake = None
    for w in WAKE_WORDS:
        if w in text:
            wake = w
            break

    if not wake:
        print("(wake word tidak terdeteksi)")
        return

    cmd = text.replace(wake, "").strip()
    now = datetime.now()

    if "buka youtube" in cmd or "open youtube" in cmd or "can you open youtube for me" in cmd or "could you open youtube for me" in cmd or "please open youtube" in cmd:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "search di google" in cmd or "search on google" in cmd or "can you open google for me" in cmd or "could you open google for me" in cmd or "please open google" in cmd or "buka google" in cmd or "open google" in cmd:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "jam berapa" in cmd or "what time is it" in cmd or "tell me the time" in cmd or "jam berapa sekarang" in cmd or "sekarang jam berapa" in cmd:
        speak(f"Sekarang jam {now.strftime('%H:%M')}")

    elif "tanggal berapa" in cmd or "what date is it" in cmd or "tell me the date" in cmd or "tanggal berapa sekarang" in cmd or "sekarang tanggal berapa" in cmd:
        speak(now.strftime("Tanggal %d %B %Y"))

    elif "buka whatsapp" in cmd or "open whatsapp" in cmd or "can you open whatsapp for me" in cmd or "could you open whatsapp for me" in cmd or "please open whatsapp" in cmd:
        webbrowser.open("https://web.whatsapp.com")
        speak("Opening WhatsApp")

    elif "buka tiktok" in cmd or "open tiktok" in cmd or "can you open tiktok for me" in cmd or "could you open tiktok for me" in cmd or "please open tiktok" in cmd:
        webbrowser.open("https://www.tiktok.com")
        speak("Opening TikTok")

    elif "buka instagram" in cmd or "open instagram" in cmd or "can you open instagram for me" in cmd or "could you open instagram for me" in cmd or "please open instagram" in cmd:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram")

    elif "buka facebook" in cmd or "open facebook" in cmd or "can you open facebook for me" in cmd or "could you open facebook for me" in cmd or "please open facebook" in cmd:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")

    elif "buka github" in cmd or "open github" in cmd or "can you open github for me" in cmd or "could you open github for me" in cmd or "please open github" in cmd:
        webbrowser.open("https://www.github.com")
        speak("Opening GitHub")

    elif "chatgpt" in cmd or "open chatgpt" in cmd or "can you open chatgpt for me" in cmd or "could you open chatgpt for me" in cmd or "please open chatgpt" in cmd:
        webbrowser.open("https://chat.openai.com")
        speak("Opening ChatGPT")

    elif "buka twitter" in cmd or "open twitter" in cmd or "can you open twitter for me" in cmd or "could you open twitter for me" in cmd or "please open twitter" in cmd or "buka x" in cmd or "open x" in cmd:
        webbrowser.open("https://www.twitter.com")
        speak("Opening Twitter")

    elif "spotify" in cmd or "open spotify" in cmd or "can you open spotify for me" in cmd or "could you open spotify for me" in cmd or "please open spotify" in cmd:
        webbrowser.open("https://www.spotify.com")
        speak("Opening Spotify")

    elif "telegram" in cmd or "open telegram" in cmd or "can you open telegram for me" in cmd or "could you open telegram for me" in cmd or "please open telegram" in cmd:
        webbrowser.open("https://web.telegram.org")
        speak("Opening Telegram")

    elif "buka github" in cmd or "open github" in cmd or "can you open github for me" in cmd or "could you open github for me" in cmd or "please open github" in cmd:
        webbrowser.open("https://www.github.com")
        speak("Opening GitHub")

    elif "snapchat" in cmd or "open snapchat" in cmd or "can you open snapchat for me" in cmd or "could you open snapchat for me" in cmd or "please open snapchat" in cmd:
        webbrowser.open("https://www.snapchat.com")
        speak("Opening Snapchat")

    elif "threads" in cmd or "open threads" in cmd or "can you open threads for me" in cmd or "could you open threads for me" in cmd or "please open threads" in cmd:
        webbrowser.open("https://www.threads.net")
        speak("Opening Threads")

    elif "linkedin" in cmd or "open linkedin" in cmd or "can you open linkedin for me" in cmd or "could you open linkedin for me" in cmd or "please open linkedin" in cmd:
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn")

    elif "buka gmail" in cmd or "open gmail" in cmd or "can you open gmail for me" in cmd or "could you open gmail for me" in cmd or "please open gmail" in cmd:
        webbrowser.open("https://mail.google.com")
        speak("Opening Gmail")

    elif "buka drive" in cmd or "open drive" in cmd or "can you open drive for me" in cmd or "could you open drive for me" in cmd or "please open drive" in cmd:
        webbrowser.open("https://drive.google.com")
        speak("Opening Google Drive")

    elif "buka maps" in cmd or "open maps" in cmd or "can you open maps for me" in cmd or "could you open maps for me" in cmd or "please open maps" in cmd:
        webbrowser.open("https://maps.google.com")
        speak("Opening Google Maps")

    elif "quran" in cmd or "open quran" in cmd or "can you open quran for me" in cmd or "could you open quran for me" in cmd or "please open quran" in cmd:
        webbrowser.open("https://quran.com")
        speak("Opening Quran.com")

    elif "buka calculator" in cmd or "open calculator" in cmd or "can you open calculator for me" in cmd or "could you open calculator for me" in cmd or "please open calculator" in cmd:
        path = create_directory("MyFolder")
        speak(f"Opening Calculator at {path.resolve()}")

    elif "buka notepad" in cmd or "open notepad" in cmd or "can you open notepad for me" in cmd or "could you open notepad for me" in cmd or "please open notepad" in cmd:
        path = create_directory("MyFolder")
        speak(f"Opening Notepad at {path.resolve()}")

    elif "buka paint" in cmd or "open paint" in cmd or "can you open paint for me" in cmd or "could you open paint for me" in cmd or "please open paint" in cmd:
        path = create_directory("MyFolder")
        speak(f"Opening Paint at {path.resolve()}")

    elif "buka cmd" in cmd or "open cmd" in cmd or "can you open cmd for me" in cmd or "could you open cmd for me" in cmd or "please open cmd" in cmd or "buka command prompt" in cmd or "open command prompt" in cmd:
        path = create_directory("MyFolder")
        speak(f"Opening Command Prompt at {path.resolve()}")

    elif "buka powershell" in cmd or "open powershell" in cmd or "can you open powershell for me" in cmd or "could you open powershell for me" in cmd or "please open powershell" in cmd:
        path = create_directory("MyFolder")
        speak(f"Opening PowerShell at {path.resolve()}")

    elif "buka control panel" in cmd or "open control panel" in cmd or "can you open control panel for me" in cmd or "could you open control panel for me" in cmd or "please open control panel" in cmd:
        path = create_directory("MyFolder")
        speak(f"Opening Control Panel at {path.resolve()}")

    elif "buka task manager" in cmd or "open task manager" in cmd or "can you open task manager for me" in cmd or "could you open task manager for me" in cmd or "please open task manager" in cmd:
        path = create_directory("MyFolder")
        speak(f"Opening Task Manager at {path.resolve()}")

    elif "buka settings" in cmd or "open settings" in cmd or "can you open settings for me" in cmd or "could you open settings for me" in cmd or "please open settings" in cmd:
        path = create_directory("MyFolder")
        speak(f"Opening Settings at {path.resolve()}")

    elif "buka control center" in cmd or "open control center" in cmd or "can you open control center for me" in cmd or "could you open control center for me" in cmd or "please open control center" in cmd:
        path = create_directory("MyFolder")
        speak(f"Opening Control Center at {path.resolve()}")

    elif "buka device manager" in cmd or "open device manager" in cmd or "can you open device manager for me" in cmd or "could you open device manager for me" in cmd or "please open device manager" in cmd:
        path = create_directory("MyFolder")
        speak(f"Opening Device Manager at {path.resolve()}")

    elif "buka disk management" in cmd or "open disk management" in cmd or "can you open disk management for me" in cmd or "could you open disk management for me" in cmd or "please open disk management" in cmd:
        path = create_directory("MyFolder")
        speak(f"Opening Disk Management at {path.resolve()}")

    elif "buka task scheduler" in cmd or "open task scheduler" in cmd or "can you open task scheduler for me" in cmd or "could you open task scheduler for me" in cmd or "please open task scheduler" in cmd:
        path = create_directory("MyFolder")
        speak(f"Opening Task Scheduler at {path.resolve()}")

    elif "buka calendar" in cmd or "open calendar" in cmd or "can you open calendar for me" in cmd or "could you open calendar for me" in cmd or "please open calendar" in cmd:
        path = create_directory("MyFolder")
        speak(f"Opening Calendar at {path.resolve()}")

    elif "buka lineage" in cmd or "open lineage" in cmd or "can you open lineage for me" in cmd or "could you open lineage for me" in cmd or "please open lineage" in cmd:
        path = create_directory("MyFolder")
        speak(f"Opening Lineage at {path.resolve()}")

    elif "buka kamera" in cmd or "open camera" in cmd or "can you open camera for me" in cmd or "could you open camera for me" in cmd or "please open camera" in cmd:
        path = create_directory("MyFolder")
        speak(f"Opening Camera at {path.resolve()}")

    elif "buka Line" in cmd or "open Line" in cmd or "can you open Line for me" in cmd or "could you open Line for me" in cmd or "please open Line" in cmd:
        webbrowser.open("https://line.me/en/")
        speak("Opening Line App")

    elif "buka discord" in cmd or "open discord" in cmd or "can you open discord for me" in cmd or "could you open discord for me" in cmd or "please open discord" in cmd:
        webbrowser.open("https://discord.com/app")
        speak("Opening Discord")

    elif "buka skype" in cmd or "open skype" in cmd or "can you open skype for me" in cmd or "could you open skype for me" in cmd or "please open skype" in cmd:
        webbrowser.open("https://web.skype.com")
        speak("Opening Skype")

    elif "web browser" in cmd or "open web browser" in cmd or "can you open web browser for me" in cmd or "could you open web browser for me" in cmd or "please open web browser" in cmd or "buka web browser" in cmd or "buka browser" in cmd or "open browser" in cmd:
        path = create_directory("MyFolder")
        speak(f"Opening Web Browser at {path.resolve()}")

    elif "buka we chat" in cmd or "open we chat" in cmd or "can you open we chat for me" in cmd or "could you open we chat for me" in cmd or "please open we chat" in cmd:
        webbrowser.open("https://web.wechat.com")
        speak("Opening WeChat")

    elif "agma" in cmd or "open agma" in cmd or "can you open agma for me" in cmd or "could you open agma for me" in cmd or "please open agma" in cmd:
        webbrowser.open("https://agma.io")
        speak("Opening Agma")

    elif "slither io" in cmd or "open slither io" in cmd or "can you open slither io for me" in cmd or "could you open slither io for me" in cmd or "please open slither io" in cmd:
        webbrowser.open("https://slither.io")
        speak("Opening Slither.io")

    elif "pinterest" in cmd or "open pinterest" in cmd or "can you open pinterest for me" in cmd or "could you open pinterest for me" in cmd or "please open pinterest" in cmd:
        webbrowser.open("https://www.pinterest.com")
        speak("Opening Pinterest")

    elif "twitch" in cmd or "open twitch" in cmd or "can you open twitch for me" in cmd or "could you open twitch for me" in cmd or "please open twitch" in cmd:
        webbrowser.open("https://www.twitch.tv")
        speak("Opening Twitch")

    elif "minecraft" in cmd or "open minecraft" in cmd or "can you open minecraft for me" in cmd or "could you open minecraft for me" in cmd or "please open minecraft" in cmd:
        webbrowser.open("https://www.minecraft.net")
        speak("Opening Minecraft")

    elif "tokopedia" in cmd or "open tokopedia" in cmd or "can you open tokopedia for me" in cmd or "could you open tokopedia for me" in cmd or "please open tokopedia" in cmd:
        webbrowser.open("https://www.tokopedia.com")
        speak("Opening Tokopedia")

    elif "shopee" in cmd or "open shopee" in cmd or "can you open shopee for me" in cmd or "could you open shopee for me" in cmd or "please open shopee" in cmd:
        webbrowser.open("https://www.shopee.com")
        speak("Opening Shopee")

    elif "bukalapak" in cmd or "open bukalapak" in cmd or "can you open bukalapak for me" in cmd or "could you open bukalapak for me" in cmd or "please open bukalapak" in cmd:
        webbrowser.open("https://www.bukalapak.com")
        speak("Opening Bukalapak")

    elif "roblox" in cmd or "open roblox" in cmd or "can you open roblox for me" in cmd or "could you open roblox for me" in cmd or "please open roblox" in cmd:
        webbrowser.open("https://www.roblox.com")
        speak("Opening Roblox")

    elif "agar io" in cmd or "open agar io" in cmd or "can you open agar io for me" in cmd or "could you open agar io for me" in cmd or "please open agar io" in cmd:
        webbrowser.open("https://agar.io")
        speak("Opening Agar.io")

    elif "crazy games" in cmd or "open crazy games" in cmd or "can you open crazy games for me" in cmd or "could you open crazy games for me" in cmd or "please open crazy games" in cmd:
        webbrowser.open("https://www.crazygames.com")
        speak("Opening Crazy Games")

    elif "duolingo" in cmd or "open duolingo" in cmd or "can you open duolingo for me" in cmd or "could you open duolingo for me" in cmd or "please open duolingo" in cmd:
        webbrowser.open("https://www.duolingo.com")
        speak("Opening Duolingo")

    elif "ruangguru" in cmd or "open ruangguru" in cmd or "can you open ruangguru for me" in cmd or "could you open ruangguru for me" in cmd or "please open ruangguru" in cmd:
        webbrowser.open("https://www.ruangguru.com")
        speak("Opening Ruangguru")

    elif "gojek" in cmd or "open gojek" in cmd or "can you open gojek for me" in cmd or "could you open gojek for me" in cmd or "please open gojek" in cmd:
        webbrowser.open("https://www.gojek.com")
        speak("Opening Gojek")

    elif "grab" in cmd or "open grab" in cmd or "can you open grab for me" in cmd or "could you open grab for me" in cmd or "please open grab" in cmd:
        webbrowser.open("https://www.grab.com")
        speak("Opening Grab")

    elif "uber" in cmd or "open uber" in cmd or "can you open uber for me" in cmd or "could you open uber for me" in cmd or "please open uber" in cmd:
        webbrowser.open("https://www.uber.com")
        speak("Opening Uber")

    elif "wikipedia" in cmd or "open wikipedia" in cmd or "can you open wikipedia for me" in cmd or "could you open wikipedia for me" in cmd or "please open wikipedia" in cmd:
        webbrowser.open("https://www.wikipedia.org")
        speak("Opening Wikipedia")

    elif "gotrade" in cmd or "open gotrade" in cmd or "can you open gotrade for me" in cmd or "could you open gotrade for me" in cmd or "please open gotrade" in cmd:
        webbrowser.open("https://www.gotrade.com")
        speak("Opening GoTrade")

    elif "stockbit" in cmd or "open stockbit" in cmd or "can you open stockbit for me" in cmd or "could you open stockbit for me" in cmd or "please open stockbit" in cmd:
        webbrowser.open("https://www.stockbit.com")
        speak("Opening Stockbit")

    elif "amazon" in cmd or "open amazon" in cmd or "can you open amazon for me" in cmd or "could you open amazon for me" in cmd or "please open amazon" in cmd:
        webbrowser.open("https://www.amazon.com")
        speak("Opening Amazon")

    elif "madrsah pembangunan uin" in cmd or "open madrsah pembangunan uin" in cmd or "can you open madrsah pembangunan uin for me" in cmd or "could you open madrsah pembangunan uin for me" in cmd or "please open madrsah pembangunan uin" in cmd or "buka mp" in cmd or "open mp" in cmd or "buka madrsah pembangunan uin" in cmd:
        webbrowser.open("https://mpuin-jkt.sch.id/")
        speak("Opening Madrsah Pembangunan UIN")

    elif "buka file explorer" in cmd or "open file explorer" in cmd or "can you open file explorer for me" in cmd or "could you open file explorer for me" in cmd or "please open file explorer" in cmd or "buka explorer" in cmd or "open explorer" in cmd or "open file manager" in cmd or "buka file manager" in cmd or "open explorer" in cmd:
        path = create_directory("MyFolder")
        speak(f"Opening File Explorer at {path.resolve()}")

    elif "El rasyad" in cmd or "open El rasyad" in cmd or "can you open El rasyad for me" in cmd or "could you open El rasyad for me" in cmd or "please open El rasyad" in cmd or "buka El rasyad" in cmd:
        webbrowser.open("https://elrasyad.sch.id/")
        speak("Opening El Rasyad School")

    elif "sd islam abu bakar" in cmd or "open sd islam abu bakar" in cmd or "can you open sd islam abu bakar for me" in cmd or "could you open sd islam abu bakar for me" in cmd or "please open sd islam abu bakar" in cmd or "buka sd islam abu bakar" in cmd:
        webbrowser.open("https://abubakar.sch.id/")
        speak("Opening SD Islam Abu Bakar School")

    elif "OPEN BANK INDONESIA" in cmd or "open bank indonesia" in cmd or "can you open bank indonesia for me" in cmd or "could you open bank indonesia for me" in cmd or "please open bank indonesia" in cmd or "buka bank indonesia" in cmd:
        webbrowser.open("https://www.bi.go.id/id/Default.aspx")
        speak("Opening Bank Indonesia")

    elif "OPEN LINtasarta" in cmd or "open lintasarta" in cmd or "can you open lintasarta for me" in cmd or "could you open lintasarta for me" in cmd or "please open lintasarta" in cmd or "buka lintasarta" in cmd:
        webbrowser.open("https://www.lintasarta.net/")
        speak("Opening Lintasarta")

    elif "kuricang" in cmd or "open kuricang" in cmd or "can you open kuricang for me" in cmd or "could you open kuricang for me" in cmd or "please open kuricang" in cmd or "buka kuricang" in cmd:
        webbrowser.open("https://kuricang.com/")
        speak("Opening Kuricang")

    elif "bing" in cmd or "open bing" in cmd or "can you open bing for me" in cmd or "could you open bing for me" in cmd or "please open bing" in cmd or "buka bing" in cmd:
        webbrowser.open("https://www.bing.com")
        speak("Opening Bing")

    elif "canva" in cmd or "open canva" in cmd or "can you open canva for me" in cmd or "could you open canva for me" in cmd or "please open canva" in cmd or "buka canva" in cmd:
        webbrowser.open("https://www.canva.com")
        speak("Opening Canva")

    elif "apple" in cmd or "open apple" in cmd or "can you open apple for me" in cmd or "could you open apple for me" in cmd or "please open apple" in cmd or "buka apple" in cmd:
        webbrowser.open("https://www.apple.com")
        speak("Opening Apple")

    elif "smu singapore" in cmd or "open smu singapore" in cmd or "can you open smu singapore for me" in cmd or "could you open smu singapore for me" in cmd or "please open smu singapore" in cmd or "buka smu singapore" in cmd or "buka smu" in cmd or "open smu" in cmd:
        webbrowser.open("https://www.smu.edu.sg")
        speak("Opening SMU Singapore")

    elif "Nus" in cmd or "open Nus" in cmd or "buka Nus" in cmd:
        webbrowser.open("https://nus.edu.sg/")
        speak("opening Nus")


    elif "exit" in cmd or "keluar" in cmd or "quit" in cmd or "exid" in cmd or "wick" in cmd:
        speak("Goodbye")
        raise SystemExit

    else:
        speak("sorry sir i cant understand")  

if __name__ == "__main__":
    speak("hello sir im Active")
    while True:
        text = listen()
        handle_command(text)
        time.sleep(0.1)