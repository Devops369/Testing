
ids = []
users = []

uinput = input("Enter an id: ")

def getId(userId):
    fakeId = None

    if userId != type(int):
        fakeId = int(len(userId))
        return fakeId
    elif userdId == type(int):
        fakeId = int(userId)
        return fakeId
    else:
        print("IdError: not an 'ID'")
        return None

realId = getId(uinput)
ids.append(realId)
for IDS in ids:
    users.append(IDS)

print("Users({})".format(users))
