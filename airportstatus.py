import requests

def status_url(code):
    return "http://services.faa.gov/airport/status/" + code + "?format=application/json"

def get_status(code):
    r = requests.get(status_url(code))

    if r.status_code != 200:
        raise Exception ("Error fetching status for airport " + code+ ": <Status: " + str(r.status_code) + ">")
    return r.json()
