print("")
cats = ['tabby', 'persian_1', 'siamese', 'persian_2']

for cat in cats:
    if "persian" in cat:
        print("Found it:", cat)
        break                   # break uses to break teh loop
    else:
        pass                    # pass means no return
        