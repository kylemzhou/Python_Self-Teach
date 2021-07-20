if question == 'no':
            while loop:
                category = input("What is new category?: \n")
                category = category[0].upper() + category[1:].lower()
                price = float(input("How much money do you spent in this category?: \n"))
                Receipts(category,price).add_obj_category()
                break
            loop = False