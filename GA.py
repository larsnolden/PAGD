import numpy as np
import pygad as pg
import os.path
import pandas as pd
from datetime import datetime

SAVEPOINT_FILE_NAME = "ga_savepoint"

solutions = pd.DataFrame(columns=["fitness", "solution", "computed_on", "generation"])

from comsolClient import runSimulation
from generateCurve import generateCurve


def fitnessFunction(ga_instance, solution, solution_idx):
    global solutions
    if solution.max() == 0:
        # return low fitness if solution is empty (all zeros)
        return 0

    # fake fitness for testing
    fitness = np.array(solution).sum()

    # image_representation = solution.reshape(11, 11)
    # print(image_representation)
    # # genetic_representation = np.random.choice([0, 1], size=(11, 11))

    # contourFilePath = generateCurve(image_representation, padding=100)
    # print(f"generated contour file at {contourFilePath}")
    # # run simulation
    # fitness = runSimulation(contourFilePath)

    # record all solutions
    now = datetime.now()
    date_time = now.strftime("%d.%m.%Y, %H:%M:%S")
    new_row = pd.DataFrame(
        [[fitness, str(solution), date_time, ga_instance.generations_completed]],
        columns=solutions.columns,
    )
    solutions = pd.concat([solutions, new_row], ignore_index=True)
    solutions.to_csv("./solutions.csv")
    return fitness


def on_gen(ga_instance):
    print("Generation : ", ga_instance.generations_completed)
    print("Fitness of the best solution :", ga_instance.best_solution()[1])
    ga_instance.save(SAVEPOINT_FILE_NAME)  # save progress on each generation


dim = 11 * 11

ga_instance = pg.GA(
    num_generations=400,
    num_parents_mating=15,  # num parents from each generation choosen that produce all of the new generation offspring
    fitness_func=fitnessFunction,
    sol_per_pop=40,
    num_genes=dim,
    init_range_low=0,
    init_range_high=2,  # exclusive
    parent_selection_type="rank",  # rank: select parents based on their fitness ranking
    # keep_parents=-1,  # keep all parents
    keep_elitism=4,  # keep the best 4 parents
    gene_type=int,
    crossover_type="uniform",  # uniform: choose either parent bit with the same probability
    # mutation_type=None,
    mutation_percent_genes=4,
    on_generation=on_gen,
    save_best_solutions=True,  # best solution after each generation is saved into an attribute named best_solution
    save_solutions=True,  # all solutions after each generation are saved into an attribute named solutions
)


def main():
    global ga_instance
    # check if there is a savepoint
    savepoint_file_exists = os.path.isfile(f"{SAVEPOINT_FILE_NAME}.pkl")
    if savepoint_file_exists:
        # overwrite the default ga_instance with the saved one
        print("Savepoint found, resuming from savepoint")
        ga_instance = pg.load(SAVEPOINT_FILE_NAME)
    else:
        print("No savepoint found, starting from scratch")

    ga_instance.run()
    ga_instance.plot_fitness()


main()
