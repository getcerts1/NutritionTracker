import requests
from datetime import datetime
from credentials import (API_KEY, ACCOUNT_ID,
                         SHEETY_API_POST_ENDPOINT, BEARER_TOKEN, HOST_DOMAIN,
                         NATURAL_LANG_EXERCISE_ENDPOINT)
HEADER = {
    "x-app-id": ACCOUNT_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

POST_HEADER = {
            "Authorization": f"Bearer {BEARER_TOKEN} "
        }



def date_refine():
    current_date = datetime.now()
    refined_time = current_date.strftime("%d/%m/%Y")
    return refined_time


def time_refine():
    a = str(datetime.now()).split()
    b = a[1].split(":")
    c = b[2].split(".")
    final_join = "".join(f"{b[0]}:{b[1]}:{c[0]}")

    return final_join


def sheety_post_request(api_endpoint, data, header):
    response = requests.post(api_endpoint, json=data, headers=header)
    if response.status_code == 200:
        print("completed post request")
        print(response.text)
        return response

def natural_lang_for_exercise():

    user_input = str(input("enter input for analysis: "))
    query_data = {
        "query": user_input
    }
    response = requests.post(HOST_DOMAIN + NATURAL_LANG_EXERCISE_ENDPOINT,
                             json=query_data, headers=HEADER)

    if response.status_code == 200:
        print(response.text)
        data = response.json()


        exercises = data["exercises"]

        # initalise sheetsAPI POST information
        new_row = {
            "workout": {
                "date": date_refine(),
                "time": time_refine(),
                "exercise": "",
                "duration": 0,
                "calories": 0
            }
        }

        for i,exercise in enumerate(exercises):
            new_row["workout"]["exercise"] = exercise["name"]
            new_row["workout"]["duration"] = round(int(exercise["duration_min"]), 1)
            new_row["workout"]["calories"] = int(exercise["nf_calories"])

            print(f"{i+1}:{new_row["workout"]["exercise"]} --- {new_row["workout"]["duration"]} --- {new_row["workout"]["calories"]}")

            sheety_post_request(SHEETY_API_POST_ENDPOINT, new_row, header=POST_HEADER)

        return data

    else:
        return response.status_code