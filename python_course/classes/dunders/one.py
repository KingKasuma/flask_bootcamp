def func():
    print("FUNC in one.py")

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
    # RUN THE SCRIPT DIRECTLY
    print('ONE.PY is being run directly!')
else:
    print('ONE.PY has been imported!')