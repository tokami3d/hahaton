from haha1 import  list_of_products, delete_product,detail_product,craete_product,update_product

def main():
    print('привет тебе доступны следузие функции марсель маркета:\n\tLIST-1\n\tDETEIL-2\n\tCREATE -3\n\tUPDATE-4\n\tDELETE-5')
    choise = input('введите действие(1,2,3,4,5:')
    if choise.strip() == '1':
        print(list_of_products())
    elif choise.strip() == '2':
        print(detail_product())
    elif  choise.strip() == '3':
        print(craete_product())
    elif choise.strip() == '4':
        print(update_product())
    elif choise.strip() == '5':
        print(delete_product())
    else:
        print('неверный выбор')
    
    answer = input('хотите прожодить? yes/no')
    if answer.lower().strip() =='yes':
        main()
    else:
        print('bay bay buch')



main()
