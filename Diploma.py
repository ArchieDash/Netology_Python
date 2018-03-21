import requests
import time
import json


def main():
    token = "7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099"

    user = input("User ID or name: ")
    if user.isdigit():
        user_id = user
    else:
        params = {"screen_name": user, "version": "5.73"}
        user_id = requests.get("https://api.vk.com/method/utils.resolveScreenName", params).json()["response"]["object_id"]

    params = {"access_token": token, "user_id": user_id, "version": "5.73"}
    friends = requests.get("https://api.vk.com/method/friends.get", params).json()["response"]
    params = {"access_token": token, "user_id": user_id, "version": "5.73", "count": "1000"}
    groups = requests.get("https://api.vk.com/method/groups.get", params).json()["response"][1:]

    progress = 1
    print("Getting information about groups...")
    for friend in friends:
        params = {"access_token": token, "user_id": friend, "version": "5.73"}
        try:
            f_groups = requests.get("https://api.vk.com/method/groups.get", params).json()["response"]
        except KeyError:
            pass
        time.sleep(0.35)
        print(f"{progress} / {len(friends)} - {round(progress*100/len(friends), 2)} %")
        progress += 1
        groups = set(groups) - set(f_groups)

    progress = 1
    print("Formatting results...")
    group_description = list()
    for group in groups:
        params = {"group_id": group, "fields": "members_count", "version": "5.73"}
        info = requests.get("https://api.vk.com/method/groups.getById", params).json()["response"]
        time.sleep(0.35)
        print(f"{progress} / {len(groups)} - {round(progress*100/len(groups), 2)} %")
        progress += 1
        group_info = dict(zip(["name", "gid", "members_count"],[info[0]["name"], info[0]["gid"], info[0]["members_count"]]))
        group_description.append(group_info)

    with open("groups.json", "w", encoding="utf8") as f:
        json.dump(group_description, f, ensure_ascii=False)


main()
