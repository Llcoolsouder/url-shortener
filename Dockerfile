FROM nginx:stable

COPY nginx.conf /etc/nginx/
COPY ./static/* /data/www/

EXPOSE 80

CMD nginx