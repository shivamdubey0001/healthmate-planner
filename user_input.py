# user_input.py - Collect user information safely and smartly
# This module handles all user input with proper validation and error handling

import re
import sys
from utils import print_with_delay, get_random_encouragement

def get_user_info():
    """
    Main function to collect all user information
    Returns a dictionary with user data or None if user wants to quit
    """

    print("\n🎯 Let's get to know you better!")
    print("💡 Type 'quit' anytime to exit")
    print("-" * 40)

    try:
        # Initialize user data dictionary
        user_data = {}

        # Get user's name
        user_data['name'] = get_user_name()
        if user_data['name'] is None:
            return None

        # Get user's age
        user_data['age'] = get_user_age()
        if user_data['age'] is None:
            return None

        # Get user's fitness goal
        user_data['goal'] = get_user_goal()
        if user_data['goal'] is None:
            return None

        # Get available daily time
        user_data['time'] = get_available_time()
        if user_data['time'] is None:
            return None

        # Get available equipment
        user_data['equipment'] = get_available_equipment()
        if user_data['equipment'] is None:
            return None

        # Get dietary preferences
        user_data['diet'] = get_dietary_preferences()
        if user_data['diet'] is None:
            return None

        # Get current fitness level
        user_data['fitness_level'] = get_fitness_level()
        if user_data['fitness_level'] is None:
            return None

        # Show summary and confirm
        if not confirm_user_data(user_data):
            print("\n🔄 No problem! Let's start fresh.")
            return get_user_info()  # Restart the process

        # Add some encouraging message
        print(f"\n🎉 Great {user_data['name']}! " + get_random_encouragement())

        return user_data

    except KeyboardInterrupt:
        print("\n\n👋 Thanks for trying HealthMate! Come back anytime.")
        return None
    except Exception as e:
        print(f"\n❌ Something went wrong while collecting info: {str(e)}")
        print("🔄 Let's try again from the beginning...")
        return get_user_info()

def get_user_name():
    """
    Get user's name with proper validation
    Ensures name contains only letters and spaces
    """

    while True:
        try:
            print("\n👤 What should I call you?")
            name = input("📝 Your name: ").strip()

            # Check if user wants to quit
            if name.lower() in ['quit', 'exit', 'q']:
                return None

            # Check if name is empty
            if not name:
                print("❌ Please enter your name!")
                continue

            # Check if name is too short
            if len(name) < 2:
                print("❌ Name should be at least 2 characters long!")
                continue

            # Check if name is too long
            if len(name) > 30:
                print("❌ Name is too long! Please keep it under 30 characters.")
                continue

            # Check if name contains only valid characters
            if not re.match("^[a-zA-Z\s]+$", name):
                print("❌ Name should contain only letters and spaces!")
                continue

            # Clean up the name (proper case)
            name = ' '.join(word.capitalize() for word in name.split())

            print(f"✅ Nice to meet you, {name}!")
            return name

        except Exception as e:
            print("❌ Invalid input. Please try again!")

def get_user_age():
    """
    Get user's age with proper validation
    Age should be between 10 and 100
    """

    while True:
        try:
            print(f"\n🎂 How old are you?")
            age_input = input("📝 Your age: ").strip()

            # Check if user wants to quit
            if age_input.lower() in ['quit', 'exit', 'q']:
                return None

            # Check if input is empty
            if not age_input:
                print("❌ Please enter your age!")
                continue

            # Convert to integer
            age = int(age_input)

            # Validate age range
            if age < 10:
                print("❌ You're too young for this app! Ask your parents for help.")
                continue
            elif age > 100:
                print("❌ Age seems too high! Please enter a valid age.")
                continue
            elif age < 18:
                print("⚠️  You're under 18. We'll create a safe routine for you!")

            print(f"✅ Got it! You're {age} years old.")
            return age

        except ValueError:
            print("❌ Please enter a valid number for age!")
        except Exception as e:
            print("❌ Invalid input. Please try again!")

