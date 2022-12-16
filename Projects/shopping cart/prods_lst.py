#putting items in the dictionary

prod_list={'mango':60,'banana':40,'apple':90,'guava':50,'chick-pea':100}
def prod_lst():
    #prod_list={'mango':60,'banana':40,'apple':90,'guava':50,'chick-pea':100}
    for k,v in prod_list.items():
        print(k,":",v)
    
    print("Type 'stop' or 'STOP' for not adding products")
    while True:
        add_prod=input("Add products in the list:")
        
        if add_prod=='stop' or add_prod=='STOP':
            break
        else:
            add_price=int(input("Add price of the product:"))
            prod_list[add_prod]=add_price
    
    new_lst(prod_list)
 
def new_lst(p):           
    print()
    print("------New list of products------")
    i=1
    for k,v in prod_list.items():
        print(i,".",k,":","₹",v,)
        i+=1
        
if __name__=="__main__" :
    prod_lst()
    new_lst(prod_list)



