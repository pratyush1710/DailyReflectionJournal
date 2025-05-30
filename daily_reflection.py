import datetime

# Get today's date
today = datetime.datetime.now().strftime("%Y-%m-%d")

# Create a filename like "Reflection_2025-05-30.txt"
filename = f"Reflection_{today}.txt"

# List of questions
questions = [
    "1. Who did you help today?",
    "2. Did you make someone smile today?",
    "3. Did you drink enough water?",
    "4. What are you grateful for today?",
    "5. What could you improve tomorrow?"
]

# Empty list to store answers
answers = []

print("🌙 Daily Reflection Journal\n")

# Ask questions
for question in questions:
    answer = input(question + " ")
    answers.append(f"{question}\n{answer}\n")

# Save to file
with open(filename, "w") as file:
    file.write(f"Reflection - {today}\n")
    file.write("=" * 30 + "\n\n")
    for answer in answers:
        file.write(answer + "\n")

print(f"\n✅ Your reflections have been saved to '{filename}'. Sleep well! 😴")