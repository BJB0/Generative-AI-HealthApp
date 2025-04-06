# Gemini Health App – Calorie Advisor  
**LLM Project | Powered by Google Gemini Pro Vision**

This repository contains a Streamlit-based AI application that uses Google Gemini Pro Vision (Large Image Models) to analyze food images and estimate total calorie intake. The model also provides a breakdown of each food item's nutritional content based on visual analysis.

---

## ✨ Features

- 🧠 Food image recognition using Google Gemini Pro Vision  
- 🔍 Calorie estimation based on visual input  
- 📝 Detailed breakdown of food items with individual calorie counts  
- 🖼️ Upload images in JPG, JPEG, or PNG format  
- ⚡ Interactive and simple web interface using Streamlit

---

## 🛠️ Technology Stack

- Python 3.x  
- Streamlit  
- Google Gemini Pro Vision API  
- Pillow (for image handling)  
- python-dotenv (for managing API keys securely)

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/gemini-calorie-advisor.git
   cd gemini-calorie-advisor


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

1.Upload a medical image (e.g., X-ray, MRI, dermatological photo).

2.The app processes the image and sends it to the Gemini Pro Vision model.

3.The model returns structured health insights and suggestions.

4.Results are displayed in a user-friendly Streamlit interface.
 


