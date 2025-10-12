"""
Snake Game - Main Launcher
Select which stage of the game to run for demonstration purposes.
"""

import stage1_snake_only
import stage2_snake_wrap
import stage3_with_food
import stage4_full_game


def main():
    """Main function to select and run a stage of the Snake game."""
    print("Snake Game - Stage Selector")
    print("===========================")
    print("1: Stage 1 - Static Snake")
    print("2: Stage 2 - Snake Movement (Wrapping)")
    print("3: Stage 3 - Add Food + Growth")
    print("4: Stage 4 - Full Game (Score + Collisions)")
    print("0: Exit")

    while True:
        try:
            choice = input("Enter stage number (0-4): ").strip()
            if choice == "1":
                print("Running Stage 1...")
                stage1_snake_only.run_stage1()
                break
            elif choice == "2":
                print("Running Stage 2...")
                stage2_snake_wrap.run_stage2()
                break
            elif choice == "3":
                print("Running Stage 3...")
                stage3_with_food.run_stage3()
                break
            elif choice == "4":
                print("Running Stage 4...")
                stage4_full_game.run_stage4()
                break
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter 0-4.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()