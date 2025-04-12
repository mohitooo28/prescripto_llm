# Prescripto - Medical Symptom Analyzer

A web application that uses Google's Gemini AI to analyze symptoms and provide information about potential common conditions, treatment options, and self-care advice.

## 📋 Overview

Prescripto is a Flask-based web application that allows users to enter their symptoms and receive:

- 🩺 **Suggested condition diagnosis** for common, non-serious ailments.
- 📖 **Brief descriptions** of the potential conditions.
- 💊 **Recommended over-the-counter medications**.
- 🏡 **Self-care tips** for managing conditions at home.

The application leverages Google's Gemini 1.5 Pro model to analyze user input and generate appropriate medical information.

## ⚠️ Important Disclaimer

> **This application is intended for educational and informational purposes only.**  
It is **not a substitute for professional medical advice, diagnosis, or treatment**. Always seek guidance from a qualified healthcare provider for medical concerns.

## 🚀 Features

- 💡 Clean, responsive UI with **Light/Dark mode toggle**.
- 🤖 Real-time symptom analysis using **Google Gemini AI**.
- 📋 Structured results: **condition, description, medications, self-care tips**.
- 📱 **Mobile-friendly** design with **Tailwind CSS**.
- ⚡ Robust **error handling** for API failures and edge cases.

## 🔧 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/mohitooo28/prescripto_llm.git
cd prescripto-llm
```


2. Create a virtual environment and activate it:
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```


3. Install the dependencies:
```bash
pip install -r requirements.txt
```


4. Create a `.env` file in the root directory by copying `.env_example`:
```bash
cp .env_example .env
```


5. Add your Google Gemini API key to the `.env` file:
```
GEMINI_API_KEY=your_api_key_here
```

## 🏃‍♂️ Running the Application

Start the Flask development server:
```bash
python app.py
```

The application will be available at http://127.0.0.1:5000/

## 💻 Usage

- Enter your **symptoms** in the input field on the homepage.
- Click the **"Predict"** button to analyze your symptoms.
- View AI-generated:
  - Condition suggestion.
  - Short description.
  - Recommended medications.
  - Self-care advice.
- Click **"Clear"** to reset the form and start over.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, JavaScript, Tailwind CSS
- **AI**: Google Gemini 1.5 Pro
- **Dependencies**: dotenv, google-generativeai

## 📝 License

[MIT License](LICENSE)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/mohitooo28/prescripto_llm/issues) if you want to contribute.

## 📌 Acknowledgments

- 🚀 Thanks to **Google Gemini AI** for powering symptom analysis.
- 🐍 **Flask** for the web framework.
- 🎨 **Tailwind CSS** for the sleek and responsive design.

---

Stay healthy and code happy! 💖
