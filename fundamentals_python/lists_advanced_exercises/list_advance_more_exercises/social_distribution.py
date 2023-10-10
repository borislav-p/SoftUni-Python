population = list(map(int, input().split(", ")))
min_wealth = int(input())
if sum(population) < len(population) * min_wealth:
    print(f"No equal distribution possible")
else:
    for el in population:
        if el < min_wealth:
            diff = min_wealth - el
            population[population.index(min(population))] += diff
            population[population.index(max(population))] -= diff
        
    print(population)
