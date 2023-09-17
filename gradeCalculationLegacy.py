eq = "======================================================"
answer = "y"


def gradeComputing(lst1, lst2):
    sList = []
    for i in range(len(lst1)):
        weight = float(lst1[i] / 100)
        grade = float(lst2[i] / 100)
        score = round(weight * grade, 4)
        sList.append(score)
    sumScore = sum(sList)
    return sumScore * 100


def finPrint(lst1, lst2, lst3, grade):
    print("=-=-=-=-=-=-=-=-=-=-=-=  SUMMARY  =-=-=-=-=-=-=-=-=-=-=-=")

    for entry in range(len(lst1)):
        print(f"=-=-=-=-=  CATEGORY {entry + 1}  =-=-=-=-=")
        print(f"=-=  Name of Category                       {lst1[entry]}")
        print(f"=-=  Category Weight                        {lst2[entry]} %")
        print(f"=-=  Current Grade                          {lst3[entry]} %")
        x = (((lst2[entry] / 100) * (lst3[entry] / 100)) * 100)
        x = round(x, 2)
        print(f"=-=  Contribution to Final Grade            {x} %")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(f"=-=  Weighted Grade in Course               {grade} %")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")


def varChange(lst1, lst2, lst3):
    print("Which category grade would you like to change?")
    for i in range(len(lst1)):
        print(f"[{i + 1}]  {lst1[i]}")
    index = int(input("\nYour answer:  "))
    index -= 1
    lst3[index] = float(input(f"New grade for {lst1[index]}:  "))
    print()
    fGrade = gradeComputing(lst2, lst3)
    fGrade = round(fGrade, 2)
    finPrint(lst1, lst2, lst3, fGrade)


while answer == "y":
    categories = int(input("Number of categories in the course:  "))

    nList = []
    wList = []
    gList = []

    for i in range(categories):
        name = input(f"\n{eq}\nName of category {i + 1}:  ")
        nList.append(name)
        weight = float(input(f"{eq}\nWeight of category {name} (%):  "))
        wList.append(weight)
        cGr = float(input(f"{eq}\nCurrent grade in category {name} (%):  "))
        gList.append(cGr)
        print(f"{eq}\n")

    if sum(wList) == 100:
        fGrade = gradeComputing(wList, gList)
        fGrade = round(fGrade, 2)
        finPrint(nList, wList, gList, fGrade)

    else:
        print(f"\n{eq}\nERROR: Total weights do not add up to 100%, but {sum(wList)}\n{eq}")
    answer2 = input("\nWould you like to change a grade variable? (y/n):  ")
    while answer2 == "y":
        print(eq)
        varChange(nList, wList, gList)
        answer2 = input("\nWould you like to change another grade variable? (y/n):  ")
    answer = input("\n\nWould you like to run the test again? (y/n):  ")
