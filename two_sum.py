from typing import List, Optional

class Solution:
    def two_sum(self, nums: List[int], target: int) -> Optional[List[int]]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return None




solution = Solution()

# Тест 1: Обычный случай
print(solution.two_sum([2, 7, 11, 15], 9))  # Ожидаемый результат: [0, 1]

# Тест 2: Нет решения
print(solution.two_sum([1, 2, 3, 4], 10))  # Ожидаемый результат: None

# Тест 3: Числа с отрицательными значениями
print(solution.two_sum([-1, -2, -3, -4, -5], -8))  # Ожидаемый результат: [2, 4]

# Тест 4: Дубликаты в списке
print(solution.two_sum([3, 3, 4, 5], 6))  # Ожидаемый результат: [0, 1]

# Тест 5: Список из одного элемента (должно вернуть None)
print(solution.two_sum([5], 5))  # Ожидаемый результат: None
