# 🧠 NeuralLens: AI Screen Assistant

**NeuralLens** is a lightning-fast desktop tool that uses Multimodal AI to "see" your screen and answer questions instantly. Built with Python, it captures your display, processes the image using **Groq (Llama 4)** or **Google Gemini**, and overlays the solution in a minimal pop-up window.

![Demo](https://via.placeholder.com/800x400?text=NeuralLens+Demo+Screenshot+Here) 
*(Add a screenshot of your tool in action here!)*

## 🚀 Features

* **Instant Screen Capture:** Snaps your screen in milliseconds using `mss`.
* **AI Vision Power:** Uses **Llama 4 (via Groq)** for ultra-fast inference or **Gemini 1.5 Flash** for high accuracy.
* **Overlay UI:** Displays answers in a "Stay-on-Top" window so you never have to Alt-Tab.
* **Global Hotkey:** Trigger it anytime with `Ctrl+Shift+Q`.
* **Optimized Performance:** Auto-compresses images to minimize API latency.

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Vision AI:** Groq API (Llama 4) / Google Gemini API
* **GUI:** Tkinter (Native Python UI)
* **Screen Capture:** MSS (Multiple Screen Shots)
* **Inputs:** Keyboard module for global hotkeys

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/NeuralLens.git](https://github.com/yourusername/NeuralLens.git)
    cd NeuralLens
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your API Keys:**
    * Create a file named `.env` in the project root.
    * Add your API key (Get one from [Groq Console](https://console.groq.com) or [Google AI Studio](https://aistudio.google.com)):
    ```ini
    GROQ_API_KEY=gsk_your_key_here
    # OR
    GOOGLE_API_KEY=AIza_your_key_here
    ```

## 🎮 Usage

1.  Run the script:
    ```bash
    python main.py
    ```
2.  Open a quiz, test, or coding problem on your screen.
3.  Press **`Ctrl + Shift + Q`**.
4.  Wait a few seconds for the AI to analyze and display the answer in the popup.
5.  Press **`Esc`** to quit the program.

## ⚠️ Disclaimer
This tool is intended for educational purposes, productivity, and study assistance. Please respect academic integrity guidelines and do not use this tool during proctored exams.

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📄 License
[MIT](https://choosealicense.com/licenses/mit/)
