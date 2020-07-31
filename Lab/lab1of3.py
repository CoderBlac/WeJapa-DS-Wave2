# Use this playground to experiment with list methods, using Test Run

#using append() method
days = ['Sunday', 'Wednesday', 'Thursday', 'Tuesday', 'Friday', 'Monday', 'Saturday']
days.append('Holiday')
print(days)

#using sorted() method
days = [1, 2, 8, 5, 9, 11, 7, 10, 4, 10, 3, 6]
sort = sorted(days)
print(sort)

#using the reverse() method
days = ['Sunday', 'Wednesday', 'Thursday', 'Tuesday', 'Friday', 'Monday', 'Saturday']
days.reverse()
print(days)

#using the pop() method
days = ['Sunday', 'Wednesday', 'Thursday', 'Tuesday', 'Friday', 'Monday', 'Saturday']
days.pop(5)
print(days)


#using the clear() method
days = ['Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday', 'Sunday']
days.clear()
print(days)


#using the count() method
days = ['Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday', 'Sunday', 'Saturday']
day = days.count("Tuesday")
print(day)

#using the remove() method
days = ['Sunday', 'Wednesday', 'Thursday', 'Tuesday', 'Friday', 'Monday', 'Saturday']
days.remove("Friday")
print(days)

#using the max()
days = [1, 2, 3, 5, 9, 6, 7, 10]
max = max(days)
print(max)

#using the min()
days = [1, 2, 3, 5, 9, 6, 7, 10]
min = min(days)
print(min)

#using sorted() method
days = [1, 2, 3, 5, 9, 6, 7, 10, 4, 8]
sort = sorted(days)
print(sort)


#using the .len()
days = [1, 2, 3, 5, 9, 6, 7, 10, 4, 8]
length = len(days)
print(length)

#using the .join method()
name = "~~".join(["John", "Junior"])
print(name)