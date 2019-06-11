import requests as req
import json

class analyticsObjects:
    #Creates the standard urls and headers for requests
    def __init__(self, client, tracking):
        self.host = "http://www.google-analytics.com"
        self.headers = {'content-type': 'application/json'}
        self.payload = {"v": "1","tid": tracking,"cid": client}
    #Makes a post to the website with the payload(decoded from json)
    def post(self, payload, decode):
        data = req.post(self.host, json.dumps(self.payload.update(payload)), headers = self.headers)
        if(data.status_code == 200): #This means the post was successfull
            return decode(data)
        else:
            raise Exception("There was a failure in the network to make the request.")
        
        

    def pageView(self, page): 
        payload = {"t": page}
        return self.post(payload, lambda a : a.json)
