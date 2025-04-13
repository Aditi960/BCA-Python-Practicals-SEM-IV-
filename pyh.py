import os

output_file = 'all_slips_combined.txt'

with open(output_file, 'w') as outfile:
    for i in range(1, 22):  # From slip1 to slip21
        for q in ['q1', 'q2']:
            filename = f"slip{i}_q{q[-1]}.py"
            if os.path.isfile(filename):
                print(f"Adding {filename}...")
                outfile.write(f"\n\n# --- Start of {filename} ---\n\n")
                with open(filename, 'r') as infile:
                    outfile.write(infile.read())
                outfile.write(f"\n\n# --- End of {filename} ---\n\n")
            else:
                print(f"File not found: {filename}")
                outfile.write(f"\n\n# --- {filename} not found ---\n\n")

print(f"\nDone! Combined content saved in: {output_file}")
