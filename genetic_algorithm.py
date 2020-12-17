from random import uniform
from random import randint

gene_number = 5
chromosome_number = 10
generations_count = 10000
mutation_chance = 0.01
equation_coef = [randint(1, 10) for i in range(gene_number)]
equation_sum = 27


def genetic_algorithm():
    population = initialize_population(gene_number, chromosome_number)
    # Подсчет фит функции
    population = fitness(population)
    for i_to_limit in range(generations_count):
        # Размножение (создание потомков)
        new_population = crossover(population)
        # Мутация
        new_population = mutation(new_population)
        # Подсчет фит функции
        new_population = fitness(new_population)
        population = new_population
    return population


def initialize_population(gene_number, chromosome_number):
    population = []
    for chromosome in range(chromosome_number):
        population.append([])
        for gene in range(gene_number):
            population[-1].append(round(uniform(0.01, 100), 2))
    return population


def equation(chromosome, equation_coef):
    value = 0
    for index, gene in enumerate(chromosome):
        value += gene * equation_coef[index]
    return value


def fitness(population):
    values = {}
    for i, chromosome in enumerate(population):
        values[i] = equation(chromosome, equation_coef)  # index : value

    _values = []

    for index in values:
        _values.append((index, values[index]))

    probabilities = []
    for index, eqvalue in _values:
        probabilities.append((index, abs(eqvalue - equation_sum)))
    # Подсчет вероятностей для того, чтобы выбрать наилучших потомков
    probabilities.sort(key=lambda tup: tup[1])
    probabilities = probabilities[:chromosome_number]

    new_population = []
    for index, percentage in probabilities:
        new_population.append(population[index])

    return new_population


def crossover(population):
    new_population = []
    for i, chromosome_i in enumerate(population):
        for j in range(i + 1, len(population)):  # i+1 для того, чтобы не был выбран тот же родитель дважды
            parent_1 = population[i]
            parent_2 = population[j]
            new_parent_1_left = parent_1[:len(parent_1) // 2]
            new_parent_1_right = parent_2[len(parent_1) // 2:]
            new_parent_2_left = parent_2[:len(parent_2) // 2]
            new_parent_2_right = parent_1[len(parent_2) // 2:]
            new_parent_1 = []
            new_parent_1.extend(new_parent_1_left)
            new_parent_1.extend(new_parent_1_right)
            new_parent_2 = []
            new_parent_2.extend(new_parent_2_left)
            new_parent_2.extend(new_parent_2_right)
            new_population.append(new_parent_1)
            new_population.append(new_parent_2)

    return new_population


def mutation(population):
    for i, chromosome in enumerate(population):
        if round(uniform(0, 1), 2) <= mutation_chance:
            population[i][randint(0, len(chromosome)) - 1] = round(uniform(0.01, 100), 2)
    return population


print(f'Equation coef is {equation_coef}')
print(f'Equation sum is {equation_sum}')
print('Algorithm working, this may take some time...')
population = genetic_algorithm()
print(f'Best result is : chromosome {population[0]} sum  {equation(population[0], equation_coef)}')
