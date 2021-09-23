def swap():
    with open("text1.txt", "r") as a:
        txt1 = a.read()
    with open("text2.txt", "r") as b:
        txt2 = b.read()
    print("Text 1 initially is:" ,txt1)
    print("Text 2 initially is:", txt2)
    with open("text1.txt", "w") as c:
        c.write(txt2)
    with open("text2.txt", "w") as d:
        d.write(txt1)
    with open("text1.txt", "r") as a:
        txt1Cng = a.read()
    with open("text2.txt", "r") as b:
        txt2Cng = b.read()

    print("Text 1 after swap is", txt1Cng)
    print("Text 2 after swap is", txt2Cng)

swap()
