from django.shortcuts import render
from .models import Product
from django.template import loader
from django.http import HttpResponse

from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

from  django.urls import reverse_lazy

from django.urls import reverse

# Create your views here.

def homeView(request):
    products = Product.objects.all() 
   
    context = {
        'product_list' : products,
        'current_page' : 'home'
    }

    template = loader.get_template('home.html')
    return HttpResponse(template.render(context,request))

def aboutView(request):
    context = {
        'current_page' : 'aboutPage'
    }
     
    template = loader.get_template('about.html')
    return HttpResponse(template.render(context,request))

class AddProduct(CreateView):
    model = Product
    fields = ['name','price','desc','pic','stock']
    template_name = 'addProduct.html'
    success_url = reverse_lazy('home')

# Read -> show details of each product
class ProductDetails(DeleteView):
    model = Product
    template_name = 'prod_details.html'
    context_object_name = 'prod'

# Update ->
class UpdateProduct(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'editProduct.html'

    def get_success_url(self):
        return reverse('prod_details',kwargs={'pk' : self.object.pk})
    
# Delete ->
class DeleteProduct(DeleteView):
    model = Product
    template_name = 'deleteProduct.html'
    success_url = reverse_lazy('home')


## Search results

def searchView(request):
    query = request.GET.get('search_text')
    #fetch the query text from GET request

    results = Product.objects.filter(name__icontains = query)
    # collect the product objects matching the name
    # This runs 'SELCT * FROM product WHERE  name like '%<query>%';
    # icontains is case-insensitive
    # contains can be used for case-sensitive 

    context = {
        'items' : results,
        'query' : query
    }

    template = loader.get_template('searchResults.html')
    return HttpResponse(template.render(context,request))