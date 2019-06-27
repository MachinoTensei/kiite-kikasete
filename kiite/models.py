from django.db import models
from django.core.validators import MinLengthValidator

class Story(models.Model):
	title = models.CharField("この小話、kiite...", help_text= '小話のタイトルを入力してください', max_length = 30)
	text = models.TextField("KIITE", help_text= 'どんな小話ですか？')
	author = models.ForeignKey("auth.User", verbose_name = "KIITE師", null = True, on_delete = models.SET_NULL)
	ps = models.CharField("P.S.", help_text= '最後に一言', max_length = 30, null = True)
	vote = models.IntegerField(default = 0)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __str__(self):
		return self.title


