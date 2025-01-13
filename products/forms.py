from django import forms
from .models import Product, Category, ProductImage

class ProductForm(forms.ModelForm):
    
    class Meta:
        
        model = Product
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        categories = Category.objects.all()
        friendly_names = {(category.id, category.get_friendly_name()) for category in categories}
        
        self.fields['category'].choices = friendly_names
        
class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image', 'alt_text']
        
