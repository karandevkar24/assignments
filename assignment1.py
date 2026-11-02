{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4cdc824e-9e7d-4ad2-80fd-02e1bdab98d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "infix=input()\n",
    "stack=[]\n",
    "postfix=\"\"\n",
    "def precedence(op):\n",
    "  if op==\"^\":\n",
    "    return 3\n",
    "  elif op==\"*\" or op==\"/\":\n",
    "    return 2\n",
    "  elif op ==\"+\" or op==\"-\":\n",
    "    return 1\n",
    "  return 0\n",
    "for ch in infix:\n",
    "    if ch.isalnum():\n",
    "        postfix+=ch\n",
    "    elif ch==\" \":\n",
    "        continue\n",
    "    elif ch==\"(\":\n",
    "        stack.append(ch)\n",
    "    elif ch==\")\":\n",
    "        while stack and stack[-1]!=\"(\":\n",
    "            postfix+=stack.pop()\n",
    "        stack.pop()\n",
    "    else:\n",
    "        while stack and stack[-1]!=\"(\" and precedence(ch)<=precedence(stack[-1]) and ch!=\"^\":\n",
    "            postfix+=stack.pop()\n",
    "        stack.append(ch)\n",
    "while stack:\n",
    "    postfix+=stack.pop()\n",
    "print(postfix)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
