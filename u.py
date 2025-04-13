import os

# Folder where files will be created (optional)
folder = "PythonSlips"
os.makedirs(folder, exist_ok=True)

# Loop through slips 1 to 21
for slip_num in range(1, 22):
    for q_num in range(1, 3):  # Q1 and Q2
        filename = f"slip{slip_num}_q{q_num}.py"
        filepath = os.path.join(folder, filename)
        with open(filepath, "w") as f:
            f.write(f"# Python code for Slip {slip_num}, Question {q_num}\n")
        print(f"Created: {filename}")
