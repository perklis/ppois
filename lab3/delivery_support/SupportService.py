from typing import List
from delivery_support.IssueReport import IssueReport


class SupportService:
    def __init__(self):
        self._issues: List[IssueReport] = []

    def register_issue(self, issue: IssueReport):
        self._issues.append(issue)
        print(f"Issue registered for order #{issue.order.order_number}")

    def show_all_issues(self):
        if not self._issues:
            print("No issues registered")
            return
        for issue in self._issues:
            issue.show_issue()
            print("-" * 40)

    def resolve_issue(self, order_number: int):
        found = False
        for issue in self._issues:
            if issue.order.order_number == order_number:
                issue.resolve()
                found = True
        if not found:
            print(f"No issue found for order #{order_number}")
