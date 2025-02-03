from flask import Flask, render_template, request  
import whois  
import requests  
from datetime import datetime  
import os  

app = Flask(__name__)  

# --- API Keys (Sign up for free tiers) ---  
VIRUSTOTAL_API = os.getenv('VIRUSTOTAL_API', 'your_virustotal_key')  
GOOGLE_SAFE_BROWSING_API = os.getenv('GOOGLE_SAFE_BROWSING_API', 'your_google_key')  

def get_domain_age(url):  
    try:  
        domain = whois.whois(url)  
        creation_date = domain.creation_date  
        if isinstance(creation_date, list):  
            creation_date = creation_date[0]  
        age = (datetime.now() - creation_date).days  
        return age  
    except:  
        return None  

def check_virustotal(url):  
    headers = {"x-apikey": VIRUSTOTAL_API}  
    response = requests.get(f"https://www.virustotal.com/api/v3/domains/{url}", headers=headers)  
    return response.json().get('data', {}).get('attributes', {}).get('last_analysis_stats', {})  

def check_google_safe(url):  
    api_url = "https://safebrowsing.googleapis.com/v4/threatMatches:find"  
    payload = {  
        "client": {"clientId": "ScamScan", "clientVersion": "1.0"},  
        "threatInfo": {  
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],  
            "platformTypes": ["ANY_PLATFORM"],  
            "threatEntryTypes": ["URL"],  
            "threatEntries": [{"url": url}]  
        }  
    }  
    response = requests.post(f"{api_url}?key={GOOGLE_SAFE_BROWSING_API}", json=payload)  
    return response.json().get('matches')  

@app.route('/', methods=['GET', 'POST'])  
def index():  
    result = None  
    if request.method == 'POST':  
        url = request.form.get('url')  
        if url:  
            result = {  
                'domain_age_days': get_domain_age(url),  
                'virustotal_stats': check_virustotal(url),  
                'google_blacklisted': check_google_safe(url)  
            }  
    return render_template('index.html', result=result)  

if __name__ == '__main__':  
    app.run(debug=True)  
