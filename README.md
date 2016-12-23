# Fetching FAA airport status in python"

I wrote some code to fetch airport status from the FAA's airport status
API.

Here's [the repo](https://github.com/jakekara/faa-airport-status.py).

The [API](http://services.faa.gov/docs/services/airport/#airportStatus) itself is pretty minimal.

You can get XML or JSON, but I'm just interested in JSON.

There are two "library" files, airportstatus.py and airports.py, that can
be used in your code, and two examples of command line scripts that use the
libraries, getall.py and getstatus.py.

#### airportstatus.py

[This
file](https://github.com/jakekara/faa-airport-status.py/blob/master/airportstatus.py)
is the main point of interest. It performs API calls with the get_status()
method. It's so short, I'll paste the entire code here:

{% highlight python %}
import requests

def status_url(code):
    return "http://services.faa.gov/airport/status/" + code +
    "?format=application/json"

def get_status(code):
    r = requests.get(status_url(code))

    if r.status_code != 200:
            raise Exception ("Error fetching status for airport " + code +
            ": <Status: " + str(r.status_code) + ">")
    return r.json()
{% endhighlight %}

#### airports.py

This file creates a list of (airport code, airport name) tuples, and search()
function that returns the subset of airports whose names or codes include
the search term.

These are the two command line tool examples:

#### getall.py

Get status of all airports in the airports.py list and save them to
all.json. Here's the Usage:

  {% highlight javascript %}
  getall.py
  {% endhighlight %}

#### getstatus.py

Get the the status of one airport and print to stdout. Here's Usage:

{% highlight javascript %}
    getstatus.py BDL
    {
      "status": {
        "minDelay": "", 
        "maxDelay": "", 
        "trend": "", 
        "reason": "No known delays for this airport.", 
        "closureEnd": "", 
        "avgDelay": "", 
        "closureBegin": "", 
        "endTime": "", 
        "type": ""
      }, 
      "ICAO": "KBDL", 
      "name": "Bradley International", 
      "city": "Windsor Locks", 
      "IATA": "BDL", 
      "delay": "false", 
      "state": "Connecticut", 
      "weather": {
        "wind": "Northwest at 3.5mph", 
        "weather": "Mostly Cloudy", 
        "meta": {
          "url": "http://weather.gov/", 
          "credit": "NOAA's National Weather Service", 
          "updated": "4:51 PM Local"
        }, 
        "temp": "40.0 F (4.4 C)", 
        "visibility": 10.0
      }
    }
{% endhighlight %}
