anime_store = []

def adding_anime(**anime):
   anime_store.append(anime)
   return "anime is added to the store"

def run():
    while True:
        option = input("1. add anime. \n2. view anime. \n3. exit program: ")

        if option == "1":
              name = input("what is the name of the anime?: ")
              year = input("what year was the anime created?: ")
              author = input("who created the anime?: ")

              result = adding_anime(name=name, year=year, author=author)
              print(result)
              print(anime_store)
                
        elif option == "2":
                print(2)
        elif option == "3":
                break
        else:
                print(f"{"--" * 22}\nNot an option. try again\n{"--" * 22}")


run()