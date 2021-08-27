#%%
n = 100
# set has special characteristic to delete no primers
number_range = set(range(2,n+1))
primes_list = []
#%%
while number_range:
    prime = number_range.pop()
    primes_list.append(prime)
    multiples = set(range(prime*2, n+1,prime))
    #this is a prowerful way to erase items that appear in other set
    number_range.difference_update(multiples)
print(primes_list)
prime_count = len(primes_list)
largest_prime = max(primes_list)
print(f'''There are {prime_count} prime numbers between  and {n}, 
where the maximum is {largest_prime}''')