from spyne import rpc, ServiceBase

class Converter(ServiceBase):
    @rpc(float, _returns=float)
    def celsius_to_fahrenheit(ctx, celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    
    @rpc(float, _returns=float)
    def celsius_to_kelvin(ctx, celsius):
        kelvin = celsius + 273.15
        return kelvin

    @rpc(float, _returns=float)
    def fahrenheit_to_celsius(ctx, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    
    @rpc(float, _returns=float)
    def fahrenheit_to_kelvin(ctx, fahrenheit):
        kelvin = (fahrenheit - 273.15) * 9/5 + 32
        return kelvin
    
    @rpc(float, _returns=float)
    def kelvin_para_fahrenheitx(ctx, kelvin):
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        return fahrenheit
    
    @rpc(float, _returns=float)
    def kelvin_para_celsius(ctx, kelvin):
        celsius = kelvin - 273.15
        return celsius
