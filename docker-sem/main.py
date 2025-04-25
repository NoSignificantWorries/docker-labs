import os
import sys


if __name__ == "__main__":
    os.system("cat /etc/os-release")
    print()
    os.system("python3 --version")
    print()

    username = os.environ.get("MY_USER")
    if username is None:
        print("WARN: Username isn't specified. Using default user login.")
        username = "Unknown"
    print(f"Hello, {username}!")
    print(f"WORK_DIRECTORY is {os.environ.get('MY_WORK_DIR')}")
    print("Files in working directory:")
    os.system("ls -a")
    print()

    args = sys.argv[1:]

    summ = 0.0
    for arg in args:
        try:
            summ += float(arg)
        except BaseException as err:
            continue

    print("Total arguments count:", len(args))
    print("Sum of numeric arguments:", summ)

