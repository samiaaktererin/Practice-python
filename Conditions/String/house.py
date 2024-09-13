name = input("What's your name? ")

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# # elif name == "Hermione":
# #     print("Gryffindor")
# # elif name == "Ron":
# #     print("Gryffindor")
# elif name == "Draco":
#     print("Stytherin")
# else:
#     print("Who?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    # case "Hermione":
    #     print("Gryffindor")
    # case "Ron":
    #     print("Gryffindor")
    case"Draco":
        print("Stytherin")
    case _:
        print("Who?")
