class Nodo:
    def __init__(self, valor, next=None):
        self.valor = valor
        self.next = next

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def agregar_ultimo(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            nuevo_nodo.next = self.cabeza
        else:
            ultimo_nodo = self.cabeza
            while ultimo_nodo.next != self.cabeza:
                ultimo_nodo = ultimo_nodo.next
            ultimo_nodo.next = nuevo_nodo
            nuevo_nodo.next = self.cabeza

    def eliminar_ultimo(self):
        if self.cabeza is None:
            return None
        elif self.cabeza.next == self.cabeza:
            valor = self.cabeza.valor
            self.cabeza = None
            return valor
        else:
            ultimo_nodo = self.cabeza
            while ultimo_nodo.next.next != self.cabeza:
                ultimo_nodo = ultimo_nodo.next
            valor = ultimo_nodo.next.valor
            ultimo_nodo.next = self.cabeza
            return valor

    def lista_vacia(self):
        return self.cabeza is None

    def agregar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            nuevo_nodo.next = self.cabeza
        else:
            nuevo_nodo.next = self.cabeza
            ultimo_nodo = self.cabeza
            while ultimo_nodo.next != self.cabeza:
                ultimo_nodo = ultimo_nodo.next
            ultimo_nodo.next = nuevo_nodo
            self.cabeza = nuevo_nodo

    def eliminar_inicio(self):
        if self.cabeza is None:
            return None
        elif self.cabeza.next == self.cabeza:
            valor = self.cabeza.valor
            self.cabeza = None
            return valor
        else:
            valor = self.cabeza.valor
            ultimo_nodo = self.cabeza
            while ultimo_nodo.next != self.cabeza:
                ultimo_nodo = ultimo_nodo.next
            self.cabeza = self.cabeza.next
            ultimo_nodo.next = self.cabeza

try:
    if  __name__ == "__main__":
        opcion = 0
        lista_circular = ListaCircular()
        while opcion != 6:
            opcion = int(input("\nMenú de opciones:\n1. Agregar al final\n2. Eliminar del final\n3. Verificar si la lista está vacía\n4. Agregar al inicio\n5. Eliminar del inicio\n6. Salir\nSelecciona una opción: "))
            if opcion == 1:
                valor = input("Ingresa el valor a agregar: ")
                lista_circular.agregar_ultimo(valor)
                print("Valor agregado exitosamente.")
            elif opcion == 2:
                valor = lista_circular.eliminar_ultimo()
                if valor is None:
                    print("La lista está vacía.")
                else:
                    print("Valor eliminado:", valor)
            elif opcion == 3:
                vacia = lista_circular.lista_vacia()
                if vacia:
                    print("La lista está vacía.")
                else:
                    print("La lista no está vacía.")
            elif opcion == 4:
                valor = input("Ingresa el valor a agregar: ")
                lista_circular.agregar_inicio(valor)
                print("Valor agregado exitosamente.")
            elif opcion == 5:
                valor = lista_circular.eliminar_inicio()
                if valor is None:
                    print("La lista está vacía.")
                else:
                    print("Valor eliminado:", valor)
            elif opcion == 6:
                print("Adiós.")
                break
            else:
                print("Opción inválida, selecciona una opción válida.")
except Exception as e:
    print(e)