import requests
from urllib.parse import urlencode


def get_mutual_friends(source_uid, target_uid, token):
    params = {
        "source_uid": source_uid,
        "target_uid": target_uid,
        "access_token": token,
    }

    response = requests.get("https://api.vk.com/method/friends.getMutual", params).json()
    users_ids = ", ".join([str(n) for n in response["response"]])
    params = {
            "user_ids": users_ids
        }
    response = requests.get("https://api.vk.com/method/users.get", params).json()
    print("Mutual friends for target users are below:\n")
    for user in response["response"]:
        print(user["first_name"], user["last_name"], "\t", "ID:", user["uid"])
        print("Link:", "".join(("https://vk.com/id", str(user["uid"]))), "\n")


def main():
    auth_url = "https://oauth.vk.com/authorize"
    app_id = 6353105

    auth_data = {
        "client_id": app_id,
        "display": "page",
        "scope": "friends",
        "response_type": "token",
        "v": "5.71"
    }

    print("Get your token by link:", "?".join((auth_url, urlencode(auth_data))))
    token = input("Type your token here:")
    source_uid = input("Type user ID:")
    target_uid = input("Type user ID with who you want to find mutual friends:")
    get_mutual_friends(source_uid, target_uid, token)


main()
