from django import forms 
from .models import create_item
class createitemForm(forms.ModelForm):
    class Meta:

        model = create_item     
        fields =['Item_name','Quantity','Quantity_buy','Selling_price']
       

class SellForm(forms.ModelForm):
    class Meta:

        model = create_item     
        fields =['sell_item']

class viewitemForm(forms.ModelForm):
    class Meta:

        model = create_item     
        fields =['Item_name','Quantity','Quantity_buy','Selling_price']
      
       