import json
import requests

def gitapp_do(q):

    outp=""
    try:
        code=q['code']
    except:
        code=""

    outp=outp + "<b>My Wonderful App (GitHub Test)</b><br>"

    if code == "":
        outp=outp + "Please login <a href='https://github.com/login/oauth/authorize?scope=user:email&client_id=7f16afb741dad8922865'>here</a><br>"
    else:
        client_id="#####"
        client_secret="#####"

        url = 'https://github.com/login/oauth/access_token'
        headers = {'Content-Type': "application/json; charset=UTF-8", 'Accept': "application/json"}
        data = {"client_id": client_id, "client_secret":client_secret, "code": code}
        res = requests.post(url, json=data, headers=headers)
        # print (res.status_code)
        # print (res.text)

        j=json.loads(res.text)

        access=j["access_token"]

        url='https://api.github.com/user'
        res = requests.get(url + "?access_token=" + str(access))

        j=json.loads(res.text)

        user=j["login"]
        avatar=j["avatar_url"]

        # print user, avatar
        outp=outp + "Hello " + str(user) + "!"
    return outp
