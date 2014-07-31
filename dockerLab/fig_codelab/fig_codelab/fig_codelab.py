import multiprocessing

bind = "127.0.0.1:8080"

def app(enfiron, start_response):
	data = "Here's some data\n"
	start_response("200 OK", [
		("Content-Type", "text/plain"),
		("Content-Length", str(len(data)))
	])
	return iter([data])
