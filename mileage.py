day = int(input())
route = int(input())
print(((day - (route % day)) + route) // day)
