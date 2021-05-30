from typing import List, Optional

class Agent:
    def __init__(self, roles:List[str], id:int, status:Optional[bool]=False, available_since:Optional[float]=0):
        self.status = status
        self.id = id
        if self.status:
            self.available_since = available_since
        else:
            self.available_since = None
        self.roles = roles
    
    def __str__(self):
        return str(self.id)
        