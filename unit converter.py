def unit_converter_function():
    print('Welcome to Unit Converter:')
    print('Conversion Options:')
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3.Celsius to Fahrenheit')
    print('4. Fahrenheit to Celsius')

    while True:
        choice = input('Enter your choice (1/2/3/4): ')

        # code block for kilometers to miles conversion
        if choice == '1':
            km = float(input('Enter distance in kilometers: '))
            miles = km * 0.621371
            print(f'{km} kilometers is equal to {miles:.2f} miles.')
        
        # code block for miles to kilometers conversion    
        elif choice == '2':
            miles = float(input('Enter distance in miles: '))
            km = miles / 0.621371
            print(f'{miles} miles is equal to {km:.2f} kilometers.')
        
        # code block for Celsius to Fahrenheit conversion    
        elif choice == '3':
            celsius = float(input('Enter temperature in Celsius: '))
            fahrenheit = (celsius * 9/5) + 32
            print(f'{celsius}°C is equal to {fahrenheit}°F.')
        
        # code block for Fahrenheit to Celsius conversion    
        elif choice == '4':
            fahrenheit = float(input('Enter temperature in Fahrenheit'))
            celsius = (fahrenheit - 32) * 5/9
            print(f'{fahrenheit}°F is equal to {celsius}°C.')
         
        # exit the code   
        elif choice == 'exit':
            print('Thank you for using the Unit Converter!')
            break
            
        else:
            print('Invalid choice. please try again')


# run the program
unit_converter_function()