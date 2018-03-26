import requests
import time
import json


class SpyGames:

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def find_friends(self):
        params = {"access_token": self.token, "user_id": self.user_id, "version": "5.73"}
        friends = requests.get("https://api.vk.com/method/friends.get", params).json()["response"]
        return friends

    def find_groups(self):
        params = {"access_token": self.token, "user_id": self.user_id, "version": "5.73", "count": "1000"}
        groups = requests.get("https://api.vk.com/method/groups.get", params).json()["response"][1:]
        return groups

    def groups_info(self):
        friends = self.find_friends()
        groups = self.find_groups()
        progress = 1
        print("Getting information about groups...")
        for friend in friends:
            params = {"access_token": self.token, "user_id": friend, "version": "5.73"}
            try:
                f_groups = requests.get("https://api.vk.com/method/groups.get", params).json()["response"]
            except KeyError:
                pass
            time.sleep(0.35)
            print(f"{progress} / {len(friends)} - {round(progress*100/len(friends), 2)} %")
            progress += 1
            groups = set(groups) - set(f_groups)
        return groups

    def target_groups(self):
        groups = self.groups_info()
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
        return group_description

    @property
    def spy_game(self):
        group_description = self.target_groups()
        with open("groups.json", "w", encoding="utf8") as f:
            json.dump(group_description, f, ensure_ascii=False)


def user_name():
    user = input("User ID or name: ")
    if user.isdigit():
        user_id = user
    else:
        params = {"screen_name": user, "version": "5.73"}
        user_id = requests.get("https://api.vk.com/method/utils.resolveScreenName", params).json()["response"]["object_id"]
    return user_id


def main():
    token = "7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099"
    user = user_name()
    console = SpyGames(token, user)
    result = console.spy_game


if __name__ == "__main__":
    main()