n = int(input("Введите количество школьников:"))
k = int(input("Введите количество яблок:"))


apples_students =  k // n
remains = k % n

print("Каждому школьнику достанется:", apples_students)
print("В корзине останется:", remains)
