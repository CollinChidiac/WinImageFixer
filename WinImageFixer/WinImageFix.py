import subprocess

def run_command(command):
    print(f"\n[>] Executing: {command}")
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(f"    {output.strip()}")
        return_code = process.poll()
        if return_code == 0:
            print(f"[✓] Command completed successfully.\n")
        else:
            print(f"[✗] Command failed with return code {return_code}.\n")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

def main():
    print("=== Windows System Health Check ===")
    commands = [
        "sfc /scannow",
        "dism /online /cleanup-image /scanhealth",
        "dism /online /cleanup-image /checkhealth",
        "dism /online /cleanup-image /restorehealth"
    ]

    for cmd in commands:
        run_command(cmd)

    print("=== All tasks completed ===")

if __name__ == "__main__":
    main()
