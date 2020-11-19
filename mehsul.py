"""Istehsal olunan mehsullar"""
firma_id = 0
class Mehsul:
    def __init__(self, name, date_of_production, price, stock,katid):
        global firma_id
        firma_id += 1
        self.name = name
        self.date = date_of_production
        self.price = price
        self.stock = stock
        self.m_id = katid
