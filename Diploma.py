import requests
import time
import json


def main():
    token = "5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128"

    user = input("User ID or name: ")
    if user.isdigit():
        user_id = user
    else:
        params = {'screen_name': user, "version": "5.73"}
        user_id = requests.get('https://api.vk.com/method/utils.resolveScreenName', params).json()["response"]["object_id"]

    params = {"access_token": token, 'user_id': user_id, "version": "5.73"}
    friends = requests.get('https://api.vk.com/method/friends.get', params).json()["response"]
    params = {"access_token": token, 'user_id': user_id, "version": "5.73", "count": "1000"}
    groups = requests.get('https://api.vk.com/method/groups.get', params).json()["response"][1:]

    for friend in friends:
        params = {"access_token": token, 'user_id': friend, "version": "5.73"}
        try:
            f_groups = requests.get('https://api.vk.com/method/groups.get', params).json()["response"]
        except:
            pass
        time.sleep(0.35)
        print('.', end='')
        groups = set(groups) - set(f_groups)

    group_description = list()
    for group in groups:
        params = {"group_id": group, "fields": "members_count", "version": "5.73"}
        info = requests.get('https://api.vk.com/method/groups.getById', params).json()["response"]
        time.sleep(0.35)
        print('.', end='')
        group_info = dict(zip(["name", "gid", "members_count"],[info[0]["name"], info[0]["gid"], info[0]["members_count"]]))
        group_description.append(group_info)
    print(group_description)

    with open('groups.json', 'w', encoding='utf8') as f:
        json.dump(group_description, f, ensure_ascii=False)


main()
