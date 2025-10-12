import unittest
from employees.Engineer import Engineer
from equipment.Equipment import Equipment


class TestEngineer(unittest.TestCase):
    def setUp(self):
        self.engineer = Engineer(
            name="Alice",
            age=30,
            work_experience=5,
            specialization="Mechanical",
            department="Maintenance",
            salary=3000,
        )
        self.equipment1 = Equipment("X-Ray", "123")
        self.equipment2 = Equipment("MRI", "456")

    def test_add_equipment_new(self):
        msg = self.engineer.add_equipment(self.equipment1)
        self.assertIn("is now responsible", msg)
        self.assertIn(self.equipment1, self.engineer._Engineer__equipment_list)

    def test_add_equipment_duplicate(self):
        self.engineer.add_equipment(self.equipment1)
        msg = self.engineer.add_equipment(self.equipment1)
        self.assertIn("already maintains", msg)

    def test_add_equipment_wrong_type(self):
        with self.assertRaises(TypeError):
            self.engineer.add_equipment("not equipment")

    def test_check_equipment_assigned(self):
        self.engineer.add_equipment(self.equipment1)
        msg = self.engineer.check_equipment(self.equipment1)
        self.assertIn("checked by Alice", msg)

    def test_check_equipment_unassigned(self):
        msg = self.engineer.check_equipment(self.equipment2)
        self.assertIn("isn't assigned", msg)

    def test_repair_equipment_broken(self):
        self.engineer.add_equipment(self.equipment1)
        self.equipment1.break_down()
        msg = self.engineer.repair_equipment(self.equipment1)
        self.assertIn("repaired and now is working", msg)

    def test_repair_equipment_working(self):
        self.engineer.add_equipment(self.equipment1)
        msg = self.engineer.repair_equipment(self.equipment1)
        self.assertIn("already working", msg)

    def test_repair_equipment_unassigned(self):
        msg = self.engineer.repair_equipment(self.equipment2)
        self.assertIn("can't repair", msg)

    def test_list_equipment_empty(self):
        msg = self.engineer.list_equipment()
        self.assertIn("has no assigned equipment", msg)

    def test_list_equipment_non_empty(self):
        self.engineer.add_equipment(self.equipment1)
        self.engineer.add_equipment(self.equipment2)
        msg = self.engineer.list_equipment()
        self.assertIn("X-Ray", msg)
        self.assertIn("MRI", msg)

    def test_str_representation(self):
        self.engineer.add_equipment(self.equipment1)
        s = str(self.engineer)
        self.assertIn("Alice", s)
        self.assertIn("Mechanical", s)
        self.assertIn("1", s)
