import requests

API_KEY = "14131132"
BASE_URL = "http://www.omdbapi.com/"

print("Welcome")
print("Enter movie name: ")
print("Text 'exit' to leave ")

while True: 
    movieName = input("Enter movie name you want to find: ")
    
    if movieName.lower() == 'exit':
        print("bye")
        break
    
    params = {
    "t": movieName,
    "apikey": API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["Response"] == "False":
        print("Error")
    else:
        print(f"Name: {data['Title']}") 
        print(f"Year: {data['Year']}")
        print(f"Rated: {data['Rated']}") 
        print(f"Released: {data['Released']}")
        print(f"Genre: {data['Genre']}")