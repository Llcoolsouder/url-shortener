# URL Shortener
This is just a small project for practicing some backend web skills. The homepage is a form where you can input a long url (or any url, I guess---Whatever floats your boat). When you submit the form, the long url is assigned a short tag which is saved in a database alongside the original url. Afterwards, `/short/<tag>` will redirect to the long url. The concept is similar to _Bitly_ or _TinyURL_.

## My Stack
- Python3
- Flask
- Gunicorn
- Sqlite3
- nginx
- Docker and Docker Compose
- HTML and CSS

## Building
The entire project is set up to run with `docker-compose`, so everything should be very portable and easy to use. To run the server, do the following:
```
docker-compose build
docker-compose up
```
That's it.  
