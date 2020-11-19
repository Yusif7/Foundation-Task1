from Pragmatech_1903.base import company, area, product


#  Firma adi ile Kategoriyani cixartmaq
def searchAreaByFirmaId(f_id):
    print("Firmaya aid ashagidaki kategoriler movcuddur :")
    n = 1
    for i in area:
        if i.id == f_id:
            print(f"{n}.{i.sahe}")
            n += 1


#  Kategori adi ile Mehsulu cixartmaq
def searchProductByKatId(k_id):
    for i in product:
        if i.m_id == k_id:
            print(f"Mehsulun adi: {i.name}\nIstehsal Tarixi: {i.date}\nQiymeti: {i.price}$\nMiqdar: {i.stock} eded ")


#  Firma adi ile Mehsulu cixartmaq
def searchFirmaByKatId(k_id):
    for i in company:
        if i.id == k_id:
            print(f"Sirketin adi: {i.name}")


inp = input("""Company Base xos gelmisiniz!!!
Sirketlerimi ashagidaki kimidir:
1. MeatForEat
2. World Technology
3. Hyundai Motors
Melumati daxil edin: """)
# Firma adi daxil edilende ona aid olan kategoriler
for i in company:
    if i.name == inp:
        searchAreaByFirmaId(i.id)
# Kategoriya daxil edilende ona aid olan mehsullarin hansi firmaya aid olmalarini goster
for i in area:
    if i.sahe == inp:
        searchFirmaByKatId(i.id), searchProductByKatId(i.id)
