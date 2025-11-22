#pip install request
#python -m pip install requests
import requests
API_KEY = "0bffabab-8341-453a-a518-3808f64987b8:fx"
BASE_URL = "https://api-free.deepl.com/v2/translate"
print("Welcome, enter your text for translation: ")
print("Text -  exit - to leave")

print("Welcome")
print("Enter movie name:")
print("Text 'exit' to leave")

while True:
    text = input("Enter movie name you want to find: ")
    if text.lower() == 'exit':
        print("bye")
        break
    
    data = {
        "auth_key": API_KEY,
        "text": text,
        "target_lang": "UK"
    }
    response = requests.post(BASE_URL, data=data)
    result = response.json()
    if "translations" in result:
        translated_text = result["translations"][0]["text"]
        print(f"Переклад: {translated_text}")
    else:
        print(result)