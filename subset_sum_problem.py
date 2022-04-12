#this function determines number of subset to make an amount.
# তোমাকে একটা ইন্টিজার অ‍্যারে C দেয়া আছে এবং একটা ভ‍্যালু  W দেয়া আছে।
# তোমাকে বলতে হবে C এর আইটেমগুলো দিয়ে কতভাবে W বানানো যায়।
def subsetsum(arr,i,w):
    if w<0:
        return 0
    if w == 0:
        return 1
    if i>=len(arr):
        return 0
    
    a=subsetsum(arr,i+1,w-arr[i])
    b=subsetsum(arr,i+1,w)
    return a+b

if __name__ == "__main__":
    arr=[5,15,3,17,12]
    w=20
    print(subsetsum(arr,0,w))
