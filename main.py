class Solution:
    def romanToInt(self, s: str) -> int:
        rule_add = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        rule_div = {
            ('I', 'V'): 3,
            ('I', 'X'): 8,
            ('X', 'L'): 30,
            ('X', 'C'): 80,
            ('C', 'D'): 300,
            ('C', 'M'): 800,
        }

        if not 1 <= len(s) <= 15:  # проверка диапозона
            raise Exception('Нарушен диапазон 1 < s < 15')

        for symbol in s:  # проверка на корректность "валидация?"
            if not symbol in rule_add.keys():
                raise Exception('Недопустимые символы')

        # if not (s.count('V') or s.count('L') or s.count('D')) <= 1:
        #     raise Exception('Цифры V, L, D не могут повторяться')
        #
        # if s.count('IIII') or s.count('XXXX') or s.count('CCCC') or s.count('MMMM'):
        #     raise Exception('Цифры I, X, C, M не могут повторяться больше трёх раз подряд')

        number = 0
        prev_symbol = None
        for symbol in s:  # итерируемся по строке
            if prev_symbol and rule_add[prev_symbol] < rule_add[symbol]:  # если текущее значение больше предыдущего
                number += rule_div[
                    (prev_symbol, symbol)]  # прибавляем теущее значение уменьшеное на удвоенное предыдущее
            else:
                number += rule_add[symbol]
            prev_symbol = symbol

        if not 1 <= number <= 3999:
            raise Exception('Нарушение возможного диапазона')

        return number


if __name__ == "__main__":
    result = Solution()
    print(result.romanToInt(str(input('s = '))))