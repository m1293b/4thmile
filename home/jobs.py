from home.models import Product

def increment_smiles(product_id):
    """
    Increment the number of smiles (like a "like" on Facebook) for the given Product.

    Smiles are an optional way for users to give a positive feedback on a product.
    """
    product = Product.objects.get(id=product_id)
    product.smiles += 1
    product.save()
    
def increment_purchases(product_id):
    """
    Increment the number of purchases for the given Product.

    This is a measure to see how many times the product has been purchased.
    If this number is higher then a limit that is set by the admin, it will be displayed on the product's page.
    """
    
    product = Product.objects.get(id=product_id)
    product.purchases += 1
    product.save()

def increment_views(product_id):
    """
    Increment the number of views for the given Product. This number will be reset by funcition every 24 hours.
    I am looking for ways to handle this task. Django-Q seems to do the job, but as this isn't a main part of the project,
    I will try to implement this after I'm ready to submit.

    This is a measure to see how many times the product has been viewed.
    If this number is higher then a limit that is set by the admin, it will be displayed on the product's page.
    """
    product = Product.objects.get(id=product_id)
    product.views += 1
    product.save()