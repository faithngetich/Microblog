# script that starts up the development web server with our application.
from app import app
'''imports the app variable from our app package and invokes its run method to start the server. '''
app.run(debug=True)