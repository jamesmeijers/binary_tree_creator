#a is in order binary tree traversal
#b is post order tree traversal
#x recreates binary tree (with root at x[0]) from a and b (assumes a and b correct)
#x is then printed in order, post order, and depth first

class bin_tree:
    data = 0
    parent = None
    actual_parent = None
    left = 0
    right = 0
    
    def __init__(self, the_data):
        self.data = the_data


def print_tree(root): #In order traversal
    if root.left != 0:
        print_tree(root.left)
    print root.data 
    if root.right != 0:
        print_tree(root.right)
        
        
def print_tree_outside(root): #Post order traversal
    if root.left != 0:
        print_tree_outside(root.left)
    
    if root.right != 0:
        print_tree_outside(root.right)
    print root.data 

def print_tree_depth(root): #depth first traversal
    i = 0
    printed = True
    while printed == True:
        printed = print_tree_at_depth(root, i, 0)
        i += 1
    
def print_tree_at_depth(root, depth, curr_depth):
    if root == 0:
        return False 
    elif curr_depth == depth: 
        print root.data
        return True
    else:
        a = print_tree_at_depth(root.left, depth, curr_depth + 1)
        b = print_tree_at_depth(root.right, depth, curr_depth + 1)
        c = a or b
        return c
    
        


        
def bin_tree_create (a, b):
    """
    Function accepts two vectors of data, a is the printout of a binary tree
    in an in-order traversal, b is the printout of a binary tree in a
    post-order traversal. It produces x, a binary tree representation of a and b
    with the root at 0. Function assumes A and B are in fact correct representations
    of the same binary tree
    """
    # example of possible input
    #a = [4, 2, 7, 5, 8, 1, 3, 9, 6, 11, 10]
    #b = [4, 7, 8, 5, 2, 9, 11, 10, 6, 3, 1]
    x = [None]*len(b)


    i = 0
    j = len(b)

    while i < j:
        x[i] = bin_tree(b[-i - 1])
        i += 1

    #a[0] = b[0] = left most number
    #b[-1] = root
    #a[-1] = right most number

    done = False
    i = 1
    num1 = x[0].data
    num2 = x[1].data
    for tmp in a:
        if tmp == num1:
            x[0].right = x[1]
            break
        elif tmp == num2:
            x[0].left = x[1]
            break

    current = x[0] 
    prev = None

    while i < len(x):
        num = x[i].data
        p = 0
        while p < len(a):
            if a[p] == num:
                if current.parent == None:
                    current.left = x[i]
                    x[i].parent = None
                    x[i].actual_parent = current
                    current = x[i]
                    prev = None
                    i += 1
                    break
                else: 
                    prev = current
                    current = current.parent
                    p = -1
            elif a[p] == current.data:
                if prev == None:
                    current.right = x[i]
                    x[i].parent = current
                    current = x[i]
                    prev = None
                    i += 1
                    break
                else:
                    prev.left = x[i]
                    x[i].parent = prev
                    current = x[i]
                    prev = None
                    i += 1
                    break
            p += 1


    #print_tree(x[0]) 
    #print " "
    #print_tree_outside(x[0]) 
    #print " "
    #print_tree_depth(x[0]) 
    
    return x
            
    