import docker
import os
import sys

def main():
    # Load input args from config file

    # Verify docker installed
    os.system("pip3 show docker")


    # Load Docker-Machine client
    client = docker.from_env()
    
    # Dummy Script
    container = client.containers.run("ubuntu", "echo hello world")
    print container

    # Build client machines from input args

    # Set Docker secrets for client machine
    
    # Create Instance with Docker Image
    
    # Copy parent directoy over to instance
    
    # Send run.sh command to load Jupyter

    for line in container.logs(stream=True):
        print line.strip()
    container.stop()

if __name__ == "__main__":
    main()
    print("Output:", sys.stdout)
