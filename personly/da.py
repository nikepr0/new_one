from collections import deque

# Создаем очередь
queue = deque(["Клиент1", "Клиент2", "Клиент3"])

# Добавление элементов (enqueue)
queue.append("Клиент4")
print(f"Очередь: {list(queue)}")

# Извлечение элементов (dequeue)
first = queue.popleft()
print(f"Обслужили: {first}")
print(f"Очередь: {list(queue)}")

# Просмотр первого элемента (peek)
print(f"Следующий: {queue[0]}")
