# Python module for getting FAA airport

The API is pretty minimal: http://services.faa.gov/docs/services/airport/#airportStatus

### Files

There are two "library" files that can be used in your code, and two
command line scripts. 

These are the two libraries:

* airports.py - Contains a list of (airport code, airport name), and a method
for performing a simple kkeyword search of airports (the search() method)

* airportstatus.py - Performs API calls with the get_status() method. 

These are the two command line tool examples::

* getall.py - Get status of all airports in the airports.py list and save
  them to all.json. Usage:

    python getall.py

* getstatus - Get the the status of one airport and print to stdout. Usage:

    python getstatus.py BDL
