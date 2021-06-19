class Tienda:
    def __init__(self, name):
        self.name = name
        self.listaproductos = []
    def add_product (self, new_product):
        self.listaproductos.append(new_product)
        return self
    def sell_product (self, id):
        self.listaproductos.pop(id)
        return
    def show_products(self):
        for x in self.listaproductos:
            x.print_info()
        return self
    def inflation(self, percent_increase):
        self.price = self.price + (self.price * percent_increase)
        return self
    def set_clearance (self, category, percent_discount):
        for x in self.listaproductos:
            if category == x.category:
                x.price = x.price - (x.price * percent_discount)
            print(x.price)
        return self
    

