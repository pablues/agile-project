
class URLDispatcher:
    def __init__(self):
        self.routes = {}

    def add_route(self, path, view_func):
        self.routes[path] = view_func

    def dispatch(self, path):
        if path in self.routes:
            return self.routes[path]()
        else:
            return self.page_not_found()

    def page_not_found(self):
        return "404 Not Found"