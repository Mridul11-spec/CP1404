import random

MAX_INCREASE = 1
MAX_DECREASE = 2
MIN_POPULATION = 100
MAX_POPULATION = 2000
STARTING_POPULATION = 1000

population = (STARTING_POPULATION)
year = 0
print("Welcome to the Gopher Population Simulator!")
print("Starting population: ", population)


while population >= MIN_POPULATION and population <= MAX_POPULATION:
    percentage_decrease = random.randint(5, 25)
    percentage_increase = random.randint(10, 20)

    population_decrease = population * percentage_decrease // 100
    population_increase = population * percentage_increase // 100
    year += 1

    population = population + population_increase - population_decrease
    print(population_increase, "gophers were born", population_decrease, "died")
    print("Population: ", population)
    print("Year" , year)
