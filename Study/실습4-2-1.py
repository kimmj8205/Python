def get_int(message):
    s=input(message)
    while not s.isdigit():
        s=input(message)
    return int(s)

