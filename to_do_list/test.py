import re
ceremony = input()

answer = 0

ceremony = re.sub(r'\b0+(\d)', r'\1', ceremony)

if ceremony.find('-') < 0:
  answer = eval(ceremony)
else:
  ceremony = '(' + ceremony.replace('-', ')-(') + ')'
  answer = eval(ceremony)

print(answer)
