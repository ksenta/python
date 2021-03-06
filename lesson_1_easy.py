{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Задача 1 без арифметики\n",
      "Введите любое число =113\n",
      "1\n",
      "1\n",
      "3\n",
      "Вот так все и было.\n",
      "-----------------\n",
      "Задача 1 c арифметикой\n",
      "Введите любое число =111\n",
      "1\n",
      "1\n",
      "1\n",
      "Задача 2\n",
      "Введите число А = 11\n",
      "Введите число В = 33\n",
      "Теперь А =  33\n",
      "Теперь В =  11\n",
      "-----------------\n",
      "Задача 3\n",
      "Введите ваш возраст: 11\n",
      "Извините, пользование данным ресурсом только с 18 лет\n"
     ]
    }
   ],
   "source": [
    "\n",
    "__author__ = 'Ксения Хисамутдинова'\n",
    "\n",
    "# Задача-1: Дано произвольное целое число (число заранее неизвестно).\n",
    "# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).\n",
    "# Подсказки:\n",
    "# * постарайтесь решить задачу с применением арифметики и цикла while;\n",
    "# * при желании решите задачу с применением цикла for.\n",
    "print('Задача 1 без арифметики')\n",
    "\n",
    "for s in input('Введите любое число ='):\n",
    "    print(s)\n",
    "    \n",
    "print('Вот так все и было.')\n",
    "print('-----------------')\n",
    "\n",
    "\n",
    "print('Задача 1 c арифметикой')\n",
    "\n",
    "s = input('Введите любое число =')\n",
    "s = int(s)\n",
    "while 0 < int(s):\n",
    "    print(int(s % 10))\n",
    "    s /= 10\n",
    "  \n",
    "\n",
    "# Задача-2: Исходные значения двух переменных запросить у пользователя.\n",
    "# Поменять значения переменных местами. Вывести новые значения на экран.\n",
    "# Подсказка:\n",
    "# * постарайтесь сделать решение через дополнительную переменную \n",
    "#   или через арифметические действия\n",
    "# Не нужно решать задачу так:\n",
    "# print(\"a = \", b, \"b = \", a) - это неправильное решение!\n",
    "print('Задача 2')\n",
    "a = input('Введите число А = ')\n",
    "b = input('Введите число В = ')\n",
    "a, b = b, a\n",
    "print('Теперь А = ', a)\n",
    "print('Теперь В = ', b)\n",
    "print('-----------------')\n",
    "\n",
    "# Задача-3: Запросите у пользователя его возраст.\n",
    "# Если ему есть 18 лет, выведите: \"Доступ разрешен\",\n",
    "# иначе \"Извините, пользование данным ресурсом только с 18 лет\"\n",
    "\n",
    "print('Задача 3')\n",
    "age = input('Введите ваш возраст: ')\n",
    "age = int(age)\n",
    "if age >= 18:\n",
    "    print('Доступ разрешен')\n",
    "print('Извините, пользование данным ресурсом только с 18 лет')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
