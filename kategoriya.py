"""Firmanin fealiyyet gosterdiyi saheler"""

kat_id = 0

class Kategoriya:

    def __init__(self, kategory, firmaid):
        global kat_id
        kat_id += 1
        self.kat_id = kat_id
        self.sahe = kategory
        self.id = firmaid
