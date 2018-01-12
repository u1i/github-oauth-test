import json
import requests

client_id=""
client_secret=""

def liapp_do(q):

    outp=""
    try:
        code=q['code']
    except:
        code=""

    outp=outp + "<b>My Wonderful App (LinkedIn Test)</b><br>"

    if code == "":
        outp=outp + "Please login <a href='https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=81is8zaqn5oqf1&redirect_uri=https%3A%2F%2Fwww2.sotong.io%2Fliapp&state=rutzelfurz'>here</a><br>"
    else:
        url = 'https://www.linkedin.com/oauth/v2/accessToken'
        # url = 'https://hookb.in/KxQ9R2eo'
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        payload = {'grant_type': 'authorization_code', 'code': code, 'redirect_uri': 'https://www2.sotong.io/liapp', 'client_id': client_id, 'client_secret': client_secret}

        res = requests.post(url, data=payload, headers=headers)

        # print (res.status_code)
        # print (res.text)
        accesstoken_response=res.text

        # return str(accesstoken_response)

        j=json.loads(res.text)

        access=j["access_token"]

        # return access

        headers = {'Authorization': 'Bearer ' + access}
        url='https://api.linkedin.com/v1/people/~:(id,first-name,last-name,email-address,num-connections,picture-url)?format=json'
        res = requests.get(url, headers=headers)
        user_response=res.text
        j=json.loads(res.text)
        hello=j["firstName"]
        outp=outp + "Hello " + hello + "!<br>&nbsp;<br><p>Access Token Request: " + str(accesstoken_response) + "<p>USER Request: " + str(user_response)
    return outp
