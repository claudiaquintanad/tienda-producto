from Clases.tienda import Tienda
from Clases.producto import Producto
#import Clases.producto
#import Clases.tienda

tienda1 = Tienda("tiendita")

producto1 = Producto("leche", 100, "lácteos")
producto2 = Producto("cereal", 500, "cereales")

tienda1.add_product(producto1)
tienda1.add_product(producto2)
tienda1.show_products()

tienda1.set_clearance("cereales", 0.02)


