class WebServer():
    def __init__(self):
        self.ips = {}
    def add(self, x):
        if x in self.ips:
            self.ips[x] = self.ips[x]+1
        else:
            self.ips[x] = 1
    def get(self, x):
        return sorted(self.ips, key = lambda x: self.ips[x], reverse = True)[:x]

if __name__="main":
    w = WebServer()
    w.add("1.1.1.1")
    w.add("1.1.1.1")
    w.add("1.1.1.1")
    w.add("1.1.1.2")
    w.add("1.1.1.3")
    w.add("1.1.1.3")
    print(w.get(2))
        
