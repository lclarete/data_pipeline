#!/usr/bin/env python
# coding: utf-8



import pynder


# getting token manually
# * https://www.youtube.com/watch?v=woZeUPcu3DA (worked!)
# * https://gist.github.com/taseppa/66fc7239c66ef285ecb28b400b556938
# * https://github.com/charliewolf/pynder/issues/136
# 
# tinder-access-token-generator node
# * https://github.com/jaebradley/tinder-access-token-generator


import re
import robobrowser

MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; U; en-gb; KFTHWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.16 Safari/535.19"
FB_AUTH = "https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd"

def get_access_token(email, password):
    s = robobrowser.RoboBrowser(user_agent=MOBILE_USER_AGENT, parser="lxml")
    s.open(FB_AUTH)
    ##submit login form##
    f = s.get_form()
    f["pass"] = password
    f["email"] = email
    s.submit_form(f)
    ##click the 'ok' button on the dialog informing you that you have already authenticated with the Tinder app##
    f = s.get_form()
    s.submit_form(f, submit=f.submit_fields['__CONFIRM__'])
    ##get access token from the html response##
    access_token = re.search(r"access_token=([\w\d]+)", s.response.content.decode()).groups()[0]
    #print  s.response.content.decode()
    return access_token




FBID = 100000212402348 #"YOUR_FB_ID"
XAuthToken= '5114b033-646c-4c0b-bd9d-b1a68d71f6d1'#"YOUR_FB_TOKEN"




'{"facebook_token": 100000212402348, "XAuthToken": ''5114b033-646c-4c0b-bd9d-b1a68d71f6d1''}'b



curl -X POST https://api.tinder.com/profile --data '{"age_filter_min": 20, "gender": 0, "age_filter_max": 35, "distance_filter": 14}'



import re

import requests
import robobrowser

MOBILE_USER_AGENT = "Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)"
FB_AUTH = "https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd"


def get_fb_access_token(email, password):
    s = robobrowser.RoboBrowser(user_agent=MOBILE_USER_AGENT, parser="lxml")
    s.open(FB_AUTH)
    f = s.get_form()
    f["pass"] = password
    f["email"] = email
    s.submit_form(f)
    f = s.get_form()
    try:
        s.submit_form(f, submit=f.submit_fields['__CONFIRM__'])
        access_token = re.search(
            r"access_token=([\w\d]+)", s.response.content.decode()).groups()[0]
        return access_token
    except Exception as ex:
        print("access token could not be retrieved. Check your username and password.")
        print("Official error: %s" % ex)
        return {"error": "access token could not be retrieved. Check your username and password."}


def get_fb_id(access_token):
    if "error" in access_token:
        return {"error": "access token could not be retrieved"}
    """Gets facebook ID from access token"""
    req = requests.get(
        'https://graph.facebook.com/me?access_token=' + access_token)
    return req.json()["id"]



get_fb_access_token('livia.clarete@gmail.com', 'liviapistico20!!!')



session = pynder.Session(XAuthToken=XAuthToken)



import requests

facebook_token = XAuthToken

USER_AGENT = "Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)"

HEADERS = {
    'app_version': '6.9.4',
    'platform': 'ios',
    "content-type": "application/json",
    "User-agent": USER_AGENT,
    "Accept": "application/json"
}

new_url = 'https://api.gotinder.com/v2/auth/login/facebook'

new_data = {"token": facebook_token}

r_new = requests.post(new_url, headers=HEADERS, json=new_data)

print(r_new.status_code)
print(r_new.json())


# In[75]:


s = requests.Session()



s.headers.update({'X-Auth-Token': XAuthToken})
s.request(method="get",url='https://api.gotinder.com/profile')



# get_access_token('livia.clarete@gmail.com', 'liviapistico20!!!')



import requests
requests.Session().request(method="get",
                           url='https://api.gotinder.com/profile',
                           headers={'X-Auth-Token': XAuthToken})


user.bio # their biography
user.name # their name
user.photo # a list of photo URLs
user.age # their age
user.birth_date # their birth_date
user.ping_time # last online
user.distance # distane from you
user.common_friends # friends in common
user.common_likes # likes in common



# Print the names of all facebook friends using Tinder Social.
print(", ".join([x.name for x in friends]))

# Get the user_info of these facebook friends.
user_info_objects = []
for friend in friends:
    user_info_objects.append(friend.get_tinder_information())

# Print the bios.
for user_info, friend in zip(user_info_objects, friends):
    print("=" * 50)
    # Use Friend.name, as user_info.name only contains first name.
    print(friend.name)
    print(friend.facebook_link)
    print("-" * 50)
    print(user_info.bio)
    print("=" * 50)


