class Product:
    def __init__(self, i, n, p, c) -> None:
        self.id = i
        self.name = n
        self.price = p
        self.count = c

    @staticmethod
    def add():
        id = input('enter id: ')
        name = input('enter name: ')
        price= input('enter price: ')
        count= input('enter count: ')
        new_product = Product(id, name, price, count)
        Products.append(new_product)

    def edit(self,field):
        
        if field == 1:
            print('What the hell man?! Go away')
            exit(0)
        elif field == 2:
            newname = input('Enter the new name: ')
            p.name = newname
            print('Name of the product is successfully changed!')
        elif field == 3:
            newprice = input('Enter the new price for the product: ')
            p.price = newprice
            print('Price of the product is successfully changed!')
        elif field == 4:
            newcount = input('Enter the new count of the product: ')
            p.count = newcount
            print('Count of the product is successfully changed!')
        else:
            print('Your input is wrong!!!')



    @staticmethod
    def search():
        sname = input('Enter the product name: ')
        for p in Products:
            if p.name == sname:
                print(p.id, p.name, p.price, p.count)

    def remove(self):
        ...

    def show(self):
        ...
    
    @staticmethod
    def show_list():
        for p in Products:
            print(p.id, p.name, p.price, p.count)

    def exit(self):
        exit(0)

Products = []

def read_from_database():
    f = open('database.txt', 'r')

    for line in f:
        result = line.split(', ')
        my_obj = Product(result[0], result[1], result[2], result[3])
        #my_dict = {'code': result[0], 'name': result[1], 'price': result[2], 'count': result[3]}

        Products.append(my_obj)

def write_to_database():
    ff = open('database.txt', 'w')
    for product in Products:
        ff.write(f"{product['code']},{product['name']},{product['price']},{product['count']}\n")
    ff.close()

def show_menu():
    print('1-add')
    print('2- Edit')
    print('3- Remove')
    print('4- Search')
    print('5- Show List')
    print('6- Buy')
    print('7- Make QR Code')
    print('8 - Exit')


print('Welcome to the Store')
print('Loading...')
read_from_database()
for p in Products:
    print(p.id)
Product.show_list()
print('Data loaded.')


while True:
    show_menu()
    choice = int(input('Enter your choice:  '))

    if choice == 1:
        Product.add()

    elif choice == 2:
        id = int(input('Enter product code to edit: '))
        for p in Products:
            if int(p.id) == id:
                field = int(input('Enter the number of field you want to edit: (Code: 1, Name: 2, Price: 3, Count: 4)(Try not to change the code!! That is not OKAY!!)  '))
                p.edit(field)
            else:
                print('Product not Found')

    elif choice == 3:
        id = int(input('Enter product code to edit: '))
        for i, p in enumerate(Products):
            if int(p.id) == id:
                del Products[i]

    elif choice == 4:
        Product.search()

    elif choice == 5:
        Product.show_list()

    elif choice == 6:
        #buy()
        ...

    elif choice == 7:
        #make_qrcode()
        ...

    elif choice == 8:
        write_to_database()
        exit(0)
        
    else:
        print('Wrong Choice!!')