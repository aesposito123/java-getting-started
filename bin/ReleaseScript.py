import os
import subprocess
import sys

def main():
    install_aws_cli()

def install_aws_cli():
    print("Downloading AWS CLI...")
    run_command(["curl", "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip", "-o", "awscliv2.zip"])
    print("Unzipping AWS CLI package...")
    run_command(["unzip", "awscliv2.zip"])
    print("Installing AWS CLI...")
    run_command(["sudo", "./aws/install"])
    print("Cleaning up...")
    run_command(["rm", "-rf", "awscliv2.zip aws"])
    print("Verifying installation...")
    run_command(["aws", "--version"])

def run_command(command, input_string=None, require_success=True):
    result = subprocess.run(command, input=input_string, text=True)
    if require_success:
        if result.returncode != 0:
            full_command = " ".join(command)
            raise BaseException( full_command + " returned exit code result.returncode " + str(result.returncode))
    return result

if __name__ == "__main__":
    main()