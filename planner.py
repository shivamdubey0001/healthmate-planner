# planner.py - Smart routine generator based on user preferences
# This module creates personalized routines using user data

import random
import json
import os
from datetime import datetime

def create_routine(user_data):
    """
    Main function to create personalized routine based on user data
    Returns a complete routine dictionary with all sections
    """

    try:
        # Initialize routine structure
        routine = {
            'morning': [],
            'workout': [],
            'meals': [],
            'evening': [],
            'tip': ''
        }

        # Generate each section based on user data
        routine['morning'] = generate_morning_routine(user_data)
        routine['workout'] = generate_workout_routine(user_data)
        routine['meals'] = generate_meal_plan(user_data)
        routine['evening'] = generate_evening_routine(user_data)
        routine['tip'] = get_daily_tip(user_data)

        # Add routine metadata
        routine['created_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        routine['user_goal'] = user_data['goal']
        routine['total_time'] = user_data['time']

        return routine

    except Exception as e:
        print(f"❌ Error creating routine: {str(e)}")
        # Return a basic fallback routine
        return create_fallback_routine(user_data)

def generate_morning_routine(user_data):
    """
    Generate morning routine based on user's available time and fitness level
    Focus on preparing body and mind for the day
    """

    morning_activities = []
    available_time = user_data['time']
    fitness_level = user_data['fitness_level']
    age = user_data['age']

    try:
        # Basic morning essentials for everyone
        morning_activities.append("🌅 Wake up 15 minutes earlier than usual")
        morning_activities.append("💧 Drink 1-2 glasses of warm water")

        # Add activities based on available time
        if available_time >= 10:
            if fitness_level == 'beginner':
                morning_activities.append("🧘‍♂️ 5 minutes light stretching or yoga")
                morning_activities.append("🚶‍♂️ 3 minutes walking around house/room")
            elif fitness_level == 'intermediate':
                morning_activities.append("🧘‍♂️ 7 minutes dynamic stretching")
                morning_activities.append("🤸‍♂️ 5 jumping jacks + 5 arm circles")
            else:  # advanced
                morning_activities.append("🧘‍♂️ 10 minutes yoga or mobility work")
                morning_activities.append("🏃‍♂️ 5 minutes light cardio warm-up")

        if available_time >= 20:
            morning_activities.append("📱 Check your daily goals (2 minutes)")
            if age < 30:
                morning_activities.append("🎵 Listen to energizing music while getting ready")
            else:
                morning_activities.append("📖 Read something positive for 3 minutes")

        if available_time >= 30:
            morning_activities.append("🌤️ Spend 2 minutes in sunlight (if possible)")
            morning_activities.append("📝 Write down 3 things you're grateful for")

        # Special additions based on goal
        if user_data['goal'] == 'weight_loss':
            morning_activities.append("⚖️ Weigh yourself (same time daily)")
        elif user_data['goal'] == 'muscle_building':
            morning_activities.append("💪 Do 10 bodyweight squats to activate muscles")
        elif user_data['goal'] == 'flexibility':
            morning_activities.append("🤸‍♀️ Hold a 30-second gentle stretch")

        return morning_activities

    except Exception as e:
        # Fallback morning routine
        return [
            "🌅 Wake up and drink water",
            "🧘‍♂️ 5 minutes light stretching",
            "💭 Take 3 deep breaths and set daily intention"
        ]

def generate_workout_routine(user_data):
    """
    Generate workout routine based on equipment, time, goal, and fitness level
    Creates balanced and progressive workouts
    """

    workout_plan = []
    goal = user_data['goal']
    time = user_data['time']
    equipment = user_data['equipment']
    fitness_level = user_data['fitness_level']
    age = user_data['age']

    try:
        # Calculate workout time (60% of total available time)
        workout_time = max(10, int(time * 0.6))

        # Warm-up (always included)
        workout_plan.append("🔥 Warm-up: 3 minutes light movement")

        # Main workout based on goal and equipment
        if goal == 'weight_loss':
            workout_plan.extend(create_weight_loss_workout(equipment, workout_time, fitness_level, age))
        elif goal == 'weight_gain' or goal == 'muscle_building':
            workout_plan.extend(create_muscle_building_workout(equipment, workout_time, fitness_level, age))
        elif goal == 'endurance':
            workout_plan.extend(create_endurance_workout(equipment, workout_time, fitness_level, age))
        elif goal == 'flexibility':
            workout_plan.extend(create_flexibility_workout(equipment, workout_time, fitness_level, age))
        else:  # general_fitness
            workout_plan.extend(create_general_fitness_workout(equipment, workout_time, fitness_level, age))

        # Cool-down (always included)
        workout_plan.append("🧊 Cool-down: 3 minutes stretching")

        # Add safety reminders based on age and fitness level
        if age > 50 or fitness_level == 'beginner':
            workout_plan.append("⚠️ Listen to your body - rest if you feel dizzy")

        if fitness_level == 'advanced':
            workout_plan.append("🚀 Challenge yourself but maintain proper form")

        return workout_plan

    except Exception as e:
        # Fallback workout
        return [
            "🔥 Warm-up: 3 minutes walking in place",
            "💪 10 bodyweight squats",
            "🤲 10 push-ups (knee push-ups if needed)",
            "🤸‍♂️ 30-second plank hold",
            "🧊 Cool-down: 3 minutes stretching"
        ]

def create_weight_loss_workout(equipment, time, fitness_level, age):
    """Create cardio-focused workout for weight loss"""

    exercises = []

    # High-intensity cardio focus
    if 'none' in equipment:  # Bodyweight only
        if fitness_level == 'beginner':
            exercises.extend([
                "🚶‍♂️ 10 minutes brisk walking/marching",
                "🤸‍♂️ 2 minutes jumping jacks (or step-ups)",
                "🦵 15 bodyweight squats",
                "🤲 10 wall push-ups",
                "🔥 1 minute rest, then repeat"
            ])
        elif fitness_level == 'intermediate':
            exercises.extend([
                "🏃‍♂️ 5 minutes jogging in place",
                "🤸‍♂️ 3 minutes jumping jacks + burpees",
                "🦵 20 squats + 15 lunges each leg",
                "🤲 15 push-ups",
                "🔥 30 seconds mountain climbers"
            ])
        else:  # advanced
            exercises.extend([
                "🏃‍♂️ 8 minutes high-intensity interval running",
                "🤸‍♂️ 50 jumping jacks + 10 burpees",
                "🦵 30 squats + 20 lunges each leg",
                "🤲 20 push-ups + 1 minute plank",
                "🔥 2 minutes continuous movement"
            ])

    elif 'jump_rope' in equipment:
        exercises.extend([
            "🪢 10 minutes jump rope (with breaks)",
            "🦵 20 squats",
            "🤲 15 push-ups",
            "🤸‍♂️ 1 minute high knees"
        ])

    elif 'treadmill' in equipment or 'bicycle' in equipment:
        cardio_equipment = 'treadmill' if 'treadmill' in equipment else 'bicycle'
        exercises.extend([
            f"🏃‍♂️ 15 minutes {cardio_equipment} (moderate pace)",
            "🦵 15 bodyweight squats",
            "🤲 10 push-ups",
            "🤸‍♂️ 2 minutes cool-down walk"
        ])

    # Add strength component with available equipment
    if 'dumbbells' in equipment:
        exercises.append("🏋️‍♂️ 3 sets: 12 dumbbell swings")

    return exercises

def create_muscle_building_workout(equipment, time, fitness_level, age):
    """Create strength-focused workout for muscle building"""

    exercises = []

    if 'none' in equipment:  # Bodyweight strength training
        if fitness_level == 'beginner':
            exercises.extend([
                "🤲 3 sets of 8-12 wall/knee push-ups",
                "🦵 3 sets of 10-15 squats",
                "🤸‍♂️ 3 sets of 15-20 second plank",
                "🚶‍♂️ 3 sets of 10 lunges each leg",
                "💪 2 minutes rest between sets"
            ])
        elif fitness_level == 'intermediate':
            exercises.extend([
                "🤲 4 sets of 12-15 push-ups",
                "🦵 4 sets of 15-20 squats",
                "🤸‍♂️ 3 sets of 30-45 second plank",
                "🚶‍♂️ 3 sets of 12 lunges each leg",
                "🦵 3 sets of 8-10 single-leg glute bridges"
            ])
        else:  # advanced
            exercises.extend([
                "🤲 4 sets of 15-20 push-ups (add variations)",
                "🦵 4 sets of 20-25 squats + jump squats",
                "🤸‍♂️ 3 sets of 60 second plank + side planks",
                "🚶‍♂️ 4 sets of 15 lunges + reverse lunges",
                "💪 3 sets of 10 pike push-ups"
            ])

    elif 'dumbbells' in equipment:
        exercises.extend([
            "🏋️‍♂️ 4 sets of 10-12 dumbbell chest press",
            "🏋️‍♂️ 4 sets of 12-15 dumbbell rows",
            "🏋️‍♂️ 3 sets of 10-12 dumbbell squats",
            "🏋️‍♂️ 3 sets of 8-10 dumbbell shoulder press",
            "🏋️‍♂️ 3 sets of 12-15 dumbbell bicep curls"
        ])

    elif 'pull_up_bar' in equipment:
        exercises.extend([
            "🤸‍♂️ 3 sets of max pull-ups (or assisted)",
            "🤲 4 sets of 12-15 push-ups",
            "🦵 4 sets of 15-20 squats",
            "🤸‍♂️ 3 sets of 30-45 second hanging"
        ])

    if 'resistance_bands' in equipment:
        exercises.append("🎗️ 3 sets of 15 resistance band exercises")

    return exercises

def create_endurance_workout(equipment, time, fitness_level, age):
    """Create cardio-endurance focused workout"""

    exercises = []

    if 'treadmill' in equipment:
        if fitness_level == 'beginner':
            exercises.extend([
                "🏃‍♂️ 15 minutes steady walk (slight incline)",
                "🚶‍♂️ 2 minutes recovery walk",
                "🏃‍♂️ 5 minutes light jog",
                "🧊 5 minutes cool-down walk"
            ])
        else:
            exercises.extend([
                "🏃‍♂️ 20 minutes interval running",
                "🚶‍♂️ 3 minutes recovery walk",
                "🏃‍♂️ 5 minutes steady pace",
                "🧊 3 minutes cool-down"
            ])

    elif 'bicycle' in equipment:
        exercises.extend([
            "🚴‍♂️ 20-25 minutes cycling (moderate pace)",
            "🦵 10 squats for leg strength",
            "🤸‍♂️ 2 minutes core exercises"
        ])

    elif 'jump_rope' in equipment:
        exercises.extend([
            "🪢 15 minutes jump rope intervals",
            "🚶‍♂️ 30 seconds rest between 2-minute sets",
            "🦵 2 minutes leg exercises"
        ])

    else:  # Bodyweight cardio
        exercises.extend([
            "🏃‍♂️ 10 minutes jogging in place",
            "🤸‍♂️ 5 minutes jumping jacks + high knees",
            "🚶‍♂️ 3 minutes step-ups (use stairs/chair)",
            "🔥 2 minutes burpees (modified if needed)"
        ])

    return exercises

def create_flexibility_workout(equipment, time, fitness_level, age):
    """Create flexibility and mobility focused workout"""

    exercises = []

    # Basic flexibility routine
    exercises.extend([
        "🧘‍♂️ 5 minutes gentle neck and shoulder rolls",
        "🤸‍♀️ 5 minutes spinal twists and cat-cow stretches",
        "🦵 5 minutes leg stretches (hamstring, quad, calf)",
        "🤲 3 minutes arm and chest stretches",
        "🧘‍♂️ 5 minutes hip openers and glute stretches"
    ])

    if 'yoga_mat' in equipment:
        exercises.extend([
            "🧘‍♀️ 10 minutes basic yoga flow",
            "🤸‍♀️ 5 minutes child's pose and pigeon pose",
            "🧘‍♂️ 3 minutes deep breathing in shavasana"
        ])

    # Age-specific modifications
    if age > 50:
        exercises.append("🪑 Include chair-assisted stretches for safety")

    if fitness_level == 'advanced':
        exercises.append("🤸‍♀️ Add advanced poses like warrior III or crow pose")

    return exercises

def create_general_fitness_workout(equipment, time, fitness_level, age):
    """Create balanced workout for general fitness"""

    exercises = []

    # Balanced approach - cardio + strength + flexibility
    workout_sections = time // 3  # Divide time into 3 parts

    # Cardio section
    exercises.extend([
        "🏃‍♂️ 8 minutes light cardio (walking/jogging)",
        "🤸‍♂️ 2 minutes jumping movements"
    ])

    # Strength section
    if 'none' in equipment:
        exercises.extend([
            "🤲 2 sets of 10 push-ups",
            "🦵 2 sets of 15 squats",
            "🤸‍♂️ 2 sets of 20-second plank"
        ])
    else:
        if 'dumbbells' in equipment:
            exercises.append("🏋️‍♂️ 3 sets of basic dumbbell exercises")
        if 'resistance_bands' in equipment:
            exercises.append("🎗️ 2 sets of resistance band exercises")

    # Flexibility section
    exercises.extend([
        "🧘‍♂️ 5 minutes full-body stretching",
        "🤸‍♀️ 2 minutes deep breathing"
    ])

    return exercises

def generate_meal_plan(user_data):
    """
    Generate meal suggestions based on dietary preferences and goals
    """

    meals = []
    diet = user_data['diet']
    goal = user_data['goal']
    age = user_data['age']

    try:
        # Breakfast suggestions
        breakfast = get_breakfast_options(diet, goal)
        meals.append(f"🌅 Breakfast: {breakfast}")

        # Pre-workout snack (if time allows)
        if user_data['time'] >= 30:
            pre_workout = get_pre_workout_snack(diet, goal)
            meals.append(f"💪 Pre-workout: {pre_workout}")

        # Post-workout meal
        post_workout = get_post_workout_meal(diet, goal)
        meals.append(f"🥗 Post-workout: {post_workout}")

        # Lunch suggestions
        lunch = get_lunch_options(diet, goal)
        meals.append(f"🍽️ Lunch: {lunch}")

        # Evening snack
        evening_snack = get_evening_snack(diet, goal)
        meals.append(f"🌆 Evening: {evening_snack}")

        # Dinner
        dinner = get_dinner_options(diet, goal)
        meals.append(f"🌙 Dinner: {dinner}")

        # Hydration reminder
        meals.append("💧 Drink 8-10 glasses of water throughout the day")

        # Special dietary notes
        if goal == 'weight_loss':
            meals.append("⚖️ Eat slowly and stop when 80% full")
        elif goal == 'weight_gain' or goal == 'muscle_building':
            meals.append("💪 Add healthy fats like nuts and avocado")

        return meals

    except Exception as e:
        # Fallback meal plan
        return [
            "🌅 Breakfast: Oats with banana and nuts",
            "🥗 Lunch: Dal, rice, and vegetables",
            "🌙 Dinner: Light meal with proteins",
            "💧 Drink plenty of water"
        ]

def get_breakfast_options(diet, goal):
    """Get breakfast based on diet and goal"""

    options = {
        'vegetarian': [
            "Oats with milk, banana, and honey",
            "2 whole wheat parathas with curd",
            "Upma with vegetables and coconut",
            "Poha with peanuts and curry leaves"
        ],
        'vegan': [
            "Oats with almond milk and fruits",
            "2 rotis with vegetable curry",
            "Quinoa porridge with berries",
            "Smoothie with banana and plant milk"
        ],
        'non_vegetarian': [
            "2 eggs with whole wheat toast",
            "Chicken sandwich with vegetables",
            "Egg paratha with mint chutney",
            "Protein smoothie with banana"
        ],
        'jain': [
            "Rice with moong dal and ghee",
            "Sabudana khichdi with peanuts",
            "Oats with milk and dates",
            "Wheat porridge with jaggery"
        ],
        'keto': [
            "2 eggs with avocado and cheese",
            "Coconut flour pancakes",
            "Greek yogurt with nuts",
            "Bulletproof coffee with MCT oil"
        ]
    }

    diet_options = options.get(diet, options.get('no_preference', options['vegetarian']))
    return random.choice(diet_options)

def get_pre_workout_snack(diet, goal):
    """Get pre-workout snack options"""

    snacks = {
        'energy': ["1 banana", "Handful of dates", "Green tea", "1 apple with peanut butter"],
        'light': ["1 glass water with lemon", "5-6 almonds", "Green tea", "1 small fruit"]
    }

    snack_type = 'energy' if goal in ['muscle_building', 'endurance'] else 'light'
    return random.choice(snacks[snack_type])

def get_post_workout_meal(diet, goal):
    """Get post-workout meal based on goal"""

    if goal in ['weight_gain', 'muscle_building']:
        if diet == 'vegetarian':
            options = ["Protein shake with milk", "Paneer sandwich", "Curd with fruits", "Chocolate milk"]
        elif diet == 'vegan':
            options = ["Plant protein smoothie", "Nuts and fruits", "Soy milk with banana", "Coconut water"]
        elif diet == 'non_vegetarian':
            options = ["Whey protein shake", "Boiled eggs with banana", "Chicken sandwich", "Protein smoothie"]
        else:
            options = ["Milk with banana", "Mixed nuts", "Fresh fruit juice", "Coconut water"]
    else:  # Weight loss or general fitness
        options = ["Coconut water", "1 fruit", "Green tea", "Buttermilk", "Lemon water"]

    return random.choice(options)

def get_lunch_options(diet, goal):
    """Get lunch options based on diet"""

    options = {
        'vegetarian': [
            "Dal, rice, vegetable, and curd",
            "Rajma with brown rice and salad",
            "Mixed vegetable curry with rotis",
            "Sambar rice with vegetables"
        ],
        'vegan': [
            "Dal, rice, and mixed vegetables",
            "Quinoa with roasted vegetables",
            "Brown rice with sambhar",
            "Mixed grain khichdi"
        ],
        'non_vegetarian': [
            "Chicken curry with rice and salad",
            "Fish with vegetables and roti",
            "Egg curry with brown rice",
            "Grilled chicken with quinoa"
        ],
        'jain': [
            "Moong dal with rice and ghee",
            "Toor dal with rotis",
            "Mixed vegetable without root vegetables",
            "Khichdi with clarified butter"
        ],
        'keto': [
            "Grilled paneer with salad",
            "Cauliflower rice with curry",
            "Cheese omelet with vegetables",
            "Avocado salad with nuts"
        ]
    }

    diet_options = options.get(diet, options.get('no_preference', options['vegetarian']))
    return random.choice(diet_options)

def get_evening_snack(diet, goal):
    """Get evening snack options"""

    healthy_snacks = [
        "Green tea with 4-5 nuts",
        "1 fruit (apple/orange/pear)",
        "Buttermilk with roasted cumin",
        "Handful of roasted chana",
        "Herbal tea with 2 dates"
    ]

    return random.choice(healthy_snacks)

def get_dinner_options(diet, goal):
    """Get dinner options - lighter than lunch"""

    options = {
        'vegetarian': [
            "2 rotis with vegetable and dal",
            "Khichdi with curd and pickle",
            "Vegetable soup with bread",
            "Light dal with rice"
        ],
        'vegan': [
            "2 rotis with vegetable curry",
            "Quinoa salad with vegetables",
            "Vegetable soup with toast",
            "Mixed dal with brown rice"
        ],
        'non_vegetarian': [
            "Grilled chicken with salad",
            "Fish curry with 1 roti",
            "Egg bhurji with 2 rotis",
            "Chicken soup with bread"
        ],
        'jain': [
            "Light moong dal with rice",
            "Vegetable khichdi",
            "Toor dal with 2 rotis",
            "Mixed vegetables without onion-garlic"
        ],
        'keto': [
            "Grilled vegetables with paneer",
            "Cauliflower rice with curry",
            "Salad with avocado and nuts",
            "Coconut curry with vegetables"
        ]
    }

    diet_options = options.get(diet, options.get('no_preference', options['vegetarian']))
    return random.choice(diet_options)

def generate_evening_routine(user_data):
    """Generate evening wind-down routine"""

    evening_activities = []
    time = user_data['time']
    age = user_data['age']
    goal = user_data['goal']

    try:
        # Basic evening routine
        evening_activities.extend([
            "🌅 Reflect on your workout - how did it feel?",
            "📝 Track your progress (even small wins count)",
            "💧 Ensure you've had enough water today"
        ])

        if time >= 15:
            evening_activities.extend([
                "🧘‍♂️ 5 minutes light stretching or meditation",
                "📖 Read something positive for 10 minutes"
            ])

        if time >= 25:
            evening_activities.extend([
                "🛁 Take a relaxing shower or bath",
                "🎵 Listen to calming music"
            ])

        # Goal-specific evening activities
        if goal == 'weight_loss':
            evening_activities.append("⚖️ Prepare healthy snacks for tomorrow")
        elif goal == 'muscle_building':
            evening_activities.append("💪 Plan tomorrow's protein sources")
        elif goal == 'flexibility':
            evening_activities.append("🧘‍♀️ Do 5 minutes of evening yoga poses")

        # Age-specific recommendations
        if age > 40:
            evening_activities.append("😴 Aim to sleep by 10 PM for recovery")
        else:
            evening_activities.append("😴 Get 7-8 hours of quality sleep")

        # Universal ending
        evening_activities.extend([
            "📱 Put devices away 30 minutes before bed",
            "🙏 Take 3 deep breaths and appreciate your efforts today"
        ])

        return evening_activities

    except Exception as e:
        # Fallback evening routine
        return [
            "🧘‍♂️ 5 minutes relaxation",
            "📝 Note one good thing about today",
            "😴 Get good sleep for recovery"
        ]

def get_daily_tip(user_data):
    """Generate daily motivational tip based on user profile"""

    goal = user_data['goal']
    fitness_level = user_data['fitness_level']
    age = user_data['age']

    try:
        # Goal-specific tips
        goal_tips = {
            'weight_loss': [
                "Small calorie deficits consistently beat crash diets every time!",
                "Focus on how you feel, not just the number on the scale.",
                "Every healthy choice is a victory - celebrate small wins!",
                "Consistency over perfection - one day at a time."
            ],
            'weight_gain': [
                "Gaining healthy weight takes time - be patient with yourself.",
                "Focus on nutrient-dense foods, not just calories.",
                "Strength training helps build muscle, not just fat.",
                "Eat regularly throughout the day to support your goals."
            ],
            'muscle_building': [
                "Muscles grow during rest, not just during workouts.",
                "Progressive overload is key - gradually increase difficulty.",
                "Protein within 30 minutes after workout helps recovery.",
                "Form over speed - quality reps build quality muscle."
            ],
            'endurance': [
                "Endurance is built gradually - increase intensity slowly.",
                "Listen to your breathing - it tells you about your pace.",
                "Consistency in cardio beats occasional intense sessions.",
                "Recovery days are part of training, not skipping training."
            ],
            'flexibility': [
                "Flexibility improvements come with daily practice.",
                "Never force a stretch - gentle persistence wins.",
                "Breathe deeply during stretches for better results.",
                "Flexibility benefits both body and mind relaxation."
            ],
            'general_fitness': [
                "Health is a journey, not a destination.",
                "Every movement counts - even taking stairs helps.",
                "Balance is key - mix cardio, strength, and flexibility.",
                "Your future self will thank you for starting today."
            ]
        }

        # Fitness level tips
        level_tips = {
            'beginner': [
                "Start slow and build gradually - your body is learning.",
                "Soreness is normal, but pain is a warning sign.",
                "Focus on building the habit first, intensity comes later.",
                "Every expert was once a beginner - be proud of starting!"
            ],
            'intermediate': [
                "Challenge yourself, but don't sacrifice form for intensity.",
                "Variety in workouts prevents plateaus and boredom.",
                "Track your progress to see how far you've come.",
                "Help a beginner - teaching reinforces your own knowledge."
            ],
            'advanced': [
                "Recovery becomes more important as intensity increases.",
                "Consider periodization - plan cycles of intensity.",
                "Lead by example - inspire others with your dedication.",
                "Remember why you started - keep the passion alive."
            ]
        }

        # Age-specific tips
        age_tips = []
        if age < 25:
            age_tips = [
                "Build habits now that will serve you for life.",
                "Your metabolism is high - use it wisely!",
                "Focus on movement quality to prevent future injuries."
            ]
        elif age < 40:
            age_tips = [
                "Consistency beats intensity - make it sustainable.",
                "Stress management is part of fitness too.",
                "Invest in your health now to avoid problems later."
            ]
        else:
            age_tips = [
                "It's never too late to improve your fitness!",
                "Focus on functional movements for daily life.",
                "Recovery time increases with age - plan accordingly."
            ]

        # Combine and select random tip
        all_tips = (goal_tips.get(goal, []) + 
                   level_tips.get(fitness_level, []) + 
                   age_tips)

        if all_tips:
            return random.choice(all_tips)
        else:
            return "Every step forward is progress - keep going!"

    except Exception as e:
        # Fallback motivational tip
        motivational_tips = [
            "Consistency beats perfection every single day!",
            "Your body can do it - it's your mind you need to convince.",
            "Progress, not perfection, is the goal.",
            "Every workout is a gift to your future self.",
            "Strong is not a size, it's a feeling.",
            "The only bad workout is the one you didn't do."
        ]

        return random.choice(motivational_tips)

def create_fallback_routine(user_data):
    """
    Create a simple fallback routine when main generation fails
    Ensures user always gets something useful
    """

    try:
        name = user_data.get('name', 'Friend')
        time = user_data.get('time', 20)

        return {
            'morning': [
                "🌅 Wake up and drink a glass of water",
                "🧘‍♂️ 3 minutes light stretching",
                "💭 Set a positive intention for the day"
            ],
            'workout': [
                "🔥 Warm-up: 2 minutes light movement",
                "💪 10 bodyweight squats",
                "🤲 10 push-ups (modify as needed)",
                "🤸‍♂️ 30-second plank hold",
                "🦵 10 lunges each leg",
                "🧊 Cool-down: 3 minutes stretching"
            ],
            'meals': [
                "🌅 Breakfast: Healthy meal with protein",
                "🥗 Lunch: Balanced meal with vegetables",
                "🌙 Dinner: Light and nutritious meal",
                "💧 Drink 8 glasses of water throughout the day"
            ],
            'evening': [
                "🧘‍♂️ 5 minutes relaxation or meditation",
                "📝 Reflect on one positive thing from today",
                "😴 Get 7-8 hours of quality sleep"
            ],
            'tip': f"Hey {name}! Remember - small consistent efforts lead to big results!",
            'created_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'user_goal': user_data.get('goal', 'general_fitness'),
            'total_time': time
        }

    except Exception as e:
        # Ultimate fallback - minimal routine
        return {
            'morning': ["🌅 Start your day with water and positivity"],
            'workout': ["💪 Move your body for at least 10 minutes"],
            'meals': ["🥗 Eat balanced, nutritious meals"],
            'evening': ["😴 Rest well for tomorrow"],
            'tip': "Every small step counts towards your health goals!",
            'created_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'user_goal': 'general_fitness',
            'total_time': 15
        }

def validate_routine(routine):
    """
    Validate that generated routine has all required sections
    Fix any missing or invalid sections
    """

    required_sections = ['morning', 'workout', 'meals', 'evening', 'tip']

    try:
        # Check if routine is dictionary
        if not isinstance(routine, dict):
            return False

        # Check all required sections exist
        for section in required_sections:
            if section not in routine:
                return False

            # Check morning, workout, meals, evening are lists
            if section != 'tip' and not isinstance(routine[section], list):
                return False

            # Check lists are not empty
            if section != 'tip' and len(routine[section]) == 0:
                return False

        # Check tip is string
        if not isinstance(routine['tip'], str) or len(routine['tip']) == 0:
            return False

        return True

    except Exception as e:
        return False

def get_routine_summary(routine, user_data):
    """
    Generate a summary of the routine for quick overview
    """

    try:
        total_activities = (len(routine.get('morning', [])) + 
                           len(routine.get('workout', [])) + 
                           len(routine.get('meals', [])) + 
                           len(routine.get('evening', [])))

        summary = {
            'total_activities': total_activities,
            'estimated_time': user_data['time'],
            'goal_focus': user_data['goal'].replace('_', ' ').title(),
            'difficulty_level': user_data['fitness_level'].title(),
            'equipment_needed': len(user_data.get('equipment', [])) > 0 and 'none' not in user_data['equipment']
        }

        return summary

    except Exception as e:
        return {
            'total_activities': 0,
            'estimated_time': 20,
            'goal_focus': 'General Fitness',
            'difficulty_level': 'Beginner',
            'equipment_needed': False
        }

def save_routine_template(routine, user_data):
    """
    Save routine as a template for future use
    Creates reusable routine templates
    """

    try:
        # Create templates directory if it doesn't exist
        if not os.path.exists("templates"):
            os.makedirs("templates")

        # Create template filename
        template_name = f"{user_data['goal']}_{user_data['fitness_level']}_{user_data['time']}min.json"
        template_path = os.path.join("templates", template_name)

        # Prepare template data
        template_data = {
            'routine': routine,
            'user_profile': {
                'goal': user_data['goal'],
                'fitness_level': user_data['fitness_level'],
                'time': user_data['time'],
                'equipment': user_data['equipment']
            },
            'created_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'template_version': '1.0'
        }

        # Save template
        with open(template_path, 'w', encoding='utf-8') as file:
            json.dump(template_data, file, indent=2, ensure_ascii=False)

        return template_path

    except Exception as e:
        # Template saving failed, but routine still works
        print(f"⚠️ Could not save template: {str(e)}")
        return None

def load_routine_template(goal, fitness_level, time_range):
    """
    Load existing routine template if available
    Speeds up routine generation for common profiles
    """

    try:
        templates_dir = "templates"
        if not os.path.exists(templates_dir):
            return None

        # Look for matching template
        template_files = os.listdir(templates_dir)

        for template_file in template_files:
            if (goal in template_file and 
                fitness_level in template_file and 
                template_file.endswith('.json')):

                template_path = os.path.join(templates_dir, template_file)

                with open(template_path, 'r', encoding='utf-8') as file:
                    template_data = json.load(file)

                # Check if template matches requirements
                profile = template_data.get('user_profile', {})
                if (profile.get('goal') == goal and 
                    profile.get('fitness_level') == fitness_level):

                    return template_data.get('routine')

        return None

    except Exception as e:
        # Template loading failed, generate fresh routine
        return None

# Utility functions for routine customization

def adjust_routine_for_time(routine, available_time):
    """
    Adjust routine activities based on available time
    Scales up or down the routine appropriately
    """

    try:
        if available_time < 15:
            # Minimal routine for very short time
            routine['workout'] = routine['workout'][:3]  # Keep only 3 exercises
            routine['morning'] = routine['morning'][:2]  # Keep only 2 morning activities
            routine['evening'] = routine['evening'][:2]  # Keep only 2 evening activities

        elif available_time > 60:
            # Extended routine for longer time
            routine['workout'].append("🏃‍♂️ Add 5 minutes extra cardio")
            routine['morning'].append("📖 Read something motivational for 5 minutes")
            routine['evening'].append("🛁 Take time for a relaxing bath/shower")

        return routine

    except Exception as e:
        return routine

def add_seasonal_adjustments(routine, user_data):
    """
    Add seasonal adjustments to routine based on current date
    Makes routine more relevant to current weather/season
    """

    try:
        current_month = datetime.now().month

        # Summer adjustments (April to June in India)
        if 4 <= current_month <= 6:
            routine['morning'].insert(1, "🌤️ Exercise early morning to avoid heat")
            routine['meals'].append("🥤 Include cooling foods like cucumber, watermelon")
            routine['evening'].append("💧 Extra hydration - add lemon water or coconut water")

        # Monsoon adjustments (July to September)
        elif 7 <= current_month <= 9:
            routine['workout'].append("🏠 Have indoor backup exercises for rainy days")
            routine['meals'].append("🍵 Include warm foods and ginger tea for immunity")

        # Winter adjustments (December to February)
        elif current_month in [12, 1, 2]:
            routine['morning'].insert(1, "☀️ Exercise when sun is up for vitamin D")
            routine['meals'].append("🔥 Include warming foods like nuts and dates")

        return routine

    except Exception as e:
        return routine