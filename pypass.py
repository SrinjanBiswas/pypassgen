import string
import random

with open('passlist.txt', 'r', encoding='utf-8') as f:
    passwords = f.readlines()

def new_pass(pass_type):
    if pass_type=='y':
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for n in range(10))
    elif pass_type=='n':
        return ''.join(random.SystemRandom().choice(passwords))
    else:
        return "WRONG CHOICE!!!!"


print("Password: " + new_pass(input("Strong password (Y/N)? ")))

# from flask import Flask, request

# # create the Flask app
# app = Flask(__name__)

# @app.route('/')
# def query_example():
#     len = int(request.args.get('length'))
#     return new_pass(len)


# if __name__ == '__main__':
#     # run app in debug mode on port 5000
#     app.run(debug=True, port=5000)