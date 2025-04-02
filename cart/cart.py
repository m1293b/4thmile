from products.models import Product
from cart.models import Cart as current_cart, CartItem
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out


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
        product_price = product.sale_price if product.is_on_sale else product.price
        if str(product.pk) in self.cart:
            current_quantity = self.cart[str(product.pk)]["quantity"]
            max_addable_quantity = product.stock - current_quantity
            # Check if adding more than stock allows
            if max_addable_quantity >= int(quantity):
                new_quantity = current_quantity + int(quantity)
                self.cart[str(product.pk)]["quantity"] = new_quantity
                # Update the total to reflect the new quantity
                self.cart[str(product.pk)]["total"] = round(
                    float(product_price) * new_quantity, 2
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
                        float(product_price) * int(quantity), 2
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

    def clear(self):
        # Clear all items from the session's cart
        self.session["cart"] = {}
        self.session.modified = True

    @receiver(user_logged_in)
    def merge_carts_on_login(sender, request, user, **kwargs):
        """
        Merges the session cart with the user's persistent cart when they log in.
        """
        session_cart = request.session.get("cart", {})
        user_cart, created = current_cart.objects.get_or_create(
            user=user, active_cart=True
        )

        # Update or merge session cart into the user's cart model
        for product_id, session_item in session_cart.items():
            product = Product.objects.get(pk=product_id)
            quantity = session_item["quantity"]

            # Check if the product exists in the user's cart
            cart_item, item_created = CartItem.objects.get_or_create(
                cart=user_cart, product=product
            )
            if item_created:
                # New item, just set the quantity
                cart_item.quantity = quantity
            else:
                # Existing item, increment the quantity
                # Although it might be better just to update the quantity, keep testing
                cart_item.quantity += quantity

            # Save the updated item
            cart_item.save()

        # Update session cart from the user's cart model
        updated_session_cart = {}
        for cart_item in CartItem.objects.filter(cart=user_cart):
            updated_session_cart[str(cart_item.product.pk)] = {
                "id": cart_item.product.pk,
                "name": cart_item.product.name,
                "quantity": cart_item.quantity,
                "total": round(float(cart_item.product.price) * cart_item.quantity, 2),
            }

        # Update the session's cart with the merged data
        request.session["cart"] = updated_session_cart
        request.session.modified = True
