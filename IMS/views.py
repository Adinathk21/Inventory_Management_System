from django.shortcuts import render,redirect
from .models import * 
from django.views import View
from .forms import createitemForm,SellForm,viewitemForm



def create_Item(request):
    if request.method =="POST":
        form =createitemForm(request.POST)
        if form.is_valid():
            form.save()
    form = createitemForm()
    context = {'form':form, }
    return render(request,'testing/create_Item.html', context)
        

class ShowProduct(View):
    def get(self,request):
        product_list = create_item.objects.all()
        template_name = 'testing/show_product.html'
        context = {'product_list': product_list}
        return render(request, template_name, context)

def homepage(request):
    home_page = 'testing/home_page.html'
    return render(request, home_page)

def view_item(request,i):
    item_obj=create_item.objects.get(id=i)
    fm =viewitemForm(instance=item_obj)
    if request.method == 'POST':
        form= viewitemForm(request.POST, instance=item_obj)
        if form.is_valid():
            form.save()
            return redirect("/ims/show/")
    template_name="testing/view.html"
    context={'fm':fm}
    return render(request,template_name,context)

def edit_item(request,i):
    item_obj=create_item.objects.get(id=i)
    form =createitemForm(instance=item_obj)
    if request.method == 'POST':
        form= createitemForm(request.POST, instance=item_obj)
        if form.is_valid():
            form.save()
            return redirect("/ims/show/")
    template_name="testing/edit_item.html"
    context={'form':form}
    return render(request,template_name,context)

def sell(request,i):
    item_obj=create_item.objects.get(id=i)
    form =SellForm(instance=item_obj)
    if request.method == 'POST':
        form= SellForm(request.POST, instance=item_obj)
        if form.is_valid():
            form.save()
            return redirect("/ims/show/")
    template_name="testing/sell.html"
    context={'form':form}
    return render(request,template_name,context)

