class MultiSet:
    OPEN_BRACE = '{'
    CLOSE_BRACE = '}'
    COMMA = ','

    def __init__(self, data=None, name=None):
        self._elements, self.name = {}, name
        if not data:
            return
        if not self._validate(data):
            raise ValueError("Некорректный ввод")
        self.clear_and_pass_to_parser_string(data)

    def _validate(self, string: str) -> bool:
        if not string or len(string) < 2:
            return False
        if string[0] != self.OPEN_BRACE or string[-1] != self.CLOSE_BRACE:
            return False

        braces_counter, last_symbol = 0, ""
        for index, symbol in enumerate(string):
            if symbol == self.OPEN_BRACE:
                braces_counter += 1
                last_symbol = symbol
                continue
            if symbol == self.CLOSE_BRACE:
                braces_counter -= 1
                if braces_counter < 0:
                    return False
                last_symbol = symbol
                continue
            if symbol == self.COMMA and self._check_comma(index, string, last_symbol):
                return False
            last_symbol = symbol
        return braces_counter == 0

    def _check_comma(self, index, string, last_symbol) -> bool:
        return (
            index == 0
            or index == len(string) - 1
            or last_symbol == self.COMMA
            or (index + 1 < len(string) and string[index + 1] == self.CLOSE_BRACE)
        )

    def clear_and_pass_to_parser_string(self, data):
        if not data:
            return
        inside_data = data[1:-1].replace(' ', '')
        self._set_parser(inside_data)

    def _set_parser(self, inside_data: str):
        index = 0
        while index < len(inside_data):
            char = inside_data[index]

            if char == self.OPEN_BRACE:
                index, nested_set = self._nested_set_parser(inside_data, index)
                self.add(nested_set.name)
                continue
            if char == self.COMMA:
                index += 1
                continue

            index, element = self._parse_element(inside_data, index)
            if element:
                self.add(element)

    def _nested_set_parser(self, inside_data: str, start_brace_index: int):
        current_index, braces_count = start_brace_index + 1, 1

        while current_index < len(inside_data) and braces_count > 0:
            if inside_data[current_index] == self.OPEN_BRACE:
                braces_count += 1
            elif inside_data[current_index] == self.CLOSE_BRACE:
                braces_count -= 1
            current_index += 1

        nested_data = inside_data[start_brace_index:current_index]
        nested_subset = MultiSet(nested_data, name=nested_data)
        return current_index, nested_subset

    def _parse_element(self, inside_data: str, start: int):
        current_index = start
        while current_index < len(inside_data) and inside_data[current_index] not in [self.COMMA, self.OPEN_BRACE, self.CLOSE_BRACE]:
            current_index += 1
        element = inside_data[start:current_index].strip()
        return current_index, element if element else None

    def add(self, element_name):
        self._elements[element_name] = self._elements.get(element_name, 0) + 1

    def remove(self, element_name):
        if element_name not in self._elements:
            return False
        self._elements[element_name] -= 1
        if self._elements[element_name] <= 0:
            del self._elements[element_name]
        return True

    def is_empty(self):
        return not self._elements

    def __len__(self):
        return sum(self._elements.values())

    def __contains__(self, element):
        return element in self._elements

    def union_of_sets(self, other):
        result = MultiSet()
        result._elements.update(self._elements)
        for element, count in other._elements.items():
            result._elements[element] = max(result._elements.get(element, 0), count)
        return result

    def intersection_of_sets(self, other):
        result = MultiSet()
        for element, count in self._elements.items():
            if element in other._elements:
                result._elements[element] = min(count, other._elements[element])
        return result

    def difference_of_sets(self, other):
        result = MultiSet()
        for element, count in self._elements.items():
            if element not in other._elements:
                result._elements[element] = count
                continue
            new_count = count - other._elements[element]
            if new_count > 0:
                result._elements[element] = new_count
        return result

    def boolean_of_set(self) -> str:
        elements = list(self._elements.keys())
        multiplicity = list(self._elements.values())
        all_subsets = []

        self._backtrack(0, {}, elements, multiplicity, all_subsets)
        subset_strings = [self._subset_to_str(subset) for subset in all_subsets]
        return "{" + ", ".join(subset_strings) + "}"

    def _subset_to_str(self, subset: dict) -> str:
        if not subset:
            return "{}"
        parts = []
        for key, value in subset.items():
            parts.extend([key] * value)
        return "{" + ",".join(parts) + "}"

    def _backtrack(self, index, subset_so_far, unique_elements, counts, boolean):
        if index == len(unique_elements):
            boolean.append({element: count for element, count in subset_so_far.items() if count > 0})
            return
        element = unique_elements[index]
        for count in range(counts[index] + 1):
            subset_so_far[element] = count
            self._backtrack(index + 1, subset_so_far, unique_elements, counts, boolean)
        subset_so_far.pop(element, None)

    def __str__(self):
        if not self._elements:
            return "{}"
        items = []
        for key, value in self._elements.items():
            items.extend([key] * value)
        return "{" + ",".join(items) + "}"


ms1 = MultiSet("{1,0,{2},{3}}")
ms2 = MultiSet("{1,  5, {2,3}}")
empty = MultiSet("{}")
single = MultiSet("{x}")
nested = MultiSet("{a,{b,{c}}}")
print("Множество 1:", ms1)
print("Множество 2:", ms2)
print("Пустое множество:", empty)
print("Один элемент множество:", single)
print("Вложенное множество:", nested)

print("Мощность ms1:", len(ms1))
print("ms1 '1'?", '1' in ms1)
print("ms1 '5'?", '5' in ms1)

ms1.remove("3")
print("После удаления '3':", ms1)
ms1.remove("{3}")
print("После удаления '{3}':", ms1)
print("Объединение:", ms1.union_of_sets(ms2))
print("Пересечение:", ms1.intersection_of_sets(ms2))
print("Разность:", ms1.difference_of_sets(ms2))
print("\nБулеан множества 1:")

print(ms1.boolean_of_set())


