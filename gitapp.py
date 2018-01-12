import json
import requests

client_id="###"
client_secret="###"


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
        url = 'https://github.com/login/oauth/access_token'
        headers = {'Content-Type': "application/json; charset=UTF-8", 'Accept': "application/json"}
        data = {"client_id": client_id, "client_secret":client_secret, "code": code}
        res = requests.post(url, json=data, headers=headers)
        # print (res.status_code)
        # print (res.text)
        accesstoken_response=res.text

        j=json.loads(res.text)

        access=j["access_token"]

        url='https://api.github.com/user'
        res = requests.get(url + "?access_token=" + str(access))
        user_response=res.text
        j=json.loads(res.text)

        user=j["name"]
        userid=j["login"]
        #avatar=j["avatar_url"]

        # print user, avatar

        url='https://api.github.com/user/emails'
        res = requests.get(url + "?access_token=" + str(access))
        useremail_response=res.text
        j=json.loads(res.text)

        outp=outp + "Hello " + str(user) + " (" + str(userid) + ") !<br>&nbsp;<br><p>Access Token Request: " + str(accesstoken_response) + "<p>USER Request: " + str(user_response) + "<p>EMAIL Request: " + str(useremail_response)
    return outp
