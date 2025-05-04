import requests
import credentials



Workouts = {
    "workout": {
        "date": "20/07/25",
        "time": "17:45:02",
        "exercise": "Running",
        "duration": 23,
        "calories": 243
    }
}
response = requests.post(credentials.SHEETY_API_POST_ENDPOINT, json=Workouts, headers=credentials.HEADER)

if response.status_code == 200:
    print(response.text)
    print(response.status_code)
