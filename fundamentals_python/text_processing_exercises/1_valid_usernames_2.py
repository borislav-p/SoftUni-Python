def lenght_is_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False
def characters_are_valid(username):
    for ch in username:
        if not (ch.isalnum() or ch == "-" or ch == "_"):
            return False
    return True
def no_redundant_symbols(username):
    if " " in username:
        return False
    return True



usernames = input().split(", ")
for username in usernames:
    if lenght_is_valid(username) and characters_are_valid(username) and no_redundant_symbols(username):
        print(username)