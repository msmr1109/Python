#mod1.py
def sum(a,b):
    return a+b

def safe_sum(a, b):
    if type(a) != type(b):
        print("type not same")
        return 
    else:
        result = sum(a.b)
    return result    


if __name__ == "__main__":
    print(sum(3,4))        
    print(sum(5,6))    