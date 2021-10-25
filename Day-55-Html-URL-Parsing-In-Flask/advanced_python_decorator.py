class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

    def is_authenticated_decorator(function):
        def wrapper(*args, **kwargs):
            if args[0].is_logged_in == True:
                # the function here refers to create_blog_post a
                function(args[0])
        return wrapper

    @is_authenticated_decorator
    def create_blog_post(user):
        print(f"This is {user.name}'s new blog post.")

new_user = User("angela")
# without changing it to true, line 20 won't run
new_user.is_logged_in = True
new_user.create_blog_post(new_user)

def logging_decorator(function):
    def wrapper(*args):
        print(f"the name of the function is {(function).__name__} with input of {args[0]}, {args[1]}, {args[2]} and tuple input of {args}")
        result = function(args[0], args[1], args[2])
        print(f"The output is {result}")
    return wrapper

@logging_decorator
def guess_the_name(a, b, c):
    return a * b * c

guess_the_name(1, 2, 3)
