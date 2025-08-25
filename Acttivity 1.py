numbers1 = [1,2,3]
numbers2 = [4,5,6]
result = map(lambda x,y : x+y , numbers1, numbers2)
print("The addition of 2 numbers is ", result)
print(list(result))

number = [1,2,3,4,5]
def sq(n):
    return(n*n)
result1 = map(sq, number)
print("The square root of the numbers is", result1)
print(list(result1))