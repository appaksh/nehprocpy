# def waterGod(functionToBeDecorated):
#     def poseidon():
#         print("I am your destruction!!!")
#         print("FOR I AM POSEIDON THE GOD OF THE SEAS!!!")
#         functionToBeDecorated()
#
#     return poseidon
#
#
# @waterGod
# def zeus():
#     print("I AM ZEUS THE GOD OF THUNDER!!!")
#
#
# zeus()

def question(functionToBeDecorated):
    print("What is 1+1")
    def bigBrainz():
        print("Answer : 11")
        functionToBeDecorated()

    return bigBrainz


@question
def smartKidWinkWink():
    print("Answer : 2")


smartKidWinkWink()
