import keyboard
import mss
import mss.tools
import base64
import os
import tkinter as tk
from tkinter import scrolledtext
import threading
from groq import Groq 
import os
from dotenv import load_dotenv 

# 1. Load the secrets from the .env file
load_dotenv()

# 2. Get the key securely
# (If the key isn't found, this returns None and avoids crashing immediately)
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("No API Key found! Make sure you created a .env file.")

# 3. Use the key
client = Groq(api_key=api_key)

# We use Llama 4 Scout, which is the current fast vision model
MODEL_NAME = "meta-llama/llama-4-scout-17b-16e-instruct"

def encode_image(image_path):
    """Groq requires images to be converted to base64 text"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def show_popup(text):
    root = tk.Tk()
    root.title(f"Groq Solver ({MODEL_NAME})")
    root.geometry("500x400+50+50")
    root.attributes("-topmost", True)
    
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Segoe UI", 12))
    text_area.pack(expand=True, fill='both', padx=10, pady=10)
    text_area.insert(tk.END, text)
    text_area.configure(state='disabled')
    
    tk.Button(root, text="Close", command=root.destroy, bg="#ccffcc").pack(fill='x')
    root.mainloop()

def get_groq_response(image_path):
    try:
        # 1. Encode image to base64
        base64_image = encode_image(image_path)
        
        # 2. Send to Groq
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Read this quiz/question. Provide the correct answer and a 1-sentence explanation."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                            },
                        },
                    ],
                }
            ],
            model=MODEL_NAME,
            temperature=0.1, # Lower temperature = more precise answers
            max_tokens=1024,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Groq Error: {str(e)}"

def capture_and_solve():
    print(f"\n--- ⚡ Triggered (Model: {MODEL_NAME}) ---")
    
    # 1. Capture Screen
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)
        # Save as JPEG directly to save space
        mss.tools.to_png(screenshot.rgb, screenshot.size, output="temp_groq.png")
    
    # 2. Solve with Groq
    print(f" 🚀 Sending to AI...")
    try:
        answer = get_groq_response("temp_groq.png")
        print(" ✅ Answer Received.")
    except Exception as e:
        answer = f"Error: {e}"

    # 3. Show Popup
    threading.Thread(target=show_popup, args=(answer,)).start()

print(f"✅ System Ready: Using Groq Llama 4")
print(" -> Press 'Ctrl+Shift+Q' to capture.")
print(" -> Press 'Esc' to quit.")

keyboard.add_hotkey('ctrl+shift+q', capture_and_solve)
keyboard.wait('esc')
