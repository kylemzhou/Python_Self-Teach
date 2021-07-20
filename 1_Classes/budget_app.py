'''
This is the first project for Classes! Specifically, it is
a budget app to keep track of expenses.
'''

class Receipts:

    def __init__(self,category,cost):
        self.category = category 
        self.cost = cost
    
    def obj_category(self,obj_dict = {}):
        obj_dict[self.category] = self.cost
    
    def get_obj_category(self):
        return obj_dict

    def __str__(self):
        return str("\nYou have spent $%s on %s." %(
            "%.2f" % self.cost, 
            self.category,
            )
        )


def main():
    loop = True

    while loop:
        category = input("What is the category?: \n")
        category = category[0].upper() + category[1:].lower()
        price = float(input("How much money do you spent in this category?: \n"))
        question = input("Is that all for the receipt? ").lower()
        if question == 'yes':
            encap = Receipts(category,price)
            loop = False
        if question == 'no':
            Receipts(category,price)
            continue
    
    print(encap.obj_category())

if __name__ == "__main__":
    main()