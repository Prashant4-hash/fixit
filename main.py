import os
import sys
import json
import urllib.request
import urllib.error

# Read OpenRouter API Key from key.txt or environment variable
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key and os.path.exists("key.txt"):
    with open("key.txt", "r") as f:
        api_key = f.read().strip()

if not api_key:
    print("[Error] No API key found in key.txt or environment variable.")
    sys.exit(1)

# Get input error message
error_input = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else ""
if not error_input and not sys.stdin.isatty():
    error_input = sys.stdin.read().strip()

if not error_input:
    print("Usage: py main.py \"git comit\"")
    sys.exit(0)

print("\033[94mAnalyzing error via OpenRouter...\033[0m")

# OpenRouter Endpoint
url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
    "HTTP-Referer": "http://localhost",
    "X-Title": "FixIt CLI"
}

payload = {
   "model": "inclusionai/ling-3.0-flash-vl:free",
    "messages": [
        {
            "role": "system",
            "content": "You are an expert CLI terminal troubleshooter. Analyze the terminal output. Return ONLY the exact command to fix the issue on line 1, and a 1-sentence explanation on line 2 starting with '# Explanation: '."
        },
        {"role": "user", "content": f"OS: {sys.platform}\nError:\n{error_input}"}
    ],
    "temperature": 0.1
}

try:
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
    with urllib.request.urlopen(req) as response:
        res_body = json.loads(response.read().decode('utf-8'))
        output = res_body['choices'][0]['message']['content'].strip()
        
        print("\n" + "="*50)
        print(f"\033[92m{output}\033[0m")
        print("="*50 + "\n")
        
        confirm = input("Execute this command now? (y/n): ").strip().lower()
        if confirm == 'y':
            cmd = output.split('\n')[0].strip()
            os.system(cmd)
except urllib.error.HTTPError as e:
    print(f"\033[91mAPI HTTP Error ({e.code}): {e.read().decode('utf-8')}\033[0m")
except Exception as e:
    print(f"\033[91mError: {e}\033[0m")