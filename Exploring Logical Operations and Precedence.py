# Task 1: Validating Calculations
expression = 2 + 3 * 5
expression_with_parentheses = (2 + 3) * 5
match = expression == expression_with_parentheses
print(match)

# Task 2: Mix and Match
mix_match_expression = 8 + 5 % 4 // 6 > 9 + 2 * 3 or 7 >= 2 + 5 - 4 % 2 # I predict this expression will evaluate to True
print(mix_match_expression)
