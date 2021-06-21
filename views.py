from django.shortcuts import render
from ecomweb.models import Product,Custemer
from ecomweb.forms import CustomerForm

# Create your views here.
def fetch_data(request):
    all_products=Product.objects.all()
    item_name=request.POST.get('data')
    if item_name!='' and item_name is not None:
        all_products=all_products.filter(title__contains=item_name)
    context={
        'all_products': all_products
        }
    return render(request,"home.html",context)



def display_one_data(request,slug):
    one_product_data=Product.objects.get(slug=slug)
    context={
            'one_product_data':one_product_data
        } 
    return render(request,"data.html",context)



def checkout(request):
    return render(request,"checkout.html")

def contact(request):
   form = CustomerForm(request.POST)
   if request.method=='POST':
       name=request.POST.get('name')
       mobileno=request.POST.get('mobileno')
       emailid=request.POST.get('emailid')
       pin=request.POST.get('pin')
       houseno=request.POST.get('houseno')
       area=request.POST.get('area')
       landmark=request.POST.get('landmark')
       city=request.POST.get('city')
       state=request.POST.get('state')
       totalprice=request.POST.get('totalprice')

       c=Custemer(name=name,mobileno=mobileno,emailid=emailid,pin=pin,houseno=houseno,area=area,landmark=landmark,city=city,state=state,totalprice=totalprice)
       c.save()
      

   
   return render(request,"contact.html")



   

   


      