import requests as rq

class Global:

    def send_request(self,endpoint,data):
        try:
            response = rq.get(endpoint, params=data)
            result=response.json()
        except Exception as e:
            print("Error: ejecutando el proceso sendRequest")
            result=None

        return result