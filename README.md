Objective: practice using google datastore NDB available in google app engine(GAE). 
1.The client send http request to the server quering the weather information with a given zipcode.
The server query's the NDB datastore with the zipcode as the key and returns the available weather info as JSON array. 
2. the client uses http request to modify the data stored in the NDB datastore. The temperature information is contained in a url. 
Upon receiving the url, the server extracts the information and store the data into the NDB datastore.  

After deploying the app into GAE, dearbabymaimai.appspot, the following url can display the history weather information in JSON object.
http://dearbabymaimai.appspot.com/query?zipcode=53705 
This url is used to mofidy the weather information in NDB.
http://dearbabymaimai.appspot.com/query?zipcode=53705&temp=90&date=08212013