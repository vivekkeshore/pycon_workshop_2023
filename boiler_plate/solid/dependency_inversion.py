# Dependency Inversion Principle
# decoupling high-level modules from low-level modules.
# High-level modules should not depend on low-level modules. Both should depend on abstractions.
# Abstractions should not depend on details. Details should depend on abstractions.


class CurrencyConvertor:
    def convert(self, from_currency, to_currency, amount):
        raise NotImplementedError


class FXConverter(CurrencyConvertor):
    def convert(self, from_currency, to_currency, amount):
        # exchange_rate = fx_api(from_cur, to_cur)
        exchange_rate = 1.2
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * exchange_rate


class XYZConverter(CurrencyConvertor):
    def convert(self, from_currency, to_currency, amount):
        # exchange_rate = xyz_rate(from_cur, to_cur)
        exchange_rate = 2.5
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * exchange_rate


class App:
    def __init__(self, converter):
        self.converter = converter

    def convert_currency(self, from_cur, to_cur, amount):
        self.converter.convert(from_cur, to_cur, amount)


fx_converter = FXConverter()
xyz_converter = XYZConverter()

app = App(fx_converter)
app.convert_currency("USD", "INR", 100)

app = App(xyz_converter)
app.convert_currency("EUR", "USD", 50)


class Appliances:
    def turn_on(self):
        raise NotImplementedError

    def turn_off(self):
        raise NotImplementedError


class LightBulb(Appliances):
    def turn_on(self):
        print("LightBulb turned on")

    def turn_off(self):
        print("LightBulb turned off")


class Refrigerator(Appliances):
    def turn_on(self):
        print("Refrigerator turned on")

    def turn_off(self):
        print("Refrigerator turned off")


class Switch:
    def __init__(self, appliance):
        self.appliance = appliance  # Removing dependency on lower module

    def on(self):
        print("Switch turned on")
        self.appliance.turn_on()

    def off(self):
        print("Switch turned off")
        self.appliance.turn_off()


light_bulb = LightBulb()
refrigerator = Refrigerator()

switch1 = Switch(light_bulb)
switch2 = Switch(refrigerator)  # Injection

switch1.on()
switch1.off()

switch2.on()
switch2.off()
