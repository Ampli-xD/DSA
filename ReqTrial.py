from kivy.app import App
from kivy.network.urlrequest import UrlRequest


def got_json(req, result):
    print (req)
    print (result)
def failed():
    print("fail")
req = UrlRequest("https://syllabusx-web-server.onrender.com/secondsemesters/CSE", on_success=got_json, on_failure=failed)

class ReqTrial(App):
    pass

ReqTrial().run()