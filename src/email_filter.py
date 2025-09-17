#https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem?isFullScreen=true
# %%
import re

def fun(s):
    # return True if s is a valid email, else return False
    # return bool(re.match(r'^[a-zA-Z][\w\.-]*[a-zA-Z0-9]@[a-zA-Z0-9][\w\.-]*[a-zA-Z0-9]\.[a-zA-Z][a-zA-Z\.]*[a-zA-Z]$', s))  
    return bool(re.match(r'^[a-zA-Z0-9\-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s))  

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


# testcase 0 
# input
"""
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
"""
# output
# ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

# testcase 1
# input
# 2
# harsh@gmail
# iota_98@hackerrank.com

# output
# ['iota_98@hackerrank.com']
