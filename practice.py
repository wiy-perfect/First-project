

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

