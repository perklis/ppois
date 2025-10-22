import unittest
from unittest.mock import Mock
from delivery_support.SupportService import SupportService


class TestSupportService(unittest.TestCase):
    def setUp(self):
        self.service = SupportService()
        self.mock_issue1 = Mock()
        self.mock_issue1.order.order_number = 101
        self.mock_issue1.show_issue = Mock()
        self.mock_issue1.resolve = Mock()

        self.mock_issue2 = Mock()
        self.mock_issue2.order.order_number = 102
        self.mock_issue2.show_issue = Mock()
        self.mock_issue2.resolve = Mock()

    def test_register_issue(self):
        self.service.register_issue(self.mock_issue1)
        self.assertIn(self.mock_issue1, self.service._issues)

    def test_show_all_issues(self):
        self.service.register_issue(self.mock_issue1)
        self.service.register_issue(self.mock_issue2)
        self.service.show_all_issues()
        self.mock_issue1.show_issue.assert_called_once()
        self.mock_issue2.show_issue.assert_called_once()

    def test_resolve_issue_existing(self):
        self.service.register_issue(self.mock_issue1)
        self.service.resolve_issue(101)
        self.mock_issue1.resolve.assert_called_once()

    def test_resolve_issue_nonexistent(self):
        self.service.register_issue(self.mock_issue1)
        self.service.resolve_issue(999)
        self.mock_issue1.resolve.assert_not_called()
