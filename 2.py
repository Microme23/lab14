import numpy as np
import matplotlib.pyplot as plt

x = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
y = [2356, 2110, 1182, 1895, 26161, 3863, 45293, 101431, 16675, 31532, 23356, 45981, 80776, 82755, 80363, 86811]
z = [137264, 138945, 140553, 149892, 148892, 3243, 1136, 5208, 20115, 36009, 51322, 9824, 14993, 23622, 56322, 21490]

np.array(x)
np.array(y)
np.array(z)

plt.plot(x, z, label='United Kingdom', color="green")
plt.plot(x, y, label='France', color="red")

country_input = input("Enter the country (United Kingdom('Kingdom') or France): ").capitalize()

if country_input == 'Kingdom':
    plt.bar(x, z, label=country_input, color="blue")
elif country_input == 'France':
    plt.bar(x, y, label=country_input, color="orange")
else:
    print("Invalid country input. Please choose either United Kingdom(Kingdom) or France.")
plt.title('Children out of school, primary', fontsize=15)
plt.xlabel('Year', fontsize=12, color='red')
plt.ylabel('Indicator', fontsize=12, color='red')
plt.legend()
plt.grid(True)
plt.show()