def get_user_goal():
    """
    Get user's fitness goal from predefined options
    Provides multiple choices with clear descriptions
    """

    goals = {
        '1': {'name': 'weight_loss', 'display': 'Weight Loss', 'desc': 'Lose weight and get fit'},
        '2': {'name': 'weight_gain', 'display': 'Weight Gain', 'desc': 'Gain healthy weight and muscle'},
        '3': {'name': 'muscle_building', 'display': 'Muscle Building', 'desc': 'Build strength and muscle mass'},
        '4': {'name': 'general_fitness', 'display': 'General Fitness', 'desc': 'Stay healthy and active'},
        '5': {'name': 'endurance', 'display': 'Endurance', 'desc': 'Improve stamina and cardio health'},
        '6': {'name': 'flexibility', 'display': 'Flexibility', 'desc': 'Increase flexibility and mobility'}
    }

    while True:
        try:
            print(f"\n🎯 What's your main fitness goal?")
            print("Choose one option:")

            for key, goal in goals.items():
                print(f"  {key}. 💪 {goal['display']} - {goal['desc']}")

            choice = input("\n📝 Enter your choice (1-6): ").strip()

            # Check if user wants to quit
            if choice.lower() in ['quit', 'exit', 'q']:
                return None

            # Validate choice
            if choice in goals:
                selected_goal = goals[choice]
                print(f"✅ Great choice! Goal: {selected_goal['display']}")
                return selected_goal['name']
            else:
                print("❌ Please choose a number between 1 and 6!")

        except Exception as e:
            print("❌ Invalid input. Please try again!")

def get_available_time():
    """
    Get user's available daily time for fitness
    Validates time is reasonable (5-180 minutes)
    """

    while True:
        try:
            print(f"\n⏰ How much time can you spend daily on fitness?")
            print("💡 Include workout + meal prep time")
            time_input = input("📝 Time in minutes (e.g., 30): ").strip()

            # Check if user wants to quit
            if time_input.lower() in ['quit', 'exit', 'q']:
                return None

            # Check if input is empty
            if not time_input:
                print("❌ Please enter the time!")
                continue

            # Convert to integer
            time_minutes = int(time_input)

            # Validate time range
            if time_minutes < 5:
                print("❌ Too little time! At least 5 minutes needed.")
                continue
            elif time_minutes > 180:
                print("❌ That's too much time! Maximum 180 minutes (3 hours).")
                continue

            # Give feedback based on time
            if time_minutes < 15:
                print("⚠️  Short time! We'll focus on quick exercises.")
            elif time_minutes > 60:
                print("🔥 Great! You have good time for a complete routine.")

            print(f"✅ Perfect! {time_minutes} minutes daily it is.")
            return time_minutes

        except ValueError:
            print("❌ Please enter a valid number for time!")
        except Exception as e:
            print("❌ Invalid input. Please try again!")

def get_available_equipment():
    """
    Get user's available equipment from multiple choices
    Users can select multiple equipment items
    """

    equipment_options = {
        '1': 'dumbbells',
        '2': 'resistance_bands',
        '3': 'pull_up_bar',
        '4': 'yoga_mat',
        '5': 'jump_rope',
        '6': 'kettlebell',
        '7': 'treadmill',
        '8': 'bicycle',
        '9': 'none'  # No equipment - bodyweight only
    }

    while True:
        try:
            print(f"\n🏋️ What equipment do you have access to?")
            print("💡 You can select multiple options (separate by commas)")
            print("Available equipment:")

            for key, equipment in equipment_options.items():
                display_name = equipment.replace('_', ' ').title()
                if equipment == 'none':
                    display_name = "No Equipment (Bodyweight Only)"
                print(f"  {key}. {display_name}")

            choices = input("\n📝 Enter your choices (e.g., 1,4,5): ").strip()

            # Check if user wants to quit
            if choices.lower() in ['quit', 'exit', 'q']:
                return None

            # Check if input is empty
            if not choices:
                print("❌ Please select at least one option!")
                continue

            # Parse multiple choices
            selected_equipment = []
            choice_list = [choice.strip() for choice in choices.split(',')]

            # Validate each choice
            valid_choices = True
            for choice in choice_list:
                if choice in equipment_options:
                    equipment_name = equipment_options[choice]
                    if equipment_name not in selected_equipment:
                        selected_equipment.append(equipment_name)
                else:
                    print(f"❌ Invalid choice: {choice}")
                    valid_choices = False
                    break

            if not valid_choices:
                continue

            # Check if 'none' is selected with other equipment
            if 'none' in selected_equipment and len(selected_equipment) > 1:
                print("❌ If you select 'No Equipment', don't select other items!")
                continue

            # Display selected equipment
            if 'none' in selected_equipment:
                print("✅ Bodyweight exercises it is! No equipment needed.")
            else:
                equipment_display = [eq.replace('_', ' ').title() for eq in selected_equipment]
                print(f"✅ Great! Equipment: {', '.join(equipment_display)}")

            return selected_equipment

        except Exception as e:
            print("❌ Invalid input. Please try again!")

