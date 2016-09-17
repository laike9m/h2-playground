HTTP: Upgrade, or send H2 packet directly
HTTPS: ALPN

both endpoints should send setting frame. When using h2, setting frame is the first data frame. preface = “PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n” + SETTINGS frame

Is preface a frame? 

TODO: 抓包查看 PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n 是不是和 setting 一起送的
用 hyper，wireshark 查看 loopback

用 wireshark 直接载入 server.crt/key，decode hyper package

requirement: 
1. python supports APLN: 2.7.9+ or 3.5+
