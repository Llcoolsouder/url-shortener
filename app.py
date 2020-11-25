import sqlite3
import hashlib
from flask import (
    Flask,
    Blueprint,
    url_for,
    request,
    redirect
)


app = Flask('url-shortener')
api = Blueprint('api', __name__)

DATABASE = 'links.db'
TABLE = 'links'
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {TABLE} (
        url text,
        source_tag text)
''')
conn.commit()
conn.close()


@api.route('/shorten/', methods=['POST'])
def shorten():
    '''
    Creates a shortened url that links to the url given via form
    '''
    url = request.form['url']
    source_tag = hashlib.md5(url.encode('utf-8')).hexdigest()[0:8]
    shortened_url = url_for('api.short', tag=source_tag)
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO {TABLE} VALUES ('{url}', '{source_tag}')")
    connection.commit()
    connection.close()
    return f'<a href={shortened_url}>{shortened_url}</a> now redirects to {url}'


@api.route('/short/<tag>/')
def short(tag):
    '''
    Redirects to the url previously associated with tag
    Parameters:
        tag (str): unique piece of shortened url
    '''
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(f"SELECT url FROM {TABLE} WHERE source_tag = '{tag}'")
    url = cursor.fetchone()[0]
    connection.close()
    if 'http' not in url:
        url = f'http://{url}'
    return redirect(url)


app.register_blueprint(api, url_prefix='/api')


if __name__ == '__main__':
    app.run(debug=True)  # TODO: Remove debug mode
