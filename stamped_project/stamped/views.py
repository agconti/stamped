# Create your views here.
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# handle javascript varaible transfer 
import json
from django.core.serializers.json import DjangoJSONEncoder


from stamped.models import Restaurant

def home(request):
	return render(request, "stamped/home.html")

def results(request):
	# import sys
	# sys.stdout.write("\nresults view action\n")
	# sys.stdout.write(result){'result':result}
	#context = get_object_or_404(Restaurant, pk=1)
	#restaurant.review_set.all()
	return render(request, "stamped/restaurant.html")

def feed_home(request):
	category_choices = [
					('asian', 'Asian'),
					('american', 'American'),
					('bar_food', 'Bar Food'),
					('seafood', 'Seafood'),
					('sandwiches', 'Sandwiches'),
					('french', 'French'),
					('comfortfood', 'Comfort Food'),
					('suhi', 'Sushi Bar'),
					('unknown_cat', 'To cool to be defined')	
				]
	
	import random
	top_choices = []
	for i in xrange(0, 3):
		category = random.choice(category_choices)
		top_5 = Restaurant.objects.filter(category=category[0]).order_by('rating')[:5]
		top_choices.append(top_5)
	import sys; sys.stdout.write(str(len(top_choices)))
	return render(request, "stamped/feed.html", {'top_choices': top_choices} )