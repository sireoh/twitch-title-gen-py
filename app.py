"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
#https://carpedm20.github.io/emoji/

import emoji
import random
from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1
 
 
# Driver code
s = ['Geeks', 'for', 'Geeks']
print(listToString(s))


@app.route('/')
def hello():
    """Renders a sample page."""
    f = open("emojis.txt", "r")
    g = open("words.txt", "r")

    fArray = f.read().split('\n')
    gArray = g.read().split('\n')

    ranArr_f = random.choice(fArray)
    ranArr_g = random.choice(gArray)

    ranText3g = listToString(random.sample(gArray, 4))
    ranText3f = listToString(random.choices(fArray, k = 3))

    return(ranText3g +
           emoji.emojize(random.choice(fArray)) + emoji.emojize(random.choice(fArray)) + emoji.emojize(random.choice(fArray))
           )

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

