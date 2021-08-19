from app import chimera_app

@chimera_app.route('/')
@chimera_app.route('/index')
def index():
    return "Welcome to ChiMeRA - Contact Management RESTfull App"

@chimera_app.route('/person')
@chimera_app.route('/person/{id}')
def person():
    return "Welcome to ChiMeRA - Contact Management RESTfull App - person"
#POST
#PUT
#DELETE
#GET
