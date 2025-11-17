"""
Aseel Rahman
OCT 15, 2025
Lab 9 file operation test
"""


def write_file(filename, msg):
    with open(filename, "w") as file:
        file.write(msg)


def read_file(filename):
    with open(filename, "r") as file:
        file.readlines()


def append_file(filename):
    with open(filename, "a") as file:
        file.write("\nNew line added.")


# function from exercise lab 7 (yesterday)


def email_read(filename, email):
    count = 0
    with open(filename, "r") as file1:
        for line in file1:
            line = line.strip()
            print(line)
            if email in line:
                count += 1
    return count


def write_report(count_gmail, count_yahoo, count_hotmail):
    with open("email_report.txt", "w") as file2:
        file2.write(f"gmail = {count_gmail}\n")
        file2.write(f"yahoo = {count_yahoo}\n")
        file2.write(f"hotmail = {count_hotmail}\n")
    print("email_report.txt created!")
