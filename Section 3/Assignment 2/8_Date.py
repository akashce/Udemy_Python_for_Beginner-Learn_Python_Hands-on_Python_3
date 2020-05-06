<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
@author: Akash

Write a Python program to read today’s date from the user and print how many days are there in the current month.
"""
d, m, y = map(int, input('Enter date in DD MM YYYY format : ').split())
mon = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
=======
# -*- coding: utf-8 -*-
"""
@author: Akash

Write a Python program to read today’s date from the user and print how many days are there in the current month.
"""
d, m, y = map(int, input('Enter date in DD MM YYYY format : ').split())
mon = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
>>>>>>> a5ccd0f74bdc9a5957d38a54bacc53b74c878979
print('Days in current month : ', mon[m])