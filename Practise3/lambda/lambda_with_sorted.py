students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

# sorted(iterable, key=...)
# key это по какому правилу мы сортируем, выше по возрасту


