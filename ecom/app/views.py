from django.shortcuts import render
from django.views import View


from .models import Customer,Product,Cart,Orderplaced
from .forms import CustomerRegistrationForm
from django.contrib import messages

#Class-based view
class ProductView(View):
    def get(self,request):
        topwears=Product.objects.filter(category="TW")
        bottomwears=Product.objects.filter(category="BW")
        mobile=Product.objects.filter(category="M")
        laptop=Product.objects.filter(category="L")
        return render(request,'app/home.html',{'topwears':topwears,'bottomwears':bottomwears,'mobile':mobile,'laptop':laptop})

#Class-based view
class Product_detail(View):
    def get(self,request,pk):
        products=Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',{'product':products})
#Function based view
def mobile(request,data=None):
    if data==None:
        mobiles=Product.objects.filter(category="M")
    elif data=='Redmi':
        mobiles=Product.objects.filter(category="M").filter(category=data)
    elif data=='samsung':
        mobiles=Product.objects.filter(category="M").filter(category=data)   
    return render(request,'app/mobile.html',{'mobile':mobiles})

def laptop(request,data=None):
    if data==None:
        laptop=Product.objects.filter(category='L')
    elif data=='belw10000':
        laptop=Product.objects.filter(category='L').filter(selling_price__lte=100000)
    elif data=='belw20000':
        laptop=Product.objects.filter(category='L').filter(selling_price__lte=20000)
    return render(request,'app/laptop.html',{'laptop':laptop})




class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Registeration Sucess')
            form.save()
        return render(request, 'app/customerregistration.html',{'form':form})
        
def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')




def checkout(request):
 return render(request, 'app/checkout.html')
