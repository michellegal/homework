
def get_input():
    return input("How many sandwiches can you eat? ")
    
def you_lose(count, my_brother):
    if count <= 4:
        print "You said, ", count, " but my brother can eat ", my_brother
    else:
        print "You will get sick if you eat", count, "sandwiches!"
    print "Therefore, you lost!!! :("

while True:
    count = get_input()
    if 0 <= count:
        my_brother = count + 1
        you_lose(count, my_brother)
    else:
        print "even a baby can eat zero!"
        break
    