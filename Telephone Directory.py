
import sys,sqlite3
import re
class telephone:
    def __init__(self):
        self.con = sqlite3.connect('telephone.db')
        self.c = self.con.cursor()
        self.c.execute('Create table if not exists record(name text,phone int,email text,address text)')
    def add_contact(self):
        name = input('enter name:')
        phone = int(input('enter no:'))
        email_id = input('enter email_id:')
        address = input('enter address:')

        self.c.execute('INSERT INTO record VALUES(?,?,?,?)',(name,phone,email_id,address))
        self.con.commit()  
    def display(self):
        self. __init__()
        self.c.execute('select * from record')
        data = self.c.fetchall()
        print('{}\t{}\t\t{}\t\t{}\t'.format('name','phone','email','address'))
        for i in data:
            print('{}\t{}\t{}\t{}\t'.format(i[0],i[1],i[2],i[3]))
            print('~~~~~~~~~~~~~')
    def screen(self):
        print('1: Add contact')
        print('2: Display all contacts')
        print('3: Search for a contact')
        print('4:Delete')
        print('5:Exit')
        k = int(input('enter choice:'))
        return k
    def search(self):
        name = input('enter name:')
        self.c.execute('select*from record where name = ?',(name))
        d = self.c.fetchall()
        print('{}\t{}\t\t{}\t\t{}\t'.format('name','phone','email','address'))
        for i in data:
            print('{}\t{}\t{}\t{}\t'.format(i[0],i[1],i[2],i[3]))
    def delete(self):
        name = ('enter name')
        self.c.execute('delete from record where name = ?',(name,))
        self.con.commit()
        c = int(input('enter choice'))
        return c
tel = telephone()
while True:
    m = tel.screen()
    if m==1:
        tel.add_contact()
    elif m==2:
        tel.display()
    elif m==3:
        tel.search()
    elif m==4:
        tel.delete()
    else:
        tel.con.close()
        sys.exit()
