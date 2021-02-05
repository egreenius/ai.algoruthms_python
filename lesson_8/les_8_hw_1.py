"""
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""

# n = int(input('Введите количество друзей на встрече:'))
n = 10
# построим матрицу смежности.
graph = []  # создаем пустой список

for i in range(n):  # организуем цикл рукопожатий для каждого участника, получим матрицу смежности
    graph.append([])
    for j in range(n):  # организуем цикл рукопожатий с каждым участником, кроме того кто жмет руку
        if i != j:
            graph[i].append(1)
        else:
            graph[i].append(0)
print('Матрица смежности, где вершины - это друзья, ребра - рукопожатия:')
print(*graph, sep='\n')

# исключим из матрицы смежности повторные рукопожатия
h_s = 0  # здесь будем накапливать количество рукопожатий
for i in range(n):
    for j in range(n):
        if graph[i][j] == graph[j][i]:
            graph[j][i] = 0
        h_s += graph[i][j]

print()
print('Матрица рукопожатий, с исключением повторных рукопожатий')
print(*graph, sep='\n')
print(f'Количество рукопожатий: {h_s}')
assert h_s == (n-1) * n/2
print('Количество рукопожатий посчитано верно')


# построение матрицы рукопожатий за один проход
graph_1 = []  # создаем пустой список
h_s = 0  # здесь будем накапливать количество рукопожатий

for i in range(n):  # организуем цикл рукопожатий для каждого участника
    graph_1.append([])
    for j in range(n):  # организуем цикл рукопожатий с каждым участником, кроме того кто жмет руку и исключим
        # предыдущие рукопожатия
        if i != j and j > i:
            graph_1[i].append(1)
        else:
            graph_1[i].append(0)
        h_s += graph_1[i][j]

print()
print('Матрица рукопожатий за один проход по циклам: ')
print(*graph_1, sep='\n')
print(f'Количество рукопожатий: {h_s}')
assert h_s == (n-1) * n/2
print('Количество рукопожатий посчитано верно')

# Крутое решение!
# from functools import reduce
#
# n = int(input('Сколько встретилось друзей: '))
# graph = [[int(i > j) for i in range(n)] for j in range(n)]
# count = reduce(lambda acc, x: acc + sum(x), graph, 0)
# print(graph)
# print(f'Количество рукопожатий {count}')
