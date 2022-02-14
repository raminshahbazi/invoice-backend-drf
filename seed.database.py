# generating Countries
from core.models import Country
Country(name="England").save()
Country(name="Brazil").save()
Country(name="China").save()
Country(name="Italy").save()
Country(name="Japan").save()





# generating InvoiceTypes
from core.models import InvoiceType
InvoiceType(name="Credit Invoice").save()
InvoiceType(name="Debit Invoice").save()
InvoiceType(name="Mixed Invoice").save()
InvoiceType(name="Expense Report").save()




# generating Items
from django.contrib.auth.models import User
from core.models import Item, Country
for i in range(5):
	Item(user=User.objects.get(id=2), name=f"item {i+1} for user1 ", discount=int(i+1), base_price=int(i+1), final_price=int(i+1), manufacturing_country=Country.objects.get(pk=1)).save()

for i in range(5):
	Item(user=User.objects.get(id=3), name=f"item {i+1} for user2 ", discount=int(i+1), base_price=int(i+1), final_price=int(i+1), manufacturing_country=Country.objects.get(pk=2)).save()




# generating Invoice
from core.models import Invoice, Item, InvoiceType
from django.contrib.auth.models import User
i = Invoice(user=User.objects.get(id=3), type=InvoiceType.objects.get(id=1), description="Invoice 1 for user2")
i.save()
i.items.add(Item.objects.first())
