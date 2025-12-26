from address import Address
from mailing import Mailing


to_address = Address("453560", "Инзер", "Котовского", "19", "24")
from_address = Address("453570", "Межгорье", "Пушкина", "30", "13")


mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=500,
    track="TR3412DFG56789"
)

print(mailing)
