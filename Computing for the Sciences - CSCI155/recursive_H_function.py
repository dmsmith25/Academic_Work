
def recursive_H(length, level):
    if level == 0:
        t.dot()
        
    else:
        t.back(length)
        t.left(90)
        t.forward(length / 2)
        t.right(90)
        recursive_H(length / 2, level - 1)
        t.left(90)
        t.back(length)
        t.right(90)
        recursive_H(length / 2, level - 1)
        t.left(90)
        t.forward(length / 2)
        t.left(90)
        t.back(length * 2)
        t.right(90)
        t.forward(length / 2)
        t.right(90)
        recursive_H(length / 2, level - 1)
        t.left(90)
        t.back(length)
        t.right(90)
        recursive_H(length / 2, level - 1)
        t.left(90)
        t.forward(length / 2)
        t.right(90)
        t.back(length)
