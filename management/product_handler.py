from menu import products


def get_product_by_id(product_id):
    for product in products:
        if product.get("_id") == product_id:
            return product
    return {}


def get_products_by_type(product_type):
    products_of_type = [
        product for product in products if product.get("type") == product_type
    ]
    return products_of_type


def add_product(menu, **product):
    new_id = max([item["_id"] for item in menu]) + 1 if menu else 1
    product["_id"] = new_id
    menu.append(product)
    return product
