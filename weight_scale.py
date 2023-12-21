def scale():
    #lbs_to_kg = kg * lbs
    #kg_to_lbs = kg // 2.20462
    print('-------------------------------')
    print('Weight Scale')
    print('Converts weight from kilograms to Pounds and vice-vers')
    print('Kg or Lbs')
    user = input('User: ').lower()
    user_weight = float(input('weight: '))
    if user == 'kg':
        print(user_weight * 2.20462 )
        print(f'you weigh {user_weight}kg in pounds')
    else:
        if user == 'lbs':
            print(user_weight // 2.20462)
            print(f'you weigh {user_weight} in Kilogram')

    print('-------------------------------')


#scale()
