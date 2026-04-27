import re 
import bill

h=re.compile(r'\d+\./n\w+.*/n')

s=h.findall(bill.text)