# Write function exclamation() that takes as input a string and returns it with this
# modification: Every vowel is replaced by four consecutive copies of itself and an exclamationmark (!) is added at the end.
# >>> exclamation('argh')
# 'aaaargh!'
# >>> exclamation('hello')
# 'heeeelloooo!'

def exclamation(string):
    # v=['a','e','i','o','u']
    # for i in string:
    #     if i in v:
    #         string=string.replace(i,i*4)
    # string+='!'
    # return string
    return ''.join(z*(4 if z.lower() in 'aeiou' else 1) for z in string)

print(exclamation('argh'))