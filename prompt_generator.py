def generate_prompt(category: str) -> str:
    prompts = {
        "business": "Act as a startup mentor and generate 5 profitable business ideas under $1,000 startup cost.",
        "content": "Act as a viral content strategist and generate 10 short-form video hooks with visual text.",
        "fitness": "Act as a personal trainer and create a beginner 4-week workout plan with 3 workouts per week.",
        "parenting": "Act as a child therapist and give 5 scripts to help a 4-year-old handle disappointment without shutting down."
    }
    return prompts.get(category.lower().strip(), "Valid categories: business, content, fitness, parenting")

if __name__ == "__main__":
    category = input("Enter category (business/content/fitness/parenting): ")
    print(generate_prompt(category))
