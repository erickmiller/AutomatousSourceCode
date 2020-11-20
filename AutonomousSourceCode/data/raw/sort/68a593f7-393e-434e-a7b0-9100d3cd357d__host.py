
class Host(object):
    def __init__(self, state, name, address, files=[], users=[]):
        self.name = name
        self.address = address
        self.files = sorted(files)
        self.files = sorted(users)
        state.hosts[name] = self
    
    def addfile(self, file):
        self.files.append(file)
        self.files.sort()
    
    def removefile(self, file):
        self.files.remove(file)
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __hash__(self):
        return hash(self.name)
