import sys

print("\n\nSYSTEM PATH, VERSION AND PLATFORM!\n\n")
def commandline():
    command_choice = str(input("Select command of choice (version, platform, path): "))

    if command_choice == 'path':
        print(sys.path)

    elif command_choice == 'platform':
        print(sys.platform)

    elif command_choice == 'version':
        print(sys.version)

    else:
        print('Invalid input')

commandline()
