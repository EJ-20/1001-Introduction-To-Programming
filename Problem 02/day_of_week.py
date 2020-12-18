# Ask for user input
y = int(input('Enter the 4-digit year: '))
m = int(input('Enter the month as an integer: '))
d = int(input('Enter the day as an integer: '))
b = ""
a = ""

if m == 1 or m == 2:
	y -= 1
#Calulations
q = y//100
p = y % 100
r = ((m + 9) % 12) + 1
s = (13*r - 1)//5
t = p//4
u = q//4
v = d + p + s + t + u + 5*q
w = v % 7

#Conditionals
if m == 1:
	b = 'January'
if m == 2:
	b = 'February'
if m == 3:
	b = 'March'
if m == 4:
	b = 'April'
if m == 5:
	b = 'May'
if m == 6:
	b = 'June'
if m == 7:
	b = 'July'
if m == 8:
	b = 'August'
if m == 9:
	b = 'September'
if m == 10:
	b = 'October'
if m == 11:
	b = 'November'
if m == 12:
	b = 'December'

if w == 0:
	a = 'Sunday'
if w == 1:
	a = 'Monday'
if w == 2:
	a = 'Tuesday'
if w == 3:
	a = 'Wednesday'
if w == 4:
	a = 'Thursday'
if w == 5:
	a = 'Friday'
if w == 6:
	a = 'Saturday'

#Output
print(b,"",d,"",y,"is a ", a)
	


