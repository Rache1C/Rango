from rango.forms import CategoryForm
from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories':category_list}
	
	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	return HttpResponse("Rango says here is the about page.")

def show_category(request, category_name_slug):
	context_dict = {}

	try:
		category = Category.objects.get(slug=category_name_slug)

		pages = Page.objects.filter(category=category)

		context_dict['pages'] = pages

		context_dict['category'] = category
	except Category.DoesNotExist:
		context_dict['pages'] = None

		context_dict['category'] = None
	return render(request, 'rango/category.html', context=context_dict)

def add_category(request):
	form = CategoryForm()

	# A HTTP POST?
	if request.method == 'POST':
		form = CategoryForm(request.POST)

		# Have we been provided with a valid form?
		if form.is_valid():
		# Save the new category to the database.
		form.save(commit=True)
		# Now that the category is saved
		# We could give a confirmation message
		# But since the most recent category added is on the index page
		# Then we can direct the user back to the index page.
		return index(request)
	else:
# The supplied form contained errors -
# just print them to the terminal.

		print(form.errors)
		
# Will handle the bad form, new form, or no form supplied cases.
# Render the form with error messages (if any).
return render(request, 'rango/add_category.html', {'form': form})
