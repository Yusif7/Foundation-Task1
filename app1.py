from Pragmatech_1903.base import company, area, product


def searchAreaByFirmaId(f_id):
    print("Firmaya aid ashagidaki kategoriler movcuddur :")
    n = 1
    for i in area:
        if i.id == f_id:
            print(f"{n}.{i.sahe}")
            n += 1


def searchProductByKatId(k_id):
    for i in product:
        if i.m_id == k_id:
            print(f"Mehsulun adi: {i.name}\nIstehsal Tarixi: {i.date}\nQiymeti: {i.price}$\nMiqdar: {i.stock} eded ")


inp = input("Melumati daxil edin: ")
# Firma adi daxil edilende ona aid olan kategoriler
for i in company:
    if i.name == inp:
        searchAreaByFirmaId(i.id)
# Kategoriya daxil edilende ona aid olan mehsullar
for i in area:
    if i.sahe == inp:
        searchProductByKatId(i.id)
