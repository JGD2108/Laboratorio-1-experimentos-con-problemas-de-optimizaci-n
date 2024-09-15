import pandas as pd
from sympy import symbols, diff, ln
from tabulate import tabulate
import random
import numpy as np

class GeneticAlgorithm:
    def __init__(self, func, population_size, num_generations, mutation_rate):
        self.func = func
        self.population_size = population_size
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate
        self.x = symbols('x')
        self.population = []
        self.best_individual = None
        self.best_fitness = float('inf')

    def initialize_population(self):
        self.population = [random.uniform(-10, 10) for _ in range(self.population_size)]

    def fitness(self, individual):
        return abs(self.func.subs(self.x, individual))

    def select_parents(self):
        fitnesses = [self.fitness(ind) for ind in self.population]
        return random.choices(self.population, weights=[1/f for f in fitnesses], k=2)

    def crossover(self, parent1, parent2):
        alpha = random.random()
        child = alpha * parent1 + (1 - alpha) * parent2
        return child

    def mutate(self, individual):
        if random.random() < self.mutation_rate:
            return individual + random.gauss(0, 1)
        return individual

    def run(self):
        self.initialize_population()
        
        for generation in range(self.num_generations):
            new_population = []
            
            for _ in range(self.population_size):
                parent1, parent2 = self.select_parents()
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)
            
            self.population = new_population
            
            for individual in self.population:
                fitness = self.fitness(individual)
                if fitness < self.best_fitness:
                    self.best_fitness = fitness
                    self.best_individual = individual

        return self.best_individual, self.best_fitness, self.num_generations

if __name__ == '__main__':
    headers = ["Experiment", "Population Size", "Generations", "Mutation Rate", "Best x", "Best f(x)"]
    x = symbols('x')
    func = 2*x - ln(x)
    results = []

    experiments = [
        {'population_size': 10, 'num_generations': 2, 'mutation_rate': 0.1},
        {'population_size': 10, 'num_generations': 30, 'mutation_rate': 0.1},
        {'population_size': 40, 'num_generations': 10, 'mutation_rate': 0.1},
        {'population_size': 5, 'num_generations': 10, 'mutation_rate': 0.1},
        {'population_size': 10, 'num_generations': 10, 'mutation_rate': 0.5},
        {'population_size': 10, 'num_generations': 10, 'mutation_rate': 0.01},
    ]

    for idx, exp in enumerate(experiments):
        ga = GeneticAlgorithm(func, exp['population_size'], exp['num_generations'], exp['mutation_rate'])
        best_x, best_fx, generations = ga.run()
        print(best_x, best_fx)
        results.append([
            f"Exp {idx+1}",
            exp['population_size'],
            exp['num_generations'],
            exp['mutation_rate'],
            best_x,
            best_fx
        ])
        
    print(tabulate(results, headers=headers, tablefmt="grid"))