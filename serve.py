import http.server, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
port = int(os.environ.get("PORT", 8765))
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=port, bind="")
