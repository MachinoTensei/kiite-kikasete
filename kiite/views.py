from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Story
from .forms import StoryForm

def home(request):
	random_query_set = Story.objects.order_by("?")[:1]
	latest_story = Story.objects.order_by("-created_at")[:100]
	context = {"latest_story": latest_story,
					"random_query_set": random_query_set,
					}
	return render(request, "kiite/home.html", context)

def detail(request, id):
	story = get_object_or_404(Story, pk = id)
	context = {"story": story}
	return render(request, "kiite/detail.html", context)

def new(request):
	storyForm = StoryForm
	context = {"storyForm": storyForm}
	return render(request, "kiite/new.html", context)

def create(request):
	storyForm = StoryForm(request.POST)
	if storyForm.is_valid():
		story = storyForm.save()
		context = {"story": story}
		return render(request, "kiite/detail.html", context)
	

def edit(request, id):
	story = get_object_or_404(Story, pk = id)
	storyForm = StoryForm(instance = story)
	context = {"story": story, "storyForm": storyForm}
	return render(request, "kiite/edit.html", context)

def update(request, id):
	story = get_object_or_404(Story, pk = id)
	storyForm = StoryForm(request.POST, instance = story)
	if storyForm.is_valid():
		storyForm.save()
	context = {"story": story}
	return render(request, "kiite/detail.html", context)
