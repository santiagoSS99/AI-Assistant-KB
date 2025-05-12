from query_engine import get_response

def main():
    print("🤖 Asistente de Soporte (Claude + KB)\n")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() in ["salir", "exit", "quit"]:
            print("Adiós.")
            break
        answer = get_response(user_input)
        print(f"IA: {answer}\n")

if __name__ == "__main__":
    main()