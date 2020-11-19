"""Firma haqqinda melumatlar"""

firma_id = 0
class Firma:
    def __init__(self, name, foundation_date, owner):
        global firma_id
        firma_id += 1
        self.id = firma_id
        self.name = name
        self.date = foundation_date
        self.owner = owner