{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "__author__ = 'Ксения Хисамутдинова'\n",
    "\n",
    "# Задание-1:\n",
    "# Ваня набрал несколько операций в интерпретаторе и получал результаты:\n",
    "# \tКод: a == a**2\n",
    "# \tРезультат: True\n",
    "# \tКод: a == a*2\n",
    "# \tРезультат: True\n",
    "# \tКод: a > 999999\n",
    "# \tРезультат: True\n",
    "\n",
    "# Вопрос: Чему была равна переменная a,\n",
    "# если точно известно, что её значение не изменялось?\n",
    "\n",
    "# Подсказка: это значение точно есть ;)\n",
    "#1\n",
    "a = float('inf')\n",
    "\n",
    "print(a == a**2) #True\n",
    "print(a == a*2) #True\n",
    "print(a > 999999) #True\n",
    "\n",
    "# a = infinity\n",
    "# There is no way t represent infinite number as an integer. But due to Python's dynamic typing system, \n",
    "# you can use float('inf') in place of an integer, \n",
    "# and it will behave as you would expect."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
