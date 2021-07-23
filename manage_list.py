from replit import db

def add_user(user: str):
    value = db["users"]
    value.append(user)
    db["users"] = value
    

def add_channel(ids: int, user: str):
    channel_list = db[user + "_server"]

    if channel_list.__contains__(str(ids)) == False:
        value = db[user + "_server"]
        value.append(str(ids))
        db[user + "_server"] = value
        

def get_channel_id(user: str):
    channel_list = db[user + "_server"].value
    return channel_list 


def get_followlist(channelID):
    user_list = db["users"].value

    followlist = []

    for user in user_list:
        channel_list = db[user + "_server"]

        if channel_list.__contains__(str(channelID)):
            followlist.append(user)

    return followlist

def reset_key():
    user_list = db["users"].value

    for user in user_list:
      db[user] = []
      db[user + "_server"] = []

def set_key(username):
    db[username] = []
    db[username + "_server"] = []


def print_value():
    user_list = db["users"].value

    for user in user_list:
      print(user, db[user].value)

def clear_user():
    user_list = db["users"].value

    clear_list = []

    for user in user_list:
        channel_list = get_channel_id(user)
        if not len(channel_list):
            clear_list.append(user)
    
    for items in clear_list:
      user_list.remove(items)
    
    db["users"] = user_list

def clear():
  for item in db.keys():
    if len(db[str(item)]) == 0:
      del db[str(item)]



if __name__ == "__main__":
    print(db["users"].value)
