FROM nginx:stable

RUN \
    curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs

ADD ./frontend-src ./frontend-src/

RUN cd frontend-src && \
    npm install && \
    npm run build && \
    mkdir -p /data/www/ && \
    mv ./build/* /data/www/

COPY nginx.conf /etc/nginx/


CMD nginx