# pass is a word to get rid of the error for class and function
# def funciton_empty():
#     pass
# PascalCase for class, otherwise snake_case
class User:
    # pass
    # create attributes - constructor, carry for every object created
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        # init value as the object creates - 0
        self.followers  = 0
        self.following = 0

    # always need a self,
    # so when the object call, it knows the object that calls it
    # user is the user that we decide to follow
    def follow(self, user):
        # the user that we follow
        user.followers += 1
        # our own following
        self.following += 1


# same for creating the attributes in constructor
# but when it has 100 objects, construcotr is better
user_0 = User("000", "nobody")
# user_0.id = "000"
# user_0.username = "nobody"

# using constructor
user_1 = User("001", "jessie")
# print(user_1.id)
# print(user_1.followers)
user_2 = User("002", "boo")

user_1.follow(user_2)
print(user_1.followers)     #0
print(user_1.following)     #1
print(user_2.followers)    #1
print(user_2.following)    #0




