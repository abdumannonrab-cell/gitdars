class magazin:
    def __init__(self, title,price,sanasi,muddati,type,email,phone):
        self.title=title
        self.price=price
        self.sanasi=sanasi
        self.muddati=muddati
        self.type=type
        self.email=email
        self.phone=phone
baza=[]

def add_magazin(s:list):
    title=input("title")
    price=input("price")
    sanasi=input("sanasi")
    muddati=input("muddati")
    type=input("type")
    email=input("email")
    phone=input("phone")
    magazinw=magazin(title,price,sanasi,muddati,type,email,phone)
    s.append(magazinw)

def view_magazin(s:list):
    for item in s:
        print(item.title,item.sanasi,item.muddati,item.type,item.email,item.phone)
# view_magazin()
def menejer_magazin(s:list):
    while True:
        kod=input("1.view_magazin\n 2.add_magazin\n 3.break")
        if kod=="1":
            view_magazin(baza)
        elif kod=="2":
            add_magazin(baza)
        else:
            break
# menejer_magazin(baza)
