from http import server


class FunHTTPRequestHandler(server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        server.SimpleHTTPRequestHandler.end_headers(self)


if __name__ == '__main__':
    server.test(HandlerClass=FunHTTPRequestHandler)
