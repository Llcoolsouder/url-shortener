FROM nginx:stable

COPY nginx.conf /etc/nginx/
COPY ./static/* /data/www/

CMD nginx