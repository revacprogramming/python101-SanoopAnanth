# Strings

text = "X-DSPAM-Confidence:    0.8475"
var=text.find(':')
flv=float(text[var+1:])
print(flv)


