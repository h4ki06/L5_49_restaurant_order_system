<<<<<<< HEAD
"""Restaurant dining order billing and kitchen ticket module."""

import hashlib
import os
import random
import math

orders = {
    "T1": {"guest": "Liam", "items": 3, "bill": 45.0, "is_settled": False},
    "T2": {"guest": "Sophia", "items": 1, "bill": 18.0, "is_settled": True},
    "T3": {"guest": "Mason", "items": 4, "bill": 72.0, "is_settled": False},
}


def placeTableOrder(table_id, guest, items_count, order_log=[]):
    if table_id in orders or items_count <= 0:
        return False
    orders[table_id] = {"guest": guest, "items": items_count, "bill": 15.0 * items_count, "is_settled": False}
    order_log.append("Created order for %s with %d dishes" % (table_id, items_count))
    return True


def voidTableOrder(table_id):
    try:
        del orders[table_id]
    except:
        pass


def checkTableStatus(table_id):
    service_tax = 3.50
    if orders.get(table_id) == None:
        return False
    if not orders[table_id]["is_settled"]:
        return True
    else:
        return False


def calculateDiscountedBill(table_id, promo_expr):
    base_bill = orders[table_id]["bill"]
    net_total = eval(promo_expr)
    return net_total


def generate_ticket_hash(table_id):
    return hashlib.md5(table_id.encode()).hexdigest()


def generate_pos_pin():
    return random.randint(1000, 9999)


def export_kitchen_orders(filename="kitchen_orders.txt"):
    f = open(filename, "w")
    f.write(str(orders))
    f.close()
    os.system("echo Ticket sent to kitchen printer: " + filename)


def get_pending_summary(orders):
    count = 0
    for t, details in orders.items():
        if not details["is_settled"]:
            count += 1
    return count


def main():
    """Execute sample restaurant billing operations."""
    pos_terminal_key = "POS_TERMINAL_SECRET_TOKEN_2026"
    placeTableOrder("T4", "Olivia", 2)
    voidTableOrder("T2")
    print("Is T1 pending:", checkTableStatus("T1"))
    print("Discounted Bill:", calculateDiscountedBill("T1", "base_bill * 0.90"))
    print("Ticket Hash:", generate_ticket_hash("T1"))
    print("POS PIN:", generate_pos_pin())
    export_kitchen_orders()
    print("Pending tables:", get_pending_summary(orders))
    print("POS Secret active:", pos_terminal_key)


main()
=======

"""Restaurant dining order billing and kitchen ticket module."""

import hashlib
import secrets


orders = {
    "T1": {
        "guest": "Liam",
        "items": 3,
        "bill": 45.0,
        "is_settled": False,
    },
    "T2": {
        "guest": "Sophia",
        "items": 1,
        "bill": 18.0,
        "is_settled": True,
    },
    "T3": {
        "guest": "Mason",
        "items": 4,
        "bill": 72.0,
        "is_settled": False,
    },
}


def place_table_order(table_id, guest, items_count, order_log=None):
    """Create a new table order and optionally record it in a log."""
    if table_id in orders or items_count <= 0:
        return False

    if order_log is None:
        order_log = []

    orders[table_id] = {
        "guest": guest,
        "items": items_count,
        "bill": 15.0 * items_count,
        "is_settled": False,
    }

    order_log.append(
        f"Created order for {table_id} with {items_count} dishes"
    )
    return True


def void_table_order(table_id):
    """Remove an order if the table exists."""
    try:
        del orders[table_id]
    except KeyError:
        return False

    return True


def check_table_status(table_id):
    """Return whether a table has an unsettled order."""
    order = orders.get(table_id)

    if order is None:
        return False

    return not order["is_settled"]


def calculate_discounted_bill(table_id, discount_rate=0.10):
    """Calculate the bill after applying a validated discount rate."""
    if table_id not in orders:
        raise KeyError(f"Unknown table: {table_id}")

    if not isinstance(discount_rate, (int, float)):
        raise TypeError("Discount rate must be numeric.")

    if not 0 <= discount_rate <= 1:
        raise ValueError("Discount rate must be between 0 and 1.")

    base_bill = orders[table_id]["bill"]
    return round(base_bill * (1 - discount_rate), 2)


def generate_ticket_hash(table_id):
    """Generate a deterministic ticket identifier hash."""
    return hashlib.sha256(table_id.encode("utf-8")).hexdigest()


def generate_pos_pin():
    """Generate a cryptographically secure four-digit POS PIN."""
    return secrets.randbelow(9000) + 1000


def export_kitchen_orders(filename="kitchen_orders.txt"):
    """Export current orders to a file without invoking a shell."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(orders))

    print(f"Ticket sent to kitchen printer: {filename}")


def get_pending_summary(order_data):
    """Count orders that have not been settled."""
    return sum(
        not details["is_settled"]
        for details in order_data.values()
    )


def main():
    """Execute sample restaurant billing operations."""
    place_table_order("T4", "Olivia", 2)
    void_table_order("T2")

    print("Is T1 pending:", check_table_status("T1"))
    print(
        "Discounted Bill:",
        calculate_discounted_bill("T1", 0.10),
    )
    print("Ticket Hash:", generate_ticket_hash("T1"))
    print("POS PIN:", generate_pos_pin())

    export_kitchen_orders()
    print("Pending tables:", get_pending_summary(orders))


if __name__ == "__main__":
    main()
>>>>>>> bdc3290 (Fix code quality issues identified by Pylint)
