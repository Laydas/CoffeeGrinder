s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    request = conn.recv(1024)
    request = str(request)

    # Check if authorization value is correct
    token_start = request.find('Authorization: Bearer')
    key_end = request.find('\\r', token_start)
    token = request[token_start + 22:key_end]

    if token != 'TOKEN123':
        data = """{"err":"Authentication Failure"}"""
        conn.send('HTTP/1.1 401 Unauthorized\n')
        conn.send('Content-Type: application/json\n')
        conn.send('Connection: close\n\n')
        conn.sendall(data)
        conn.close()
    elif token == 'TOKEN123':
        led_on = request.find('/?led=on')
        led_off = request.find('/?led=off')
        if led_on > 0:
            on_off = 'on'
            led.value(0)
        if led_off > 0:
            on_off = 'off'
            led.value(1)
        data = """{"led value":\"""" + on_off + """\", "raw":\"""" + token + """\"}"""
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: application/json\n')
        conn.send('Connection: close\n\n')
        conn.sendall(data)
        conn.close()