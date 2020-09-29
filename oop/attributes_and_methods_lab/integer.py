class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if isinstance(value, float):
            result = Integer(int(value))
        else:
            result = 'value is not a float'

        return result

    @classmethod
    def from_roman(cls, value):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        i = 0
        num = 0
        while i < len(value):
            if i + 1 < len(value) and value[i:i + 2] in roman:
                num += roman[value[i:i + 2]]
                i += 2
            else:
                num += roman[value[i]]
                i += 1

        return Integer(num)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            result = Integer(int(value))
        else:
            result = 'wrong type'

        return result

    def add(self, integer):
        if isinstance(integer, Integer):
            result = self.value + integer.value
        else:
            result = 'number should be an Integer instance'

        return result