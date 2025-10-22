import unittest
from unittest.mock import Mock
from datetime import datetime
from client.Review import Review
from delivery_support.IssueReport import IssueReport
from exceptions import RatingInputError


class TestReview(unittest.TestCase):
    def setUp(self):
        self.order = Mock()
        self.order.order_number = 1
        self.order.status = "DELIVERED"

        self.client = Mock()
        self.client.name = "Olya"

    def test_good_review(self):
        review = Review(self.order, self.client, rating=5, comment="Perfect")
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, "Perfect")
        self.assertIsNone(review.issue)
        self.assertIsInstance(review.created_at, datetime)
        self.assertEqual(review.client, self.client)
        self.assertEqual(review.order, self.order)

    def test_bad_review(self):
        review = Review(self.order, self.client, rating=3, comment="Not delicious")
        self.assertIsNotNone(review.issue)
        self.assertIsInstance(review.issue, IssueReport)
        self.assertEqual(review.issue.description, "Not delicious")

    def test_review_without_comm(self):
        review = Review(self.order, self.client, rating=2)
        self.assertIsNotNone(review.issue)
        self.assertEqual(review.issue.description, "No comment provided")

    def test_invalid_rating(self):
        with self.assertRaises(RatingInputError):
            Review(self.order, self.client, rating=6)

        with self.assertRaises(RatingInputError):
            Review(self.order, self.client, rating=0)

    def test_not_delivered_order(self):
        self.order.status = "IN_PROGRESS"
        with self.assertRaises(ValueError):
            Review(self.order, self.client, rating=4, comment="Test")
