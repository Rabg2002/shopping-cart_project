#reciept of total amount of cart
import prods_lst
import choose_prdct


def tot_price(a):
    add=0
    for k,v in a.items():
        add+=a[k]
    tax=(15*add)/100
    amt=add+tax
    disc=(5*add)/100
    print('---------------------------')
    print("Amount = ₹",add)
    print("Tax@15% = ₹",tax)
    print("  --> Amount with tax = ₹",amt)
    print("Discount allowed@5% = ₹",disc)
    print("  --> Total amount = ₹",amt-disc)
    print('---------------------------')

if __name__=="__main__" :   
    prods_lst.new_lst(prods_lst.prod_list)
    choose_prdct.choose_product(prods_lst.prod_list)
    tot_price(choose_prdct.dict)