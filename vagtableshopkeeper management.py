username='vickyreddy'
password=123456
user=input('enter the username:')
pin=int(input('enter the  password:'))
phn_no=[]
cart=[ ]
qnty=[ ]
pay=[ ]
profit=[]
amount=0
if user==username and pin ==password:
    item=['tamato','ladysfinger','onion','potato']
    quantity=[25,10,50,30]
    price=[30,30,50,40]
    cost=[20,25,30,25]
    while True:
        are_you=input('who are you..?(owner/custmer):')
        if are_you=='owner':
            print('1.append')
            print('2.remove')
            print('3.update')
            print('4.inventry')
            print('5.report')
            print('6.itemzed profit')
            print('7.exit')
            while True:
                ask=input('what wants to do(1/2/3/4/5/6):')
                if ask== '1':
                    add=input('you want to add one more item..?(yes/no):')
                    if add=='yes':
                        what=input('what item you should add:')
                        how=float(input('how much quntity you add:'))
                        p=int(input('whats the price of item:'))
                        item.append(what)
                        quantity.append(how)
                        price.append(p)
                        print('your item  is added sucessfully:')
                elif ask=='2':
                        hey=input('you want to remove an item(yes/no):')
                        if hey=='yes':
                            v=input('what item wants to remove:')
                            idx=item.index(v)
                            item.remove(v)
                            quantity.remove(quantity[idx])
                            price.remove(price[idx])
                            print('your item  is removed sucessfully:')
                        else:
                            print('thank you')
                elif ask=='3':
                        s=input('if you wants to update(increase/decrease):')
                        if s== 'increase':
                            k=input('what should be increased(quantity/price):')
                            if k=='quantity':
                                q=input('what item quantity should be increase:')
                                if q  in item:
                                    w=item.index(q)
                                    E=int(input('how much quantity be increased:'))
                                    quantity[w]=quantity[w]+E
                                    print(quantity)
                                else:
                                    print('the  item is not avabile')
                            else:
                                r=input('what item price should be increase:')
                                if r in item:
                                    idx=item.index(r)
                                    v=int(input('how much  increase:'))
                                    price[idx]=price[idx]+v
                                    print(price)
                                else:
                                    print('the item is not avabile')
                        else:
                            k=input('what should be decreased(quantity/price):')
                            if k=='quantity':
                                q=input('what item quantity should be decreased:')
                                if q in item:
                                    w=item.index(q)
                                    E=int(input('how much quantity be decreased:'))
                                    quantity[w]=quantity[w]-E
                                    print(quantity)
                                else:
                                    print('the item isnot avabile')
                            else:
                                r=input('what item price should be decreased:')
                                if r in item:
                                    idx=item.index(r)
                                    v=int(input('how much  decrease:'))
                                    price[idx]=price[idx]-v
                                    print(price)
                                else:
                                    print('the item is not avabile')
                elif ask=='4':
                    
                    print(item)
                    print(quantity)
                    print(price)
                elif ask=='5':
                    for i in zip(cart,qnty,profit):
                        print(i)
                    print("your profit is :",profit)
                    break
                elif ask=='6':
                    for i in zip(cart,profit):
                        print(i)
                        
                    print("your profit is :",profit)
                    break
                else:
                    break
                
        #user            
        elif are_you=='custmer':
            custmername=input('enter custmername:')
            
            while True:
                customerphnno=input("enter  customer number ")
                if customerphnno.isdigit() and len(customerphnno)==10:
                    break
                else:
                    print("Give Correct Mobile Number ")
                
            if customerphnno.isdigit() and len(customerphnno)==10:
                item=['tamato','ladysfinger','onion','potato']
                quantity=[25,10,50,30]
                print(item)
                print(quantity)
                print('1.add cart')
                print('2.remove cart')
                print('3.update cart')
                print('4.view')
                print('5.billing')
                print('6.exit')
                
                while True:
                    hey=input('enter an option(1/2/3/4/5):')
                    if hey =='1':
                        
                        s=input('what items you want:')
                        if s in item:
                            cart.append(s)
                            ch=float(input('how much quantity you wants:'))
                            idx=item.index(s)
                            if ch<=quantity[idx]:
                                qnty.append(ch)
                                quantity[idx]=quantity[idx]-ch
                                amount=ch*price[idx]
                                pay.append(amount)
                                diff=[]
                                for i in range(len(price)):
                                    diff.append(price[idx]-cost[idx])
                                idx1=cart.index(s)
                                profit.append(diff[idx1]*qnty[idx1])
                               
                                print('item is added to your cart')
                            else:
                                print('the item is out of stock')
                        else:
                            print('the item is not avabile')
                           
                        
                    elif hey =='2':
                        hey=input('you want to remove an item(yes/no):')
                        if hey=='yes':
                            what=input('what item wants to remove:')
                            idx=cart.index(what)
                            if what in cart:
                                cart.remove(what)
                                amount=amount-ch*price[idx]
                                qnty.remove(qnty[idx])
                                pay.remove(pay[idx])
                                print('item is removed from your cart:')
                            else:
                                print('the item is not in cart')
                        else:
                            print('thank you')
                    elif hey=='3':
                        hey=input('you want to  update your items(yes/no):')
                        if hey =='yes':
                            s=input('if you wants to update(increase/decrease):')
                            if s=='increase':
                                what=input('what item wants to increase:')
                                if what in cart:
                                    i=cart.index(what)
                                    w=float(input('how much quantity you need to increase:')) 
                                    quantity[idx]=quantity[idx]-w
                                    qnty[i]=qnty[i]+w
                                    amount=qnty[i]+w*price[idx]
                                    pay[i]=pay[i]+w*price[idx]
                                else:
                                    print('the item not in cart')
                            else:
                                what=input('what item wants to decrease:')
                                if what in cart:
                                    i=cart.index(what)
                                    w=float(input('how much quantity you need to decrease:'))
                                    quantity[idx]=quantity[idx]+w
                                    amount=amount-w*price[idx]
                                    qnty[i]=qnty[i]-w
                                    pay[i]=pay[i]-w*price[idx]
                        else:
                            print('thank you')
                    elif hey=='4':
                        for view in zip (cart,qnty):
                            print(view[0],'----','qnty','----',view[1],sep=' ')
                            
                    elif hey=='5':
                        print('Somthing vegtable store')
                        print('Items quantity price(kg) amount')
                        for i in cart:
                            print(i,end='   ')
                            idx=cart.index(i)
                            print(qnty[idx],end='    ')
                            idx2=item.index(i)
                            print(price[idx2],end='        ')
                            v=qnty[idx]*price[idx2]
                            print(v)
                            amount=amount+v
                            print()
                        print('your total amount is ',amount)
                    else:
                        print('exit')
                        break
                
                hey=input('you want to closing the shop(yes/no):')
                if hey=='yes':
                    continue
                else:
                    for x in zip(item,quantity):
                        print(x[0], '------ ',x[1],sep=' ')
                  
                print('thank you vist again')
                break
                
           
                
            
            
           
            
        
        
            
            
            
     
           
            
      
        
                
        
       

            
                
                
                
                
                
            
           
           
                    
              
              

          
    
        
       








































        
        
    


