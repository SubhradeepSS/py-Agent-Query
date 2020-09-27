class Agent:
    def __init__(self, roles, id, status=False, available_since=None):
        self.status = status
        self.id = id
        if self.status:
            self.available_since = available_since
        else:
            self.available_since = None
        self.roles = roles
    
    def __str__(self):
        return str(self.id)