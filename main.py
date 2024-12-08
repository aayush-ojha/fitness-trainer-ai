import google.generativeai as genai
import api_keys

genai.configure(api_key=api_keys.gemini_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def get_response():
    input_text = input("What would you like to ask? ")
    prompt = f"As an experienced fitness trainer, respond to the client's question: '{input_text}'"
    response = model.generate_content(prompt)
    return response.text

def get_workout_plan():
    fitness_level = input("What's your fitness level (beginner, intermediate, advanced)? ")
    goals = input("What are your fitness goals? ")
    available_days = input("How many days per week can you work out? ")
    prompt = (f"As an experienced fitness trainer, create a detailed weekly workout plan for a "
              f"{fitness_level} focusing on {goals}, available to work out {available_days} days per week.")
    response = model.generate_content(prompt)
    return response.text

def get_nutrition_advice():
    dietary_preferences = input("Do you have any dietary preferences or restrictions? ")
    goals = input("What are your nutrition goals? (e.g., weight loss, muscle gain, maintenance) ")
    prompt = (f"As an experienced fitness trainer, provide a balanced weekly diet plan suitable for a "
              f"beginner with dietary preferences/restrictions: {dietary_preferences}, aiming for {goals}.")
    response = model.generate_content(prompt)
    return response.text

def main():
    print("Welcome to the AI Fitness Trainer!")
    while True:
        print("\nMenu:")
        print("1. Get fitness advice")
        print("2. Get a workout plan")
        print("3. Get nutrition advice")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print(get_response())
        elif choice == '2':
            print(get_workout_plan())
        elif choice == '3':
            print(get_nutrition_advice())
        elif choice == '4':
            print("Thank you for using the AI Fitness Trainer. Stay active!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()