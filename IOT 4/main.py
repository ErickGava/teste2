from database import Pizza

def main():
    pizza = Pizza()
    pizza.adicionar_pizza("Diavola", "medias", 40.00)
    pizza.listar_pizzas()

if __name__ == "__main__":
    main()