import unittest
from employees.Employee import Employee
from employees.Economist import Economist
from employees.base_salaries import BASE_SALARIES


class TestEconomist(unittest.TestCase):
    def setUp(self):
        self.economist = Economist(
            name="Ivan",
            age=40,
            work_experience=10,
            department="Finance",
            monthly_budget=60000,
        )
        self.emp1 = Employee("Doctor", "Alice", 35, 5, 0)
        self.emp2 = Employee("Nurse", "Bob", 30, 3, 0)
        self.emp3 = Employee("Engineer", "Charlie", 28, 1, 0)

    def test_calculate_salary_known_title(self):
        salary = self.economist.calculate_salary(self.emp1)
        expected = BASE_SALARIES["Doctor"] + 50 * self.emp1.work_experience
        self.assertEqual(salary, expected)
        self.assertEqual(self.emp1.get_salary(), expected)

    def test_calculate_salary_unknown_title(self):
        unknown_emp = Employee("Janitor", "Dmitry", 45, 10, 0)
        salary = self.economist.calculate_salary(unknown_emp)
        self.assertEqual(salary, 800 + 50 * 10)

    def test_adjust_salaries_to_budget_within_budget(self):
        employees = [self.emp1, self.emp2, self.emp3]
        self.economist.adjust_salaries_to_budget(employees)
        total_after = sum(e.get_salary() for e in employees)
        self.assertLessEqual(total_after, self.economist.monthly_budget)
        self.assertEqual(self.economist.processed_employees, employees)

    def test_adjust_salaries_to_budget_exceeds_budget(self):
        econ = Economist("Anna", 35, 12, "Finance", monthly_budget=2000)
        employees = [self.emp1, self.emp2]
        for e in employees:
            e._set_salary(5000)
        econ.processed_employees = []
        econ.adjust_salaries_to_budget(employees)
        total = sum(e.get_salary() for e in employees)
        self.assertLessEqual(total, econ.monthly_budget or 2000)
        self.assertEqual(econ.processed_employees, employees)

    def test_calculate_all_salaries_within_budget(self):
        employees = [self.emp1, self.emp2, self.emp3]
        total = self.economist.calculate_all_salaries(employees)
        expected = sum(e.get_salary() for e in employees)
        self.assertEqual(total, expected)
        self.assertLessEqual(total, self.economist.monthly_budget)

    def test_calculate_all_salaries_exceeds_budget(self):
        econ = Economist("Olga", 50, 20, "Finance", monthly_budget=1000)
        employees = [self.emp1, self.emp2]
        total = econ.calculate_all_salaries(employees)
        self.assertLessEqual(total, econ.monthly_budget)
