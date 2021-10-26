list = ["Ben", 9, [2, 1]]
print(list)
list.append("Lorenzo")
print(list)
del list[0]
lorenzo = list.pop(2)
print(lorenzo)
print(list)
numbered_list = [89, 56, 99, 2]
print(sorted(numbered_list, reverse=True))


inventory = ["tentacle sweeper", "sword"]
item = input("Which item will you use: ")


def checking_items(inventory2, item2):
    if item2 in inventory2 and item2 == "tentacle sweeper":
        print("yes")
    else:
        print("no")


checking_items(inventory, item)


