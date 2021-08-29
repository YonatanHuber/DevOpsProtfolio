from supplies import supplies_app

@supplies_app.route('/')
@supplies_app.route('/index')
def index():
    return "Hello, World!"