if [ ! -f server.key ]; then
    rm server.key
fi
if [ ! -f server.crt ]; then
    rm server.crt
fi
openssl req -x509 -sha256 -nodes -newkey rsa:2048 -days 365 -keyout server.key -out server.crt
