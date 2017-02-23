import datetime
from django.utils import timezone
from django.test import TestCase

from .models import Question

class QuestionMethodTests(TestCase):
    """
    was_published_recently() should return False for questions whose
    pub_date is in the future.
    """
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

# Create your tests here.
