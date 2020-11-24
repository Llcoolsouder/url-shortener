import sqlite3
import hashlib
from flask import (
    Flask,
    Blueprint,
    url_for,
    request
)


app = Flask('url-shortener')
api = Blueprint('api', __name__)
database = 'links.db'
conn = sqlite3.connect(database)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS links (
        source text,
        destination text)
''')
conn.commit()
conn.close()


@api.route('/shorten/', methods=['POST'])
def shorten():
    '''
    Creates a shortened url that links to the url given via form
    '''
    source = request.form['url']
    destination_tag = hashlib.md5(source.encode('utf-8')).hexdigest()[0:8]
    destination = url_for('api.short', tag=destination_tag)
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO links VALUES ('{source}', '{destination_tag}')")
    connection.commit()
    connection.close()
    return f'<a href={destination}>{destination}</a> now redirects to {source}'


@api.route('/short/<tag>/')
def short(tag):
    '''
    Redirects to the url previously associated with tag
    Parameters:
        tag (str): unique piece of shortened url
    '''
    return 'This endpoint has not been implemented.'


app.register_blueprint(api, url_prefix='/api')


if __name__ == '__main__':
    app.run(debug=True)  # TODO: Remove debug mode
