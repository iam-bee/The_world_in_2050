from datetime import datetime
now = datetime.now()

def get_population():
    try:
        age = int(input('Enter your age: '))
        year = now.year
        population = 7850000000
        population_2020 = 7850000000
        while year < 2050:
            age += 1
            year += 1
            population *= 1.01
            print(f'In {year} the world population will be {population}') 
            print(f'You will be {age} years old \n')
            #if age > 120:
               # break
            if year == 2050:
                print(f'There will be {population - population_2020} more inhabitants compared to 2020')
    except ValueError:
        print('Please enter a valid age')
world_population = get_population()
