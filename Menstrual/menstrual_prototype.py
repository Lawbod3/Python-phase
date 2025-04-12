from datetime import datetime
from Menstrual.menstrual_method import menstrual_method




while True:
    while True:
        first_period = input("Enter the first day of your last period: ")
        try:
                 datetime.fromisoformat(first_period)
                 break
        except ValueError:
                 print("wrong date format, try again: ")
    while True:
        cycle_length = input("Enter the cycle length: ")
        if cycle_length.isdigit() and 21 <= int(cycle_length) <= 35:
                   break
        else:
           print("Cycle length must be a number between 21 and 35, try again.")


    while True:
        flow_length = input("How many days do you bleed: ")
        if  flow_length.isdigit() and 2 <= int(flow_length) <= 7:
           break
        else:
            print("invalid flow length, it should be between 2 and 7, try again.")

    cycle = menstrual_method(cycle_length, flow_length, first_period)

    exitApp = False
    while not exitApp:
        print('Kindly select your reason for using the App')
        print('1. Menstrual Cycle')
        print('2. Family Planing and Fertility')
        print('3. Menstrual Cycle Awareness')
        print('4. Exit')

        while True:
            try:
                choice = input("Enter your choice: ")
                if 1 <= int(choice) <= 4:
                    break
                else:
                    print("invalid choice, try again.")
            except ValueError:
                print("wrong choice, try again.")


        match choice:
            case "1":
                print(f'Your next period is likely to be {cycle.get_period_day()}')
                print(f'Your next ovulation day is likely to be {cycle.get_ovulation()}')
                print(f'Your next period is likely to End {cycle.get_end_of_cycle()}')
                print(f'Your next Pre- ovulation  is likely to be within {cycle.get_pre_ovulation()}')
                print(f'Your next Post- ovulation  is likely to be within {cycle.get_post_ovulation()}')
                break

            case "2":
                print(f'Pre- Ovulation Safe Day; Low probability of pregnancy is likely to be {cycle.get_safe_day()}')
                print(
                    f'Post- Ovulation Safe Day; Low probability of pregnancy is likely to be {cycle.get_post_ovulation_safe_day()}')
                print(
                    f'fertility - period; High probability of pregnancy is likely to be within {cycle.get_fertility_period()}')
                print(f'Ovulation; High probability of pregnancy is likely to be {cycle.get_ovulation()}')
                break

            case "3":
                print('''
             Menstrual Phase day 1-5
                          Menstrual cramps: Painful cramps in the lower abdomen or back that can last for several days.
                          You might be having slight headache during this period.
                          You might feel unusually tired.

                          Menstrual Phase day 6-13
                          Improved energy level and mood improvement.

                          Menstrual Phase day 14
                          The ovulation is likely to be within this day for 28days Cycle.

                          Menstrual Phase day 15-28
                          Breast Tenderness: Some women experience swollen, sore, or tender breasts.
                          Many women experience mood swing this period.
                          Post ovulation in some women lead to vomiting.            
             ''')
                break
            case "4":
                exitApp = True
                break

        break

    break
