#Input from the user
level = input('Please enter the level of your plan (Low, Regular or High): ').lower()
typeOfCoverage = input('Family or single? ').lower()


if typeOfCoverage == 'single':
    if level == 'low':
        print('Monthly payment: $36.25')
    elif level == 'regular':
        print('Monthly payment: $48.90')
    elif level == 'high':
        print('Monthly payment: $69.80')

if typeOfCoverage == 'family':
    status = (input('Children? (Yes/No) '))
        
    if level == 'low':
        if status == 'yes':
            print('Monthly payment: $98.35')
        else:
            print('Monthly payment: $56.50')
    if level == 'regular':
        if status == 'yes':
            print('Monthly payment: $136.75')
        else:
            print('Monthly payment: $74.40')
    if level == 'high':
        if status == 'yes':
            print('Monthly payment: $174.55')
        else:
            print('Monthly payment: $99.45')
        
    
    
