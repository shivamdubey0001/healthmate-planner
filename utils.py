# utils.py - Utility functions for HealthMate
# This file contains helper functions for colors, welcome screen, clearing screen, etc.

import os
import platform
import time

# Simple function to clear the screen based on operating system
def clear_screen():
    """
    Clears the terminal screen for better readability.
    Works on Windows, Mac, Linux, and even Replit.
    """
    try:
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    except Exception:
        print("\n" * 5)  # Fallback: just add blank lines


# Print welcome message with some decoration and delay for friendly experience
def show_welcome():
    """
    Displays the welcome message with a soft animation feel.
    Sets a warm and positive tone for the user.
    """
    print("\n🧠 Welcome to HealthMate – Your Personal Daily Routine Assistant!")
    print("=" * 60)
    time.sleep(1)
    print("💬 I'm here to help you stay fit, focused and energetic.")
    time.sleep(1)
    print("🎯 Let's create a smart daily plan that actually works for YOU.\n")
    time.sleep(1)


# Print goodbye message when user exits
def show_goodbye():
    """
    Displays a friendly goodbye message at the end.
    Leaves the user with positive energy.
    """
    print("\n" + "-" * 50)
    print("👋 Thank you for using HealthMate!")
    print("💖 Stay strong. Stay consistent. Stay YOU.")
    print("📅 Come back tomorrow for a fresh new routine!\n")
    time.sleep(1)


# Print message with delay for better user experience
def print_with_delay(message, delay=0.5):
    """
    Print a message with a delay for better readability and user experience.
    """
    print(message)
    time.sleep(delay)


# Get random encouragement message for users
def get_random_encouragement():
    """
    Returns a random encouraging message to motivate users.
    """
    encouragements = [
        "You're doing great! Let's build healthy habits together! 💪",
        "Every small step counts towards a healthier you! 🌟",
        "Your commitment to health is inspiring! Keep it up! 🚀",
        "Ready to transform your daily routine? Let's go! 🔥",
        "Health is wealth, and you're investing wisely! 💎",
        "Your future self will thank you for this! 🙏",
        "Building a better you, one day at a time! ⭐",
        "Consistency is key, and you've got this! 🗝️"
    ]
    
    import random
    return random.choice(encouragements)
