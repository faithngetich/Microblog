from flask import Flask
'''creates the application object (of class Flask) and then imports the views module'''

app = Flask(__name__)
from app import views
'''IT's below here to avoid circular references'''