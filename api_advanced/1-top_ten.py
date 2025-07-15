#!/usr/bin/python3
"""documenting stuff"""
import requests

def top_ten(username):
    url = f"https://api.example.com/users/{username}/top_ten"
    try:
        res = requests.get(url)
    except requests.RequestException as e:
        # You can print an error or handle it differently
        return None

    if res.status_code != 200:
        return None

    try:
        res_json = res.json()
    except ValueError:
        return None

    # Process res_json as needed

    return "OK"
