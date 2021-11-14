from django.test import TestCase
from .models import  Initiative,Profile,Wallet,Contributor
from django.contrib.auth.models import User
# Create your tests here.
class InitiativeTestCase(TestCase):
            def setUp(self):
                              self.user = User(username='Kipkorir')
                              self.user.save()
                              self.initiative=Initiative(user = self.user,name='School funds',description='raising school funds',target_amount=50000.00, due_date="2021-12-12")
                              self.initiative.save_initiative()
                              self.contributor = Contributor(user = self.user,initiative=self.initiative,contributor_name = 'Benjamin',phone_number = '070456783',email='benja@gmail.com')
                              self.contributor.save()
                              self.profile = Profile(id=12 ,initiative=self.initiative ,contributor=self.contributor,user=self.user)
            def test_instance(self):
                              self.assertTrue(isinstance(self.initiative, Initiative))
            def test_save_initiative(self):
                              self.initiative.save_initiative()
                              initiative= Initiative.objects.all()
                              self.assertTrue(len(initiative) > 0)
            def test_delete_initiative(self):
                              self.initiative.delete_initiative()
                              initiative = Initiative.objects.all()
                              self.assertTrue(len(initiative) <= 0)
class  ContributorTestCase(TestCase):
            def setUp(self):
                              self.user = User(username='Kipkorir')
                              self.user.save()
                              self.initiative=Initiative(user = self.user,name='School funds',description='raising school funds',target_amount=50000, due_date="2021-12-12")
                              self.initiative.save_initiative()
                              self.contributor = Contributor(user = self.user,initiative=self.initiative,contributor_name = 'Benjamin',phone_number = '070456783',email='benja@gmail.com')
                              self.contributor.save()
                              self.profile = Profile(id=12 ,initiative=self.initiative ,contributor=self.contributor, user=self.user)
            def test_instance(self):
                              self.assertTrue(isinstance(self.contributor, Contributor))
            def test_save_contributor(self):
                              self.contributor.save_contributor()
                              contributor= Contributor.objects.all()
                              self.assertTrue(len(contributor) > 0)
            def test_delete_contribiutor(self):
                              self.contributor.delete_contributor()
                              contributor = Contributor.objects.all()
                              self.assertTrue(len(contributor) <= 0)
class ProfileTestCase(TestCase):
            def setUp(self):
                              self.user = User(username='Kipkorir')
                              self.user.save()
                              self.initiative=Initiative(user = self.user,name='School funds',description='raising school funds',target_amount=50000, due_date="2021-12-12")
                              self.initiative.save_initiative()
                              self.contributor = Contributor(user = self.user,initiative=self.initiative,contributor_name = 'Benjamin',phone_number = '070456783',email='benja@gmail.com')
                              self.contributor.save()
                              self.profile = Profile(id=12 ,initiative=self.initiative ,contributor=self.contributor,
                                    user=self.user)
            def test_instance(self):
                              self.assertTrue(isinstance(self.profile, Profile))
            def test_save_profile(self):
                              self.profile.save_profile()
                              profile = Profile.objects.all()
                              self.assertTrue(len(profile) >0)
            def test_update_profile(self):
                              self.profile.save_profile()
                              self.profile.update_profile(self.profile.user_id)
                              self.profile.save_profile()
                              self.assertTrue(Profile,self.profile.user)
class WalletTestCase(TestCase):
            def setUp(self):
                              self.user = User(username='Kipkorir')
                              self.user.save()
                              self.initiative=Initiative(user = self.user,name='School funds',description='raising school funds',target_amount=50000, due_date="2021-12-12")
                              self.initiative.save_initiative()
                              self.wallet=Wallet(user = self.user,initiative = self.initiative,total_contributions=60000)
                              self.contributor = Contributor(user = self.user,initiative=self.initiative,contributor_name = 'Benjamin',phone_number = '070456783',email='benja@gmail.com')
                              self.contributor.save()
                              self.profile = Profile(id=12 ,initiative=self.initiative ,contributor=self.contributor,user=self.user)
            def test_instance(self):
                              self.assertTrue(isinstance(self.wallet, Wallet))
            def test_save_wallet(self):
                              self.wallet.save_wallet()
                              wallet= Wallet.objects.all()
                              self.assertTrue(len(wallet) > 0)
            def test_delete_wallet(self):
                              self.wallet.save_wallet()
                              self.wallet.delete_wallet()
                              wallet = Wallet.objects.all()
                              self.assertTrue(len(wallet) <= 0)





















