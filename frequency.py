def frequent (arr, n):
    hashtable = dict()

    # Storing the frequency of each element of the array
    for i in range(n):
        if arr[i] in hashtable.keys():
            hashtable[arr[i]] += 1
        else:
            hashtable[arr[i]] = 1

    # Finding the maximum frequency
    max_freq = 0
    element = -1

    for i in hashtable:
        if hashtable[i] > max_freq :
            element = i
            max_freq = hashtable[i]

    return element
