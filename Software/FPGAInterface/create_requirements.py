import os
import subprocess
import sys

def generate_requirements():
    project_path = os.path.dirname(os.path.abspath(__file__))
    try:
        # Use subprocess to run pip freeze and capture its output
        output = subprocess.check_output([sys.executable, "-m", "pip", "freeze"])

        # Define the path to the requirements.txt file
        requirements_file = os.path.join(project_path, "requirements.txt")

        # Write the captured output to requirements.txt
        with open(requirements_file, "wb") as f:
            f.write(output)
        print(f"requirements.txt has been generated in {sys.executable}.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running pipreqs: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    generate_requirements()
