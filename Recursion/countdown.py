

def countdown(num):
    if num == 0:
        return
    print(num)
    countdown(num-1)


countdown(5)