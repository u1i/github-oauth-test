import json
import requests

client_id=""
client_secret=""


def igapp_do(q):

    outp=""
    try:
        code=q['code']
    except:
        code=""

    outp=outp + "<b>My Wonderful App (Instagram Test)</b><br>"

    if code == "":
        outp=outp + "Please login <a href='https://api.instagram.com/oauth/authorize/?client_id=eac2654f6b9944958f70dc4e62068f4b&redirect_uri=https%3A%2F%2Fwww2.sotong.io%2Figapp&response_type=code&scope=follower_list+public_content'>here</a><br>"
    else:
        url = 'https://api.instagram.com/oauth/access_token'
#        url='https://requestb.in/16lpe8m1'
        headers = {}
        payload = {'grant_type': (None, 'authorization_code'), 'code': (None, code), 'redirect_uri': (None, 'https://www2.sotong.io/igapp'), 'client_id': (None, client_id), 'client_secret': (None, client_secret)}

        res = requests.post(url, files=payload, headers=headers)

#        print (res.status_code)
#        print (res.text)
        accesstoken_response=res.text
        
        j=json.loads(res.text)

        access=j["access_token"]
        hello=j["user"]["username"]

        return str(accesstoken_response)

    return outp
