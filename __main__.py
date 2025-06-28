from src import * 
from src.InterfazTerminal.ControladorInterfazTerminal import ControladorInterfazTerminal
from src.InterfazTerminal.InterfazCajero import InterfazCajero
from src.InterfazTerminal.RenderizadorInterfazTerminal import RenderizadorInterfazTerminal

# datos:
# usuario: admin
# contraseña: 1234
# saldo incial: 100000 


if __name__ == "__main__":
    
    interfaz = InterfazCajero()
    renderizador = RenderizadorInterfazTerminal()
    cajeroInterfazTerminal = ControladorInterfazTerminal(interfaz, renderizador)
    cajeroInterfazTerminal.bucle_general()
    
