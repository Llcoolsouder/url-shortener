from flask import (
    Flask
)

app = Flask('url-shortener')

@app.route('/shorten/', methods=['POST'])
def shorten():
    '''
    Creates a shortened url that links to the url given via form
    '''
    return 'This endpoint has not been implemented.'

@app.route('/short/<url>')
def short(url):
    '''
    Redirects to the url previously associated with url
    Parameters:
        url (str): unique piece of shortened url
    '''
    return 'This endpoint has not been implemented.'


if __name__ == '__main__':
    app.run(debug = True) # TODO: Remove debug mode