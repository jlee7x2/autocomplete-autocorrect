import random
import time
import string
import math
import matplotlib
import matplotlib.pyplot as plt
import autocorrect

'''
string.ascii_letters
'abcdefghijklmnopqrstuvwxyz'

#simple
start=time.time()
print(autocorrect.complete('a'))
end=time.time()
print(end-start)

sum=0.0000
#random sample

for i in range(100):
    ww=random.choice(string.ascii_letters)
    for j in range(2):
         ww=""
         cur = random.choice(string.ascii_letters)
         start2=time.time()
         b=autocorrect.complete(cur+ww)
         print(b)
         ww = ww+cur
         end2=time.time()
         print(end2-start2)
         sum+=end2-start2
avg=sum/200
print("average running time is")
print(avg)

t=autocomplete.Trie()

aa='aa'
for i in range(2):
    t.insert(aa)
    print(t.root)
    start=time.time()
    t.all_words_beginning_with_prefix(aa)
    end=time.time()
    print(list(t.all_words_beginning_with_prefix('a')))
    print(end-start)
    aa=aa+'a'

#input just for testing
#t=autocomplete.Trie()
#r=""
#for k in range(100):
   #a='a'
      #  t.insert('aaaa')
       # b=t.all_words_beginning_with_prefix('a')
       # for r in b:
       #      print(b)
      #  print(b)
   # start3=time.time()
   # b=t.all_words_beginning_with_prefix(a)
  #  end3=time.time()
  #  print(b)
  #  print(end3-start3)

freq = dict()
with open('freq10.json', 'r') as fp:
    freq = json.load(fp)

t = autocomplete.Trie()
for j in range (100):
      for w in freq-j:
            t.insert(w)
            closest_words = autocorrect.get_closest_k_words('a', 2)
            for i in range(len(closest_words)-1, -1, -1):
                 print(str(i+1) + ": " + closest_words[i][0])

closest_words = autocorrect.get_closest_k_words('a', 2)
print(closest_words[0][1])
print(closest_words[1][1])
print(closest_words[0][0])
print(closest_words[1][0])

string.ascii_letters
"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#random sample
ww = "a"
b=""

for j in range(1000):
         cur = random.choice(string.ascii_letters)
         start2=time.time()
         b = autocorrect.complete(ww)
         end2 = time.time()
         ww = ww+cur
         print(b)
         print(end2-start2)
'''

string.ascii_letters
"abcdefghijklmnopqrstuvwxyz"
ww=""
r=[]
q=[]
for z in range(1,50):
    cur = random.choice(string.ascii_letters)
    ww = ww + cur
    start2 = time.time()
    closest_words = autocorrect.get_closest_k_words(ww, 3)
    #print(len(closest_words))
   # for i in range(len(closest_words) - 1, -1, -1):
   # print(str(i + 1) + ": " + closest_words[i][0])
    end2 = time.time()
    r.append(end2-start2)
    q.append(z)
    #q.append(math.pow(z,2))

print(r)

styles = ["-"]
plt.plot(q,r)
plt.title("running time of autocorrect")
plt.xlabel('string length n')
plt.ylabel("Running time (ms)")
   #plt.ylim([0,3]) ## useful for the plot that I got.
plt.show()

'''
for j in range(10):
    start1=time.time()
    t.all_words_beginning_with_prefix(ww)
    end1=time.time()
    ww=ww+'aa'
    print(end1-start1)

print(list(t.all_words_beginning_with_prefix('a')))
print(list(t.all_words_beginning_with_prefix('aaaaa')))

plt.plot(range(100),time2)
plt.title("running time of autocomplete")
plt.xlabel('string length n')
plt.ylabel("Running time")
   #plt.ylim([0,3]) ## useful for the plot that I got.
plt.show()

s=time.time()
autocorrect.complete('als')
print(autocorrect.complete('als'))
e=time.time()
print(e-s)
print(s)
print(e)
'''