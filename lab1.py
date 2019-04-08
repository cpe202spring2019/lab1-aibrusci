
def max_list_iter(int_list):
    if int_list == None:
        raise ValueError()
    if len(int_list) > 0:
        largest = int_list[0]
        for i in int_list:
            if i > largest:
                largest = i
        return largest
    else:
        return None

def reverse_rec(int_list):
    if int_list == None:
        raise ValueError()
    else:
        if len(int_list) == 0:
            return []
        return [int_list[-1]] + reverse_rec(int_list[:-1])  
         

def bin_search(target, low, high, int_list):
    if int_list == None:
        raise ValueError()
    else:
        mid = (high + low) // 2
        if int_list[mid] == target:
            return mid
        else:
            mid = (high + low) // 2
            if target <= int_list[mid] and target >= int_list[low]:
                high = mid 
                return bin_search(target, low, high, int_list)
            elif target >= int_list[mid] and target <= int_list[high]:
                low = mid + 1
                return bin_search(target, low, high, int_list)
            else:
                return None
