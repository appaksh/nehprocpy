for _ in range(int(input())):
    myReplacements = input()
    while ' && ' in myReplacements or ' || ' in myReplacements:
        myReplacements = myReplacements.replace(" && ", " and ").replace(" || ", " or ")
    print(myReplacements)
