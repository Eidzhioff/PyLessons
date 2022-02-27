from random import sample
from random import choice
import string
pas = string.ascii_letters + string.digits
lst=[7,8,9,10]
n = choice(lst)
print(''.join(sample(pas,n)))
