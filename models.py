from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  def __str__(self):
        return self.question_text
  def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
  question = models.ForeignKey(Question,on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  def __str__(self):
        return self.choice_text
# それぞれdjango.db.models.Modelのサブクラス
# charfield⇢文字のフィールド
# datetimefield⇢日時フィールド
# ForeignKey⇢外部キー

class Data6369 (models.Model):
      index = models.IntegerField(null=False,blank=False)
      start_week = models.CharField(max_length=255,null=False,blank=False)
      end_week = models.CharField(max_length=255,null=False,blank=False)
      start_price = models.FloatField(null=False,blank=False)
      last_price = models.FloatField(null=False,blank=False)
      high_price = models.FloatField(null=False,blank=False)
      lowprice = models.FloatField(null=False,blank=False)
      rsi = models.FloatField(null=False,blank=False)
      moveaverage = models.FloatField(null=False,blank=False)
      stdev = models.FloatField(null=False,blank=False)
      bb = models.FloatField(null=False,blank=False)
      def __str__(self):
            return self.index
