from vending_machine import choose_product_get_change
from inventory import rewrite_products, rewrite_rename_cashbox, rename_products


class vendimg_machine_actions():
    choose_product_get_change()


class inventory_changes():
    rewrite_products()
    rewrite_rename_cashbox()
    rename_products()


if __name__ == '__main__':
    vendimg_machine_actions()
    inventory_changes()
