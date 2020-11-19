"""Istehsal olunan mehsullar"""

class Mehsul:
    def __init__(self, name, date_of_production, price, stock,katid):
        self.name = name
        self.date = date_of_production
        self.price = price
        self.stock = stock
        self.m_id = katid
