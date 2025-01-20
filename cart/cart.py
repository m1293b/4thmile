from products.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session

        # Initialize the cart if it does not exist in session
        if "cart" not in self.session:
            self.session["cart"] = {}

        self.cart = self.session.get("cart", {})

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def get_cart_items(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(pk__in=product_ids)
        return products

    def add(self, product, quantity):
        # Ensure the added quantity does not exceed available stock
        if str(product.pk) in self.cart:
            current_quantity = self.cart[str(product.pk)]["quantity"]
            max_addable_quantity = product.stock - current_quantity
            if max_addable_quantity >= int(quantity):
                self.cart[str(product.pk)]["quantity"] += int(quantity)
                self.cart[str(product.pk)]["total"] = int(product.price) * int(quantity)
            else:
                return False
        else:
            # Add the product to the cart with the specified quantity
            if product.stock >= int(quantity):
                self.cart[str(product.pk)] = {
                    "id": product.pk,
                    "name": product.name,
                    "quantity": int(quantity),
                    "total": int(product.price) * int(quantity),
                }
            else:
                return False

        self.session.modified = True
        return True  # Return true to indicate success

    def remove(self, product):
        # Remove the product from the cart
        if str(product.pk) in self.cart:
            del self.cart[str(product.pk)]

        self.session.modified = True

    def update(self, product, quantity):
        # Update the quantity of a product in the cart
        if str(product.pk) in self.cart:
            self.cart[str(product.pk)]["quantity"] = int(quantity)

        self.session.modified = True

    def clear(self, request):
        # Clear all items from the cart
        del request.session["cart"]
        request.session.modified = True
