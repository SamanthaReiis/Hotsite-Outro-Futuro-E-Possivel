from django.shortcuts import render
from django.http import HttpResponse
from .models import Report, Item, Podcast, Storie
from django.views.generic import ListView, DetailView

# Create your views here.
#def Post_listView(request, id):
 #   reports = Report.objects.get(id=id)
  #  return render(request, "hotsite/post_list.html", {"reports": reports})

#def HomeView (request):
 #   return render(request, "hotsite/home.html", {})



class ReportView(ListView):
	model = Report
	template_name = "hotsite/home.html"

	def image(request):
		return render (request, "hotsite/home.html", {'image': Report.objects.get(pk=1)})

#class ItemView(ListView):
    
 #   model = Item 
  #  template_name =  "hotsite/post_list.html"

   # def Video(request):

    #	return render (request, "hotsite/post_list.html", {'video': EmbedVideoField () } )

#class PodcastView(object):

 #   model = Podcast 
  #  template_name =  "hotsite/post_list.html"

#class StorieView(object):
	
#	model = Storie
#	template_name =  "hotsite/post_list.html"
