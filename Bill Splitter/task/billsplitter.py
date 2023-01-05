import random
result = {}
names = []
friends = 0
#friends1 = friends

def inp1():
    while True:
        friends = int(input("Enter the number of friends joining (including you):"))
        if friends <= 0:
            print()
            print("No one is joining for the party")
            break
        else:
            friends1 = friends
            print()
            print("Enter the name of every friend (including you), each on a new line:")
            while friends1 != 0:
                names.append(input())
                friends1 -= 1
            inp2(friends)
            break


def inp2(friends):
    print()
    result_bill = int(input("Enter the total bill value:"))
    for i in names:
        result[i] = round((result_bill)/friends, 2)
    #print(result)
    fun3(names, result_bill, friends)


def fun3(name, res_bill, friends):
    print()
    lucky = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:")
    if lucky == "Yes":
       lucky_person = random.choice(name)
       name.remove(lucky_person)
       for i in names:
           result[i] = int(res_bill / (friends - 1))
           result.update({lucky_person: 0})
       print()
       print(f"{lucky_person} is the lucky one!")
    else:
        print()
        print("No one is going to be lucky")
    print()
    print(result)

inp1()
