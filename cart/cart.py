from products.models import Product
from cart.models import Cart as current_cart, CartItem
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in


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

    # @receiver(user_logged_in)
    # def merge_carts_on_login(request, user, **kwargs):
    #     # Update carts: session and model
    #     cart_model, created = current_cart.objects.get_or_create(user=request.user, active_cart=True)
    #     session_cart = request.session.get("cart", None)

    #     # Check if the user already has an active cart
    #     try:
    #         user_cart = current_cart.objects.get(user=user, active_cart=True)
    #     except current_cart.DoesNotExist:
    #         user_cart = None

    #     if session_cart:
    #         if user_cart is None:
    #             user_cart = current_cart.objects.create(user=user, active_cart=True)

    #         # Update or create cart items
    #         for item in session_cart:
    #             product_id = item["product_id"]
    #             quantity = item["quantity"]
    #             try:
    #                 cart_item = CartItem.objects.get(cart=user_cart, product_id=product_id)
    #                 cart_item.quantity += quantity
    #                 cart_item.save()
    #             except CartItem.DoesNotExist:
    #                 CartItem.objects.create(
    #                     cart=user_cart, product_id=product_id, quantity=quantity
    #                 )

    #     else:
    #         # If session cart is empty or non-existent, populate it with the user's active cart
    #         if user_cart:
    #             session_cart = []
    #             cart_items = CartItem.objects.filter(cart=user_cart)
    #             for item in cart_items:
    #                 session_cart.append(
    #                     {"product_id": item.product_id, "quantity": item.quantity}
    #                 )
    #             request.session["cart"] = session_cart
