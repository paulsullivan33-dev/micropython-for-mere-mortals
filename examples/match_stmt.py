command = "water"
match command:
    case "water":
        print("pump on")
    case _:
        print("unknown")
