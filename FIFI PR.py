def FIFI_PR(string, no_frame):
    frame = []
    lst = []
    page_fault = 0

    for i in string:
        if i not in frame:
            if len(frame) <= no_of_frame-1:
                frame.append(i)
                page_fault = page_fault + 1
            else:
                pass
        else:
            pass

    t=0
    for i in range(no_of_frame):
        string.remove(string[0])

    for i in string:
        if i not in frame:
            for j in range(t,no_of_frame):
                frame[j] = i
                t = t + 1
                break
            page_fault = page_fault + 1
            if t == no_of_frame:
                t = 0
        else:
            pass
    print("Page fault occurs ", page_fault, "Times")


no_of_frame = int(input("Enter number of frame : "))
string = []
size = int(input("Enter number of pages  : "))
for i in range(size):
    value = int(input("enter value : "))
    string.append(value)

FIFI_PR(string, no_of_frame)





