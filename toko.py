item1 = {"nama":"laptop","stock":"85", "harga": 120000}
item2 = {"nama":"ponsel","stock":"109", "harga": 50000}
item3 = {"nama":"tablet","stock":"4", "harga": 120000}
item4 = {"nama":"cashp","stock":"67", "harga": 6000}
item5 = {"nama":"headphone","stock":"35", "harga": 8000}

items = [item1,item2,item3,item4,item5]

for i in range(len(items)):
    print("nama barang:" , items[i]["nama"])
    print("stock:", items[i]["stock"])
    print("harga"": ", items[i]["harga"])

    
nama = str(input("masukan nama barang: "))
stock = int(input("masukan jumblah stock: "))
harga = int(input("masukan harga: "))

item6 = {"nama":nama,"stock":stock,"harga":harga}
items.append(item6)

for i in range(len(items)):
    print("nama barang:" , items[i]["nama"])
    print("stock:", items[i]["stock"])
    print("harga"": ", items[i]["harga"])