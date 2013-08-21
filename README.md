Objective: practice using google datastore NDB available in google app engine(GAE). 

1.The client send http request to the server quering the weather for a given zipcode.
The server query the NDB datastore with the zipcode as the key and output the weather info as JSON array. 

2. the client uses http request to modify the data stored in the NDB datastore. The temperature information is contained in a url. 
Upon receiving the url, the server extracts the information and store the data into the NDB datastore.  

After deploying the app into GAE, url1 can display the history weather information in JSON object. 
url2 is used to mofidy the weather information in NDB.

url1: http://dearbabymaimai.appspot.com/query?zipcode=53705 \

url2: http://dearbabymaimai.appspot.com/query?zipcode=53705&temp=90&date=08212013