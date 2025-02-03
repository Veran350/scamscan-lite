# 🔍 ScamScan Lite  
*A minimalist web app to detect potential scam websites. Use responsibly.*  

![ScamScan Banner](https://via.placeholder.com/1500x500.png?text=ScamScan+Lite+-+Detect+Scam+Sites+🚨)  
*Banner Placeholder: Replace with your own image/video link.*  

---

## 🚀 **Features**  
- **Domain Age Check**: Flags domains registered <6 months ago.  
- **VirusTotal Integration**: Scans for malware/suspicious activity.  
- **Google Safe Browsing**: Checks against blacklisted URLs.  
- **Simple UI**: No bloat, just results.  

[![Demo GIF](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3ZxejN4eGJ1eGx2aHk0eWh2Y3N1eWJjcjRzZGx1eTZ0b2Vnb2V0dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7btT1T9qpQZRqGF2/giphy.gif)](https://example.com/demo-video)  
*Click GIF for demo video (replace with your link).*

---

## ⚙️ **Installation**  
1. **Clone the repo**:  
   ```bash  
   git clone https://github.com/yourusername/scamscan-lite.git  
   cd scamscan-lite  
   ```  
2. **Install dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. **Set up API keys**:  
   - Sign up for [VirusTotal](https://www.virustotal.com/) and [Google Safe Browsing](https://developers.google.com/safe-browsing).  
   - Create a `.env` file:  
     ```  
     VIRUSTOTAL_API=your_key_here  
     GOOGLE_SAFE_BROWSING_API=your_key_here  
     ```  

---

## 🖥️ **Usage**  
1. **Run the app**:  
   ```bash  
   python app.py  
   ```  
2. Open `http://localhost:5000` in your browser.  
3. Enter a URL (e.g., `bwin0023.com`) and click **Scan**.  

![Screenshot](https://via.placeholder.com/800x400.png?text=ScamScan+Interface+Preview)  

---

## 🔑 **API Keys**  
| Service                 | Free Tier Limits          | Sign-Up Link                          |  
|-------------------------|---------------------------|---------------------------------------|  
| **VirusTotal**          | 500 requests/day          | [Sign Up](https://www.virustotal.com/) |  
| **Google Safe Browsing**| 10,000 requests/day       | [Get Key](https://developers.google.com/safe-browsing) |  

---

## 🤝 **Contributing**  
1. Fork the repo.  
2. Create a branch:  
   ```bash  
   git checkout -b feature/your-idea  
   ```  
3. Commit changes:  
   ```bash  
   git commit -m "Add amazing feature"  
   ```  
4. Push and open a PR!  

---

## 📜 **License**  
MIT License - See [LICENSE](LICENSE).  

---

**⚠️ DISCLAIMER**: This tool is for **educational purposes only**. Do not use it to harass websites or violate terms of service.  

---
