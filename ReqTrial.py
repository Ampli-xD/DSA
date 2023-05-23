from kivy.app import App
from kivy.network.urlrequest import UrlRequest


def failed():
    print("fail")
    
    
    
    
def got_json(req, result):
    for i in result:
        if "subject" in i.keys():
            print(i['subject'])







req = UrlRequest("https://syllabusx-web-server.onrender.com/secondsemesters/CSE", on_success=got_json, on_failure=failed)

class ReqTrial(App):
    pass

ReqTrial().run()