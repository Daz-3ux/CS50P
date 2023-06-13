class Jar:
    def __init__(self, capicity=12):
        try:
            if capicity <= 0:
                raise ValueError
            self.capicity = capicity
            self.cnt = 0
        except ValueError:
            raise
        
    def __str__(self):
        cookie = ""
        for _ in range(self.cnt):
            cookie += "🍪"
        return cookie
    
    def deposit(self, cnt):
        try:
            if cnt <= 0 or cnt + self.cnt > self.capicity:
                raise ValueError
            self.cnt += cnt
        except ValueError:
            raise
        
    def withdraw(self, del_cnt):
        try:
            if del_cnt <= 0 or del_cnt > self.cnt:
                raise ValueError
            self.cnt -= del_cnt
        except ValueError:
            raise
    
    @property
    def capacity(self):
        return self.capicity
    
    @property
    def size(self):
        return self.cnt