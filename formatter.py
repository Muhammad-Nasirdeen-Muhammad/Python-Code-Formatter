import time
try:
    import autopep8

    Gfile = ""

    def formatCode(file):
        Gfile = file
        Openfile = open(f"{file}.py", "r")
        fileContent = Openfile.read()
        return autopep8.fix_code(fileContent)

    def wait(secs=1):
        time.sleep(secs)
    while True:
        print("""Enter:
1. Format Code
2. Exit
        """)
        choice = input("Enter option: ")
        if choice == "1":
            try:
                path = input(
                    "Path to the python file you want to be formatted(Note - Don't add the extension(.py)): ")
                Gfile = f"{path}.py"
                FormattedCode = formatCode(path)
                print(f"""Here is your formatted Python code:
    {FormattedCode}""")
                print("Should we modify the orirginal code")
                isApproved = input("Yes or No: ").upper()
                if isApproved == "YES":
                    OpenFile = open(Gfile, "w")
                    OpenFile.write(f"{FormattedCode}")
                    print("Modifying...")
                    wait()
                    print("Done")
                    OpenFile.close()
                elif isApproved == "NO":
                    pass
            except FileNotFoundError:
                print("")
                print("File does not exist, but don't fret try again")
                wait()
        elif choice == "2":
            print("Exiting...")
            print("Exited.")
            break
except ImportError:
    print("""You don't have the required module to run this program.
     pip install autopep8 to run""")
