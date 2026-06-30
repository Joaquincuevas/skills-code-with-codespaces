def mostrar_menu():
	print("=== MENU DE MEMES ===")
	print("1. Meme de risa")
	print("2. Meme de enojo")
	print("3. Meme de sorpresa")
	print("4. Meme de tristeza")
	print("5. Salir")


def obtener_meme(opcion):
	memes = {
		"1": "Meme de risa: jajaja, esto estuvo bueno.",
		"2": "Meme de enojo: no me gustó nada.",
		"3": "Meme de sorpresa: no me lo esperaba.",
		"4": "Meme de tristeza: qué sad.",
	}
	return memes.get(opcion, "Opción no válida. Elige un número del 1 al 5.")


def main():
	mostrar_menu()
	opcion = input("Elige una opción: ")

	if opcion == "5":
		print("Saliendo del programa...")
	else:
		print(obtener_meme(opcion))


if __name__ == "__main__":
	main()
