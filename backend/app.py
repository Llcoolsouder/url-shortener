from link import Link, LinkEncoder
import sqlite3
import json
from flask import (
    Flask,
    Blueprint,
    url_for,
    request,
    redirect
)
from flask_cors import CORS

app = Flask('url-shortener')
cors = CORS(app, resources={"/api/*": {"origins": "*"}})
api = Blueprint('api', __name__)

DATABASE = 'database/links.db'
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
    link = Link.from_url(request.json['url'])
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(
        f"INSERT INTO {TABLE} VALUES ('{link.url}', '{link.source_tag}')")
    connection.commit()
    connection.close()
    return json.dumps(link, cls=LinkEncoder)


@api.route('/links/')
def all():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {TABLE}')
    links = list(map(lambda data: Link(*data), cursor.fetchall()))
    connection.close()
    return json.dumps(links, cls=LinkEncoder)


app.register_blueprint(api, url_prefix='/api')


@app.route('/short/<tag>/')
def short(tag):
    '''
    Redirects to the url previously associated with tag
    Parameters:
        tag (str): unique piece of shortened url
    '''
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {TABLE} WHERE source_tag = '{tag}'")
    link_data = cursor.fetchone()
    connection.close()
    link = Link(*link_data)
    return redirect(link.get_absolute_url())


if __name__ == '__main__':
    app.run()
