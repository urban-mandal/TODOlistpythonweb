import os
class SecretsManeger:
    def __init__(self):
        self.SECRET_KEY = os.urandom(24) 

    def get_secretkey(self):
        return self.SECRET_KEY

