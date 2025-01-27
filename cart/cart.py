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
        # Retrieve all products from the session's cart
        product_ids = self.cart.keys()
        products = Product.objects.filter(pk__in=product_ids)
        return products

    def add(self, product, quantity):
        # Check if the product is already in the cart
        if str(product.pk) in self.cart:
            current_quantity = self.cart[str(product.pk)]["quantity"]
            max_addable_quantity = product.stock - current_quantity
            # Check if adding more than stock allows
            if max_addable_quantity >= int(quantity):
                new_quantity = current_quantity + int(quantity)
                self.cart[str(product.pk)]["quantity"] = new_quantity
                # Update the total to reflect the new quantity
                self.cart[str(product.pk)]["total"] = round(
                    float(product.price) * new_quantity, 2
                )
            else:
                return False
        else:
            # Add the product to the cart with the specified quantity
            if product.stock >= int(quantity):
                self.cart[str(product.pk)] = {
                    "id": product.pk,
                    "name": product.name,
                    "quantity": int(quantity),
                    "total": round(
                        float(product.price) * int(quantity), 2
                    ),  # Total is price times quantity
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
            self.cart[str(product.pk)] = {
                "quantity": int(quantity),
                "total": round(float(product.price) * int(quantity), 2),
                # Total is price times quantity
            }

        self.session.modified = True

    def get_total(self):
        return sum(item["total"] for item in self.cart.values())

    def clear(self, request):
        # Clear all items from the session's cart
        del request.session["cart"]
        request.session.modified = True
