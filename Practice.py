programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages: print(language)


even_num = [num for num in range(21) if num % 2 == 0]
print(even_num)

num_by_parity = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in range(6)]
print(num_by_parity)
