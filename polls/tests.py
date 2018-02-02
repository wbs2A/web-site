import datetime
from .models import Question
from django.test import Client
from django.test import TestCase
from django.utils import timezone
from django.test.utils import setup_test_environment
# Create your tests here.

class QuestionModelTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() returns False
		 for questions whose pub_date is in the future.
		"""
		time = timezone.now()+datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		""" was_published_recently() returns False for question whose pub_date
		is older than 1 day.
		"""
		time = timezone.now()- datetime.timedelta(days=1, seconds=1)
		old_question = Question(pub_date=time)
		self.assertIs(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		"""was_published recently() returns True for questions whose pub_date
		is within the last day.
		"""
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		recent_question = Question(pub_date=time)
		self.assertIs(recent_question.was_published_recently(), True)

class ClientResponseTests(TestCase):
	#Test the response from '/'
	def test_response_with_initial_page(self):
		client = Client()
		response = client.get('/')
		self.assertIs(response.status_code,200)

	def test_response_with_polls_page(self):
		client = Client()
		response = client.get('/polls/')
		self.assertIs(response.status_code,200)
	