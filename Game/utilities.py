import typing

def eval_boolean(x:str) -> bool: # evaluates whether a response means yes or no
    positive = "y yes ok okay k kk ye positive true affirmative"
    positive = positive.split()
    negative = "n no negative naw bruh negative false deny"
    negative = negative.split()


    if x in positive: return True
    elif x in negative: return False
    else: return False # this is easier than having it return None


#print( eval_boolean(9)   )