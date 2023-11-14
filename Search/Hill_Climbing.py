import random

def objective_function(solution):
    return -1 * (solution ** 2)

def hill_climbing(max_iterations, initial_solution, step_size):
    current_solution = initial_solution
    current_value = objective_function(current_solution)

    for _ in range(max_iterations):
        # rastgele bir komşu çözümüne bakılır
        neighbor_solution = current_solution + random.uniform(-step_size, step_size)
        neighbor_value = objective_function(neighbor_solution)

        if neighbor_value > current_value:
            current_solution = neighbor_solution
            current_value = neighbor_value

    return current_solution, current_value

# Başlangıç çözümü ve parametreler
initial_solution = random.uniform(-10, 10)
max_iterations = 1000
step_size = 0.1

result_solution, result_value = hill_climbing(max_iterations, initial_solution, step_size)

print(f"Başlangıç çözümü: {initial_solution}")
print(f"Sonuç çözümü: {result_solution}")
print(f"Sonuç değeri: {result_value}")
