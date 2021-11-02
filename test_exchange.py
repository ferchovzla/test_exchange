import random

def calculate(denominations):
   print("\n")
   print("#############################\n")
   for key in denominations:
      #print(key, '->', denominations[key]) 
      amount = int(denominations[key][0])
      deno = denominations[key][1].split()
      deno = [int(d) for d in deno]      
      deno.sort(reverse=True)
      print("Amount: {} \n".format(amount))
      quantity = 0
      for i in deno:      
         if(amount >= i):
            rest = int(amount / i)
            quantity = rest + quantity
            print("Give "+str(rest) + " coins "+str(i))
            amount = amount % i

      print("Total: {} coins".format(quantity))
      print("#############################\n")


print("Enter the number of iterations")
number_iterations = int(input())

deno = {}
values = []
for i in range(0,number_iterations):
    print("<<<<<<<<< Iteration {} >>>>>>>>>".format(i+1))
    print(" - Enter the Value ---> 1<= Value <= 100")
    value = input()
    print(" - Enter the denominations (#denominations <= 10 ). Example: 1 2 5 10 20")
    deno[i] = [value, input()]

#print(deno)    
    
#deno = [1,2,5,10,15,20,50]
#deno.sort(reverse=True)
#print(type(deno))
#amount = 1347

calculate(deno)
