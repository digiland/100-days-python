class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
        self.followers = 0
        print("User created")


user_2 = User("001", "tom", "123")

print(user_2.first_name)


# factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
