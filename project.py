with open("file_1", "w") as f:
    f.write(
        "\nПривет\nHI, error\nсалам\nerroR, хуфыв, \n12312441asderierrrod\neRrOr_123"
    )

with open("file_1", "r") as f:
    text = f.read()


with open("file_1", "w") as f:
    f.write(text.lower())

with open("file_1", "r") as f:
    for line in f:
        if "error" in line:
            print(line.strip())
