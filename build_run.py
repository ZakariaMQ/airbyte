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
        "sudo apt update",
        "sudo apt install -y apt-transport-https ca-certificates curl software-properties-common",
        "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -",
        'sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"',
        "sudo apt update",
        "sudo apt install -y docker-ce",
        "sudo systemctl start docker",
        "sudo systemctl enable docker",
        "sudo usermod -aG docker ${USER}",
        # Log out and log back in to apply the usermod change, can be done manually
        "sudo apt install -y docker-compose-plugin",
        "docker compose version"
    ]
    
    run_commands(commands)
    subprocess.run(['./run-ab-platform.sh'], check=True)
    print("Started Airbyte successfully.")
