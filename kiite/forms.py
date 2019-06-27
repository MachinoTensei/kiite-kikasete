from django import forms
from .models import Story
from django.core.exceptions import ValidationError

class StoryForm(forms.ModelForm):
	class Meta:
		model = Story
		fields = ("title", "text", "ps")

