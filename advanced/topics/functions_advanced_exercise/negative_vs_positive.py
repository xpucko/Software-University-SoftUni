def solve(nums):
    numbers = [int(x) for x in nums.split()]
    positives_sum = sum([x for x in numbers if x > 0])
    negatives_sum = sum([x for x in numbers if x < 0])
    if positives_sum < abs(negatives_sum):
        result = 'The negatives are stronger than the positives'
    else:
        result = 'The positives are stronger than the negatives'

    return f'{negatives_sum}\n{positives_sum}\n{result}'


print(solve(input()))