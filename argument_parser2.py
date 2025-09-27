import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--subject_p", help = "physics")
    parser.add_argument("--subject_c", help = "chemistry")
    parser.add_argument("--subject_m" , help = "maths")
    parser.add_argument("--operation", help = "operation", choices = ["average", "total"])

    subs = parser.parse_args()

    print(subs.subject_p)
    print(subs.subject_c)
    print(subs.subject_m)
    print(subs.operation)

    p = int(subs.subject_p)
    c = int(subs.subject_c)
    m = int(subs.subject_m)
    result = None

    if subs.operation == "average":
        result = (p+c+m)/3
    elif subs.operation == "total":
        result = p+c+m
    else:
        print("Invalid Operation")
    print(f"Result: {result}")