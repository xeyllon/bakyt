from collections import deque

# СТРУКТУРЫ ДАННЫХ
# Стек - LIFO последний зашел, первый вышел
# Очень - FIFO  первый зашел, первый ушел

# d = deque()
# d.append(1)
# d.append(2)
# d.appendleft(0)
# d.appendleft(-1)
# print(d)


# print(d.pop())
# print(d.pop())
# print(d)

# d.extend([8, 8, 8])
# d.extendleft([1, 1, 1])
# print(d)

# d.clear()
# print(d)

# stack = deque()

# stack.append(1)
# stack.append(2)
# stack.append(3)
# print(f"Стек после добавления элементов - {stack}")

# print(f"Удаляем элемент {stack.pop()}")
# print(f"Удаляем элемент {stack.pop()}")

# print(f"Стек после добавления элементов - {stack}")



# задача

def validate(s):
    # Создаем стек на основе deque() для эффективности работы
    stack = deque()
    # Создаем словарь ключь-значение с скобками для отслеживания правильности
    br = {")": "(", "]": "[", "}": "{"}

    # keys = ключ  values = значение

    for char in s:  # перебираем каждую скобку из "s"
       
        if char in br.values(): # проверяем есть ли значение в ключ-словаре
            stack.append(char)
        elif char in br.keys():# если скобка является закрывающей
            # если стак пустой или скобка не 
            # правильная по отношению к последней в стеке
            if not stack or stack.pop() != br[char]:  
                # возвращаем false
                return False
        
    return not stack
print(validate("({[]})"))
print(validate("({["))
