# 🥗 Gemini Health App - Calorie Advisor

A smart and interactive AI-powered web app that analyzes food images and estimates their total calories using Google Gemini Pro Vision. It also provides health insights based on the detected food items.

Built with **Streamlit**, this app is designed for anyone who wants quick and insightful nutritional analysis from just an image!

---

## 🚀 Features

- 📸 Upload a food image (JPEG/PNG)
- 🍔 Detects and lists all visible food items
- 🔢 Estimates calorie count for each item
- ✅ Calculates total calorie intake
- ⚖️ Analyzes whether the meal is healthy or not
- 💡 Suggests ways to make unhealthy meals healthier
- 🧠 Clear, emoji-enhanced, point-wise breakdown

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend AI**: [Google Gemini Pro Vision](https://ai.google.dev/)
- **Image Processing**: Pillow (PIL)
- **Env Management**: python-dotenv

---

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/gemini-health-app.git
   cd gemini-health-app



2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Configure API Keys
     Create a .env file and add your Google Gemini Pro Vision API credentials:**
```bash
   GEMINI_API_KEY=your_api_key_here
```

4.**Run the application**
```bash
streamlit run app.py
```

## ⚙️ How It Works

1.Upload an image.

2.The app processes the image and sends it to the Gemini Pro Vision model.

3.The model returns structured health insights and suggestions.

4.Results are displayed in a user-friendly Streamlit interface.
 


