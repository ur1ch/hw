"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):    
    print('Low Fuel Level Error')

class NotEnoughFuel(Exception):    
    print('Not Enough Fuel')

class CargoOverload(Exception):    
    print('Cargo Overload')