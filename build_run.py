import subprocess

def run_commands(commands):
    for command in commands:
        try:
            print(f"Running: {command}")
            subprocess.run(command, shell=True, check=True)
            print(f"Completed: {command}\n")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running: {command}\nError: {e}")
            break

if __name__ == "__main__":
    commands = [
        "sudo apt install -y docker-compose-plugin",
        "docker compose version",
        "./run-ab-platform.sh -b"
    ]
    
    run_commands(commands)
    print("Started Airbyte successfully.")
