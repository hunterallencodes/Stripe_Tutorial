from django.test import TestCase
from datetime import date, timedelta
import datetime

from .models import User


class PaymentTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username="test"
        )
        self.user.save()

    def test_has_paid(self):
        self.assertFalse(
            self.user.has_paid(),
            "Initial user should have empty paid_until attr"
        )

    def test_diff_date_values(self):
        current_date = date(2021, 1, 4)
        _30days = timedelta(days=30)
        self.user.set_paid_until(current_date + _30days)
        self.assertTrue(
            self.user.has_paid(
                current_date=current_date
            )
        )
        self.user.set_paid_until(current_date - _30days)
        self.assertFalse(
            self.user.has_paid(
                current_date=current_date
            )
        )
