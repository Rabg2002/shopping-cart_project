#choosing products from the list of products
import prods_lst

dict={}
qty1={}
def choose_product(p):
    #dict={}
    while True:
        print('|---------------------------------|')
        slt=input(" Choose your product:")
        if slt=='q' or slt=='Q':
            break
        else:
            for k,v in p.items():
                if slt==k:
                    qty=int(input('Enter quantity from(1-10):'))
                    qty1[slt]=qty
                    dict[slt]=qty*(p[slt])
    totl_price(qty,dict,qty1)
def totl_price(qty,dict,qty1):                   
    print()
    print('-----List of your choosen products-----')
    a=1
    for i,g in dict.items():
        print(a,'.',i,'*',qty1[i],'= ₹',g)
        a+=1

choose_product(prods_lst.prod_list)
