# Primes finder Version 4

# upper bound

def primes_finder(n):
    
    # number range to be checked
    number_range = set(range(2, n+1))

    # empty list to append discovered primes to
    primes_list = []

    # while loop
    while number_range:
        
        # prime = number_range.pop()
        prime = min(sorted(number_range))
        number_range.remove(prime)
        
        primes_list.append(prime)
        multiples = set(range(prime*2, n+1, prime))
        number_range.difference_update(multiples)
    
    # print our list of primes
    #print(primes_list)
    
    # number of primes that were found
    prime_count = len(primes_list)

    # largest prime
    largest_prime = max(primes_list)

    # summary
    print(f"There are {prime_count} prime numbers between 2 and {n}, the largest of which is {largest_prime}.")
    
    return primes_list
    

primes_list = primes_finder(int(float(input("Find prime numbers up to: "))))
