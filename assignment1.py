infix=input()
stack=[]
postfix=""
def precedence(op):
  if op=="^":
    return 3
  elif op=="*" or op=="/":
    return 2
  elif op =="+" or op=="-":
    return 1
  return 0
for ch in infix:
    if ch.isalnum():
        postfix+=ch
    elif ch==" ":
        continue
    elif ch=="(":
        stack.append(ch)
    elif ch==")":
        while stack and stack[-1]!="(":
            postfix+=stack.pop()
        stack.pop()
    else:
        while stack and stack[-1]!="(" and precedence(ch)<=precedence(stack[-1]) and ch!="^":
            postfix+=stack.pop()
        stack.append(ch)
while stack:
    postfix+=stack.pop()
print(postfix)
