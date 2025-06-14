
print("⚓ Attention, Captain! You're entering the Bermuda Triangle zone...")

while True:
    choice = input("Where do you steer the ship? (1-North, 2-South, 3-Stay): ")

    if choice == "1":
        print("We sail homeward. But there's a storm on the horizon... ⚡")
        action = input("1 - Sail through the storm, 2 - Turn back, 3 - Stay put: ")

        if action == "1":
            print("This is very dangerous! We might not survive... ⚠️")
        elif action == "2":
            print("We may avoid disaster if we're fast enough... 🌫")
        elif action == "3":
            print("It's risky, but maybe there's a chance... ⏳")
        else:
            print("The storm is approaching fast!")

    elif choice == "2":
        print("You see a ghostly light in the distance... A way to salvation! 🧭")
        direction = input("1 - Sail to the lighthouse, 2 - Follow the stars, 3 - Trust your intuition: ")

        if direction == "1":
            print("Sailing toward the light... You reach a strange island, eerie sounds around... 🏝")
            print("You're on the island. The whispers grow louder... Ahead is a dark cave.")
            island_choice = input("1 - Enter the cave, 2 - Walk around it, 3 - Run back to the boat: ")

            if island_choice == "1":
                print("You step into the cave... Inside, a glowing symbol pulses from the deep... 🌀")
            elif island_choice == "2":
                print("You walk around and see strange footprints in the sand... Someone was just here... 👣")
            elif island_choice == "3":
                print("You run back... But the boat is gone! The waves have taken it... 🌊")
            else:
                print("You hesitate... The cave breathes darkness...")

        elif direction == "2":
            print("You follow the starlit path... Suddenly, everything goes dark and a storm begins! 🌩")
        elif direction == "3":
            print("Your intuition works. A magical compass rises from the sea... 🧭✨")
        else:
            print("You hesitate... The waves rise again, and the path disappears... 🌊")

    elif choice == "3":
        print("The ship starts slowly sinking... 🌊")

    else:
        print("Unknown command. The compass doesn't understand you... 🧭❓")

    # Final scene: wish
    final_choice = input("\nYou hear a voice in the silence... It asks: 'What is your true wish?' Type it here: ")

    if final_choice.lower() in ["to become a traveler in python code", "be a python code explorer", "to explore python"]:
        print("✨ The Soul of the Triangle accepts your wish... And the world begins to shift.")
        print("You're no longer just a player. You are a traveler in the code of Python.")
        print("Every line, every variable, every function — a path you're walking. 🚀")
        print("Your journey is just beginning... And it's real. ✨")
    else:
        print("...The Soul of the Triangle listens closely...")
        print("Your wish is accepted. It is now growing within the fabric of reality. Believe — it will find you. 🌱")
