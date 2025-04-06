# Generative AI Health App  
**LLM Project | Powered by Google Gemini Pro Vision**

This repository contains a generative AI-powered health assistant application that utilizes Google Gemini Pro Vision (Large Image Models) to analyze medical images and provide intelligent health-related insights and recommendations. The project combines multimodal large language model capabilities with practical healthcare applications.

---

## ✨ Features

- 🧠 Medical image analysis using Google Gemini Pro Vision  
- 💬 Natural language interface for health-related queries  
- 📄 AI-generated health reports and suggestions  
- 🖼️ Multimodal interaction combining image and text input  
- 🩺 Useful for early-stage screening and monitoring

---

## 🛠️ Technology Stack

- Python 3.x  
- Streamlit (for interactive web interface)  
- Google Gemini Pro Vision API  
- Pillow / OpenCV for image processing  
- python-dotenv for environment variable management

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/generative-ai-health-app.git
   cd generative-ai-health-app

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
 


