import random
import piglatin
l1 = [1,2,3,5]
s = 'hello world'
number = 20

def make_list(item):
    return [item]

list_of_tens = []
for i in range(5):
    list_of_tens.append(10)

counting_list = []
for i in range(10):
    counting_list = counting_list + [i]

random_list = []
for i in range(20):
    random_list.append(random.randrange(5,15))
    
odds = []
for item in random_list:
    if item%2==1:
        odds.append(item)

squares = []
for item in random_list:
    squares.append(item*item)
    

def square(x):
    return x*x

counting = [x for x in range(5,10)]
tens_v2 = [10 for x in range(15) ]
random_list_v2 = [random.randrange(5,10) for x in range(20)]
random_list_v3 = [random.randrange(x) for x in range(1,100,5)]
sentence = "now is the winter of our discontent"
upper_case = [piglatin.piglatinify(word.capitalize()) for word in sentence.split()]

sqlist = [x*x for x in random_list_v3]

l = [x for x in range(20)]
odds = [x for x in l if x%2 ==1]
evens = [x for x in l if x%2 ==0]
bignums = [x for x in l if x>10]
shortwords = [w for w in sentence.split() if len(w) < 4]
vwords = [w for w in sentence.split() if w[0] in 'aeiou']