def get_dietary_preferences():
    """
    Get user's dietary preferences and restrictions
    Helps in meal planning
    """

    diet_options = {
        '1': {'name': 'vegetarian', 'display': 'Vegetarian', 'desc': 'No meat, but dairy is okay'},
        '2': {'name': 'vegan', 'display': 'Vegan', 'desc': 'No animal products at all'},
        '3': {'name': 'non_vegetarian', 'display': 'Non-Vegetarian', 'desc': 'Everything including meat'},
        '4': {'name': 'jain', 'display': 'Jain Food', 'desc': 'No root vegetables, strict vegetarian'},
        '5': {'name': 'keto', 'display': 'Keto Diet', 'desc': 'Low carb, high fat diet'},
        '6': {'name': 'no_preference', 'display': 'No Specific Preference', 'desc': 'I eat everything'}
    }

    while True:
        try:
            print(f"\n🥗 What are your dietary preferences?")
            print("Choose your eating style:")

            for key, diet in diet_options.items():
                print(f"  {key}. {diet['display']} - {diet['desc']}")

            choice = input("\n📝 Enter your choice (1-6): ").strip()

            # Check if user wants to quit
            if choice.lower() in ['quit', 'exit', 'q']:
                return None

            # Validate choice
            if choice in diet_options:
                selected_diet = diet_options[choice]
                print(f"✅ Got it! Diet preference: {selected_diet['display']}")
                return selected_diet['name']
            else:
                print("❌ Please choose a number between 1 and 6!")

        except Exception as e:
            print("❌ Invalid input. Please try again!")

def get_fitness_level():
    """
    Get user's current fitness level
    Helps in creating appropriate difficulty routines
    """

    fitness_levels = {
        '1': {'name': 'beginner', 'display': 'Beginner', 'desc': 'Just starting out or returning after long break'},
        '2': {'name': 'intermediate', 'display': 'Intermediate', 'desc': 'Exercise regularly, comfortable with basic moves'},
        '3': {'name': 'advanced', 'display': 'Advanced', 'desc': 'Very active, can handle intense workouts'}
    }

    while True:
        try:
            print(f"\n💪 What's your current fitness level?")
            print("Be honest - this helps create the right routine for you:")

            for key, level in fitness_levels.items():
                print(f"  {key}. {level['display']} - {level['desc']}")

            choice = input("\n📝 Enter your choice (1-3): ").strip()

            # Check if user wants to quit
            if choice.lower() in ['quit', 'exit', 'q']:
                return None

            # Validate choice
            if choice in fitness_levels:
                selected_level = fitness_levels[choice]
                print(f"✅ Perfect! Fitness level: {selected_level['display']}")
                return selected_level['name']
            else:
                print("❌ Please choose a number between 1 and 3!")

        except Exception as e:
            print("❌ Invalid input. Please try again!")

def confirm_user_data(user_data):
    """
    Show user their entered data and ask for confirmation
    Allows user to review and modify if needed
    """

    try:
        print("\n" + "="*50)
        print("📋 PLEASE REVIEW YOUR INFORMATION")
        print("="*50)

        # Display all user data in a nice format
        print(f"👤 Name: {user_data['name']}")
        print(f"🎂 Age: {user_data['age']} years")
        print(f"🎯 Goal: {user_data['goal'].replace('_', ' ').title()}")
        print(f"⏰ Daily Time: {user_data['time']} minutes")

        # Format equipment display
        if 'none' in user_data['equipment']:
            equipment_display = "No Equipment (Bodyweight Only)"
        else:
            equipment_display = ', '.join([eq.replace('_', ' ').title() for eq in user_data['equipment']])
        print(f"🏋️ Equipment: {equipment_display}")

        print(f"🥗 Diet: {user_data['diet'].replace('_', ' ').title()}")
        print(f"💪 Fitness Level: {user_data['fitness_level'].title()}")

        print("\n" + "-"*40)

        while True:
            confirm = input("✅ Is this information correct? (yes/no): ").strip().lower()

            if confirm in ['yes', 'y', 'correct', 'ok', 'right']:
                return True
            elif confirm in ['no', 'n', 'wrong', 'incorrect']:
                return False
            elif confirm in ['quit', 'exit', 'q']:
                return None
            else:
                print("❌ Please answer with 'yes' or 'no'!")

    except Exception as e:
        print("❌ Error while confirming data. Assuming it's correct...")
        return True

# Helper function to validate if input is empty after stripping
def is_empty_input(user_input):
    """
    Check if user input is empty or contains only whitespace
    """
    return not user_input or not user_input.strip()

# Helper function to sanitize user input
def sanitize_input(user_input, max_length=100):
    """
    Clean and sanitize user input
    Remove dangerous characters and limit length
    """
    if not user_input:
        return ""

    # Remove leading/trailing whitespace
    cleaned = user_input.strip()

    # Limit length
    if len(cleaned) > max_length:
        cleaned = cleaned[:max_length]

    return cleaned