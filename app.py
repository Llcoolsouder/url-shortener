from flask import (
    Flask,
    Blueprint
)

app = Flask('url-shortener')
api = Blueprint('api', __name__)

@api.route('/shorten/', methods=['POST'])
def shorten():
    '''
    Creates a shortened url that links to the url given via form
    '''
    return 'This endpoint has not been implemented.'

@api.route('/short/<url>/')
def short(url):
    '''
    Redirects to the url previously associated with url
    Parameters:
        url (str): unique piece of shortened url
    '''
    return 'This endpoint has not been implemented.'

app.register_blueprint(api, url_prefix='/api')


if __name__ == '__main__':
    app.run(debug = True) # TODO: Remove debug mode