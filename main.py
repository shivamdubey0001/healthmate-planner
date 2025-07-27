# main.py - HealthMate Smart Daily Routine & Fitness Planner
# This is the main controller file that runs everything

import os
import sys
from datetime import datetime

# Import our custom modules
from user_input import get_user_info
from planner import create_routine
from utils import show_welcome, show_goodbye, clear_screen

def main():
    """
    Main function that controls the entire HealthMate application
    This function calls other modules in proper sequence
    """

    try:
        # Clear screen for fresh start
        clear_screen()

        # Show welcome message to user
        show_welcome()

        # Get user information (age, goal, time, equipment)
        print("🔍 Let's understand your needs first...")
        user_data = get_user_info()

        # Check if user wants to quit
        if user_data is None:
            print("\n👋 No worries! Come back anytime when you're ready.")
            return

        # Create personalized routine based on user input
        print("\n🎯 Creating your personalized routine...")
        print("⏳ Please wait a moment...")

        # Generate the routine
        routine = create_routine(user_data)

        # Display the routine to user
        print("\n" + "="*50)
        print("🎉 YOUR PERSONALIZED HEALTHMATE ROUTINE IS READY!")
        print("="*50)

        # Show the complete routine
        display_routine(routine, user_data)

        # Ask if user wants to save or modify
        handle_user_choice(routine, user_data)

        # Show goodbye message
        show_goodbye()

    except KeyboardInterrupt:
        # Handle when user presses Ctrl+C
        print("\n\n😊 Thanks for using HealthMate! Take care!")
        sys.exit(0)

    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"\n❌ Oops! Something went wrong: {str(e)}")
        print("🔧 Don't worry, this happens sometimes. Please try again!")

        # Ask user if they want to restart
        restart = input("\n🔄 Want to try again? (y/n): ").lower().strip()
        if restart == 'y' or restart == 'yes':
            main()  # Restart the application

def display_routine(routine, user_data):
    """
    Display the generated routine in a beautiful format
    Makes it easy to read and follow
    """

    print(f"\n👤 Hey {user_data['name']}! Here's your custom plan:")
    print(f"🎯 Goal: {user_data['goal']}")
    print(f"⏰ Daily Time: {user_data['time']} minutes")
    print("\n" + "-"*40)

    # Show morning routine
    if 'morning' in routine:
        print("\n🌅 MORNING ROUTINE:")
        for item in routine['morning']:
            print(f"   ✓ {item}")

    # Show workout routine
    if 'workout' in routine:
        print("\n💪 WORKOUT TIME:")
        for item in routine['workout']:
            print(f"   ✓ {item}")

    # Show meal suggestions
    if 'meals' in routine:
        print("\n🥗 MEAL SUGGESTIONS:")
        for item in routine['meals']:
            print(f"   ✓ {item}")

    # Show evening routine
    if 'evening' in routine:
        print("\n🌙 EVENING ROUTINE:")
        for item in routine['evening']:
            print(f"   ✓ {item}")

    # Show daily tip
    if 'tip' in routine:
        print(f"\n💡 TODAY'S TIP: {routine['tip']}")

def handle_user_choice(routine, user_data):
    """
    Handle what user wants to do after seeing their routine
    Options: save, modify, or just exit
    """

    print("\n" + "-"*40)
    print("🤔 What would you like to do now?")
    print("1. 💾 Save this routine")
    print("2. 🔄 Create a new routine")
    print("3. 👋 Exit")

    while True:
        try:
            choice = input("\n👉 Enter your choice (1/2/3): ").strip()

            if choice == '1':
                save_routine(routine, user_data)
                break
            elif choice == '2':
                print("\n🔄 Let's create a fresh routine for you!")
                main()  # Restart the process
                break
            elif choice == '3':
                print("\n✅ Perfect! Hope this routine helps you stay healthy!")
                break
            else:
                print("❌ Please enter 1, 2, or 3 only!")

        except Exception as e:
            print(f"❌ Invalid input. Please try again!")

def save_routine(routine, user_data):
    """
    Save the generated routine to a file for future reference
    Creates a simple text file with user's routine
    """

    try:
        # Create filename with current date and user name
        current_date = datetime.now().strftime("%Y%m%d")
        filename = f"routine_{user_data['name']}_{current_date}.txt"

        # Create routines folder if it doesn't exist
        if not os.path.exists("saved_routines"):
            os.makedirs("saved_routines")

        filepath = os.path.join("saved_routines", filename)

        # Write routine to file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write("🧠 HEALTHMATE - YOUR PERSONAL ROUTINE\n")
            file.write("="*50 + "\n\n")
            file.write(f"👤 Name: {user_data['name']}\n")
            file.write(f"🎯 Goal: {user_data['goal']}\n")
            file.write(f"⏰ Time Available: {user_data['time']} minutes\n")
            file.write(f"📅 Created On: {datetime.now().strftime('%d %B %Y')}\n\n")

            # Write each section
            sections = ['morning', 'workout', 'meals', 'evening']
            section_names = ['🌅 MORNING ROUTINE', '💪 WORKOUT TIME', '🥗 MEAL SUGGESTIONS', '🌙 EVENING ROUTINE']

            for section, section_name in zip(sections, section_names):
                if section in routine:
                    file.write(f"{section_name}:\n")
                    for item in routine[section]:
                        file.write(f"  ✓ {item}\n")
                    file.write("\n")

            if 'tip' in routine:
                file.write(f"💡 TODAY'S TIP: {routine['tip']}\n")

        print(f"\n✅ Routine saved successfully!")
        print(f"📁 File location: {filepath}")
        print("📝 You can open this file anytime to check your routine!")

    except Exception as e:
        print(f"❌ Couldn't save the routine: {str(e)}")
        print("🤷‍♂️ But don't worry, you can still follow the routine above!")

# This is the entry point of our application
# When someone runs this file, it will start here
if __name__ == "__main__":
    print("🚀 Starting HealthMate...")
    main()