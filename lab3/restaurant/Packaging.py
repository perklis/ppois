from restaurant.kitchen.DishCategory import DishCategory


class Packaging:
    def __init__(self):
        self.type_name = None
        self.material = None
        self.is_ready = True
        self.is_used = False

    def choose_packaging(self, category: DishCategory):
        name = category.name.lower()
        if "drink" in name:
            self.type_name = "Cup"
            self.material = "Plastic"
        elif "soup" in name:
            self.type_name = "Bowl"
            self.material = "Paper"
        elif "pizza" in name or "roll" in name:
            self.type_name = "Box"
            self.material = "Cardboard"
        else:
            self.type_name = "Container"
            self.material = "Plastic"
        print(f"Chosen {self.type_name} for {category.name}")

    def pack_dish(self, dish_name: str, category: DishCategory):
        if not self.is_ready:
            print(f"Packaging not ready for {dish_name}")
            return False
        if not self.type_name:
            self.choose_packaging(category)
        self.is_used = True
        print(f"{dish_name} packed in {self.type_name}")
        return True

    def prepare(self):
        self.is_ready = True
        self.is_used = False
        print("Packaging is ready")

    def mark_used(self):
        self.is_ready = False
        self.is_used = True
        print("Packaging marked as used")

    def get_info(self) -> str:
        return (
            f"Type: {self.type_name}\n"
            f"Material: {self.material}\n"
            f"Ready: {self.is_ready}\n"
            f"Used: {self.is_used}"
        )
