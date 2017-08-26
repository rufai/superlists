from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

# Create your tests here.
class SomeTest(TestCase):
	"""docstring for SomeTest"""
	# def __init__(self, arg):
	# 	super(SomeTest, self).__init__()
	# 	self.arg = arg

	def test_bad_maths(self):
		self.assertEqual(1+1, 3)
		
class HomePageTest(TestCase):
	"""docstring for HomePageTest"""
	def __init__(self, arg):
		super(HomePageTest, self).__init__()
		self.arg = arg

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)
		
