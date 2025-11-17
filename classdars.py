
import re

class kontakt:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
baza=[]
def view_kontakt(s:list):
    for item in s:
        print(item.name,item.phone,item.email)
def add_kontakt(s:list):
        name=input("name=")
        phone=input("phone=")
        email=input("email=")
        x=r'^[A-Za-z][A-Za-z]+$'
        y=r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
        z=r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
        togri=True
        if not re.match(x,name):
            print("name xato")
            togri=False
        if not re.match(y,phone):
            print("phone xato")
            togri = False
        if not re.match(z,email):
            print("email xato")
            togri = False
        if togri:
            add = kontakt(name, phone, email)
            s.append(add)
            print("qo'shildi")

def edit_kontakt(s:list):
    name1 = input("name=")
    for item in s:
        if item.name==name1:
            yangi=item
            name = input("name=")
            phone = input("phone=")
            email = input("email=")
            x = r'^[A-Za-z][A-Za-z]+$'
            y = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
            z = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
            togri = True
            if not re.match(x, name):
                print("name xato")
                togri = False
            if not re.match(y, phone):
                print("phone xato")
                togri = False
            if not re.match(z, email):
                print("email xato")
                togri = False
            if togri:
                yangi.name = name
                yangi.phone = phone
                yangi.email = email
                print("o'zgardi")
                break
        else:
            print("topilmadi")
def delete_komtakt(s:list):
    name1=input("name=")
    count=0
    for item in s:
        count+=1
        if item.name==name1:
            s.pop(count-1)
            print("o'chirildi")
        else:
            print("topilmadi")
def menejer_kontakt(s:list):
    while True:
        kod=input("1.view_kontakt\n 2.add_kontakt\n 3.edit_kontakt\n 4.delete_kontakt\n 5.break")
        if kod=="1":
            view_kontakt(baza)
        elif kod=="2":
            add_kontakt(baza)
        elif kod=="3":
            edit_kontakt(baza)
        elif kod=="4":
            delete_komtakt(baza)
        else:
            break
# menejer_kontakt(baza)
