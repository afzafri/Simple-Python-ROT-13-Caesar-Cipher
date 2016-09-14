#dictionary for decode and encode
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b','p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m'}

userinput = raw_input("\nPlease enter the text you want to Encode/Decode: ").lower() #ask user input, and change to lowercase

#new string
decoded = ""

#for loop, guna dictionary, dan append masuk string baru
#check kalau character tu wujud dalam dictionary, daptkan value dari dictionary, dan masukkan ke dalam string baru tu
#kalau xda dalam dictionary, masukkan terus value asal ke dalam string baru tu
for i in userinput:
    if i in key:
        decoded += key[i]
    else:
        decoded += i

#output
print "\nResult: ",decoded
