from menu import products


def get_product_by_id(product_id):
    if not isinstance(product_id, int):
        raise TypeError("product id must be an int")

    for product in products:
        if product.get("_id") == product_id:
            return product
    return {}


def get_products_by_type(product_type):
    if not isinstance(product_type, str):
        raise TypeError("product type must be a str")

    products_of_type = [
        product for product in products if product.get("type") == product_type
    ]
    return products_of_type


def add_product(menu, **product):
    new_id = max([item["_id"] for item in menu]) + 1 if menu else 1
    product["_id"] = new_id
    menu.append(product)
    return product


def menu_report():
    product_count = len(products)

    if product_count == 0:
        return "Products Count: 0 - Average Price: $0.00 - Most Common Type: None"

    average_price = round(sum(item["price"] for item in products) / product_count, 2)

    type_counts = {}
    for product in products:
        type_counts[product["type"]] = type_counts.get(product["type"], 0) + 1

    most_common_type = max(type_counts, key=type_counts.get)

    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}"


def add_product_extra(menu, *required_keys, **product):
    for key in required_keys:
        if key not in product:
            raise KeyError(f"field {key} is required")

    product = {key: product[key] for key in required_keys}

    new_id = max([item["_id"] for item in menu], default=0) + 1 if menu else 1
    product["_id"] = new_id

    menu.append(product)
    return product
