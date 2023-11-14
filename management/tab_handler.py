from management.product_handler import *


def calculate_tab(tab):
    subtotal = 0.0
    for item in tab:
        product = get_product_by_id(item["_id"])
        subtotal += product["price"] * item["amount"]
    return {"subtotal": f"${round(subtotal, 2)}"}
