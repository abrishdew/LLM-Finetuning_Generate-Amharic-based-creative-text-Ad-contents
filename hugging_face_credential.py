
import subprocess

# Replace 'your_token_here' with your actual Hugging Face token
token = 'your_token_here'

# Build the command with the token
command = f'huggingface-cli login --token {token}'

# Run the command and capture the output
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Print the output
print("Command Output:")
print(result.stdout)

# Print any errors
if result.stderr:
    print("Command Error:")
    print(result.stderr)
