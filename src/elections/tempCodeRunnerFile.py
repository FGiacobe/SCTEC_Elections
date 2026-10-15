
password = "1234"
n = 0
for _ in range(3):
    assert_pass = input("Enter the password: ")
    if assert_pass == password:
        print("Correct password.")
        n += 1
        break

    print("Incorrect password.")
    print(f"Iteration {_}")
    n += 1
