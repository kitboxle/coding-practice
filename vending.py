
class VendingMachine:
    def __init__(self):
        self.machine = {}
        self.balance = 0
        self.sales = 0
        self.record = [] 
        self.total_sales = {}
        self.totalqty = {}
        self.cost = {}
        self.revenue = {}

    def add_item(self, name, price, qty):
        rev = []
        stats = {}
        cost_stats = {}
        stats['price'] = price
        stats['quantity'] = qty
        cost_stats['price'] = price
        if name in self.totalqty:
            self.totalqty[name] += qty
        else:
            self.totalqty[name] = qty
        self.machine[name] = stats
        self.cost[name] = price
        self.revenue[name] = rev
        print(f'{qty} {name}(s) added to inventory')
    
    def get_item_price(self, name):
        if name not in self.machine:
            print('Invalid item')
            return None
        else:
            return self.machine[name]['price']
    
    def get_item_quantity(self, name):
        if name not in self.machine:
            print('Invalid item')
        else:
            return self.totalqty[name]
    
    def list_items(self):
        if len(self.machine) == 0:
            print('No items in the vending machine')
        else:
            print('Available items:')
            keys = list(self.machine.keys())
            keys.sort()
            sorted_machine = {i: self.machine[i] for i in keys}
            for items in sorted_machine:
                price = sorted_machine[items]['price']
                qty = self.totalqty[items]
                print(f'{items} (${price}): {qty} available')
    
    def insert_money(self, dollars):
        if dollars == 2.0 or dollars == 1.0 or dollars == 5.0:
            self.balance +=dollars
            print(f'Balance: {self.balance}')
        else:
            print('Invalid amount')

    def purchase(self, name_item):
        self.total_sales[name_item] = 0
        if name_item not in self.machine:
            print('Invalid item')
        elif name_item in self.machine and self.machine[name_item]['quantity'] == 0:
            print(f'Sorry {name_item} is out of stock')
        elif name_item in self.machine and self.machine[name_item]['quantity'] != 0 and self.balance < self.machine[name_item]['price']:
            item_price = self.machine[name_item]['price']
            print(f'Insufficient balance. Price of {name_item} is {item_price}')
        else:
            self.balance = self.balance - self.machine[name_item]['price']
            self.machine[name_item]['quantity'] -= 1
            self.sales += self.machine[name_item]['price']
            self.record.append(name_item)
            self.total_sales[name_item] += self.machine[name_item]['price']
            self.revenue[name_item].append(self.cost[name_item])
            self.totalqty[name_item] -= 1


                
            print(f'Purchased {name_item}')
            print(f'Balance: {self.balance}')
    
    def output_change(self):
        if self.balance == 0:
            print('No change')
        else:
            print(f'Change: {self.balance}')
            self.balance -= self.balance
    def remove_item(self, snack_name):
        if snack_name in self.machine:
            del self.machine[snack_name]
            print(f'{snack_name} removed from inventory')
        else:
            print('Invalid item')
    def empty_inventory(self):
        self.machine.clear()
        print('Inventory cleared') #remove later
    
    def get_total_sales(self):
        return round(self.sales, 2)
    
    def stats(self, n):
        if self.record == []:
            print('No sale history in the vending machine')
        else:
            it = []
            for goods in self.record[::-1]:
                it.append(goods)
            unique = []
            narrow = it[:n]
            co = len(narrow)
            amoun_dc = {}
            for things in narrow:
                amoun_dc[things] = narrow.count(things)
                if things not in unique:
                    unique.append(things)
            print(f'Sale history for the most recent {co} purchase(s):')
            for final in sorted(unique):
                tot_rev_lst = self.revenue[final]
                amoun = amoun_dc[final]
                tot = sum(tot_rev_lst[:-2:-1])
                print(f'{final}: ${tot:.2f} for {amoun} purchase(s)')

                
print('-----------------------------')
'''vm = VendingMachine()
vm.add_item("Bxkpnjr", 3.08, 4)
vm.add_item("Qbich", 1.38, 5)
vm.insert_money(2.00)
vm.purchase("Qbich")
vm.insert_money(2.00)
vm.insert_money(1.00)
vm.purchase("Bxkpnjr")
vm.insert_money(1.00)
vm.purchase("Qbich")
vm.empty_inventory()
vm.stats(2)'''

# Remove an item

