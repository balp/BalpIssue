"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from balpissueapp.models import *
from django.utils import timezone

class ModelProjectTest(TestCase):
    def testAProjectCanHaveIssues(self):
        sut = Project()
        sut.name = "Test"
        sut.save()
        sut.issue_set.create(title="One", pub_date=timezone.now())
        self.assertEqual(1, sut.issue_set.count())

        
