INVENTORY = dict()
REGISTRATION = list()

class Product:
    def __init__(self, name, unit_cost, quantity, code, category):
        self.name = name
        self.unit_cost = unit_cost
        self.quantity = quantity
        self.code = code
        self.category = category
    
    def __repr__(self):
        return (
            f"Nome: {self.name}\n"
            f"Código: {self.code}\n"
            f"Categoria: {self.category}\n"
            f"Valor unitário: {self.unit_cost}\n"
            f"Quantidade em estoque: {self.quantity}\n"
        )

class Purchase:
    def __init__(self, unit_cost, quantity, code ,cost):
        self.unit_cost = unit_cost
        self.cost = cost
        self.quantity = quantity
        self.code = code
        
    
    def __repr__(self):
        return (
            f"Código: {self.code}\n"
            f"Valor unitário: {self.unit_cost}\n"
            f"Quantidade comprada: {self.quantity}\n"
            f"Custo total: {self.cost}\n"
        )     

def buy_product():
    code = input("Código do produto para compra: ")
    quantity=int(input("diga a quantidade:"))
    product = INVENTORY.get(code)
    if not product:
        print("Código não existente, adicione um produto primeiro.")
        return
    if product.quantity < quantity:
        print("Quantidade invalida.")
        return
    print(product)
    product.quantity -= quantity
    INVENTORY[code]=product
    REGISTRATION.append(build_purchase(product,quantity))
    

def build_purchase(product,quantity):
    purchase = Purchase(
        code = product.code,
        unit_cost = product.unit_cost,
        quantity = quantity,
        cost = product.unit_cost*quantity
    )
    return purchase

def build_custom_product():
    product = Product(
        name=input("Nome do produto: "),
        code=input("Código do produto: "),
        quantity=int(input("Quantidade: ")),
        category=input("Categoria: "),
        unit_cost=float(input("Valor unitário: "))
    )
    return product

def verify_product_quantity(product):
    if product.quantity < 3:
        print(f"Produto de código {product.code} com estoque baixo ({product.quantity} unidade(s))")

def add_product():
    product = build_custom_product()
    INVENTORY[product.code] = product
    verify_product_quantity(product)

def update_product():
    code = input("Código do produto: ")
    product = INVENTORY.pop(code, None)
    if not product:
        print("Código não existente, adicione um produto primeiro.")
        return
    print(product)
    new_product = build_custom_product()

    verify_product_quantity(product=new_product)

    INVENTORY[new_product.code] = new_product


def list_products_quantities():
    for code, product in INVENTORY.items():
        print(f"Código: {code} Nome: {product.name} Quantidade: {product.quantity}")

def get_inventory_value():
    total = 0
    for code, product in INVENTORY.items():
        total += product.unit_cost * product.quantity
    print(f"Inventario atual avaliando em :R${total}")   

should_run = True

message = """
1 - Adicionar produto
2 - Atualizar produto
3 - Verificar quantidade de produtos em estoque
4 - Verificar valor do estoque atual
5 - Realizar uma compra
6 - historico de compras
0 - Fechar programa
"""


while should_run:
    print(message)
    result = input("Próxima ação: ")
    if result == "1":
        add_product()
    elif result == "2":
        update_product()
    elif result == "3":
        list_products_quantities()
    elif result == "4":
        get_inventory_value()
    elif result == "5":
        buy_product()
    elif result == "6":
        print(REGISTRATION)    
    elif result == "0":
        should_run = False
    else:
        print("Errado")
    print(INVENTORY)