import re


#function flattens nested list into single list
def flatten(nested_list):
    flat=[]
    for item in nested_list:
        if isinstance(item,list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat

nested_list= [1,[2,3],[[[4],5]]]

print(flatten(nested_list))

#recursive functions lesson
#countdown timer-prints numbers down to 0

def countdown(n):
    # base case: if n is zero
    if n ==0:
        print("Blastoff!")
        return
    # recursive step
    else:
        print(n)
        #calls countdown() with n-1
        countdown(n-1)

countdown(5)

# Reversing string

def reverse_string(s):
    # base case: if string is empty or 1 letter long
    if len(s) <= 1:
        return s
    else:
        # call reverse_string on the rest of the string
        
        return reverse_string(s[1:])+s[0]
print(reverse_string("hello"))

# counts down from a number and returns the successive sum
def countdown_accumulator(n):
    if n == 1:
        return 1
    return n + countdown_accumulator(n-1)

user_input= input()
n= int(user_input)
print(countdown_accumulator(n))



# Unique word counter

def counter(text):
    pattern= r'[^\w\s]'
    replace= ""
    
    text= re.sub(pattern,replace,text)
    
    word_list=[x for x in text.split(" ")]


    d= {}
    for word in word_list:
        d[word]= d.get(word,0)+1
    return d

user_input=input("Enter a string of text: ").lower()
print(counter(user_input))

sample_text = "Python is fun, and learning Python is rewarding!"
print(counter(sample_text.lower()))
