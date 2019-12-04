users={"Peter": 600, "Georgo": 700, "Mike": 800}

def add_user():
    res = input("add your name: ")
    newt=str(res)
    users[newt] = 500
    print(users)


add_user()
print("Done")
print(users)