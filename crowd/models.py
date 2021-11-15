from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Initiative(models.Model):
  
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  description = models.TextField(max_length=3000)
  due_date = models.DateField(blank=True,null=True)
  target_amount = models.FloatField()
  
  def __str__(self):
               return self.name
  def save_initiative(self):
               self.save()

  def delete_initiative(self):
               self.delete()
  

class Contributor(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  initiative = models.ForeignKey(Initiative,on_delete=models.CASCADE)
  contributor_name = models.CharField(max_length=100)
  phone_number = models.CharField(max_length=10)
  email = models.EmailField()
  
  def __str__(self):
               return self.contibuter_name
  def save_contributor(self):
               self.save()

  def delete_contributor(self):

               self.delete()  

  
class Profile(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  initiative = models.ForeignKey(Initiative,on_delete=models.CASCADE)
  contributor = models.ForeignKey(Contributor,on_delete=models.CASCADE)
  
  def __str__(self):
               return self.user.username
  def save_profile(self):
               self.save()

  def delete_profile(self):
               self.delete()  
  def update_profile(cls, id):
        Profile.objects.get(user_id=id)
  
class Wallet(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  initiative = models.ForeignKey(Initiative,on_delete=models.CASCADE)
  total_contributions =  models.FloatField()
  
  def __str__(self):
               return self.initiative.name

  def save_wallet(self):
               self.save()

  def delete_wallet(self):

               self.delete()  


