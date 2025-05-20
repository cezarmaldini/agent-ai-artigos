from graph import build_graph

if __name__ == "__main__":
    flow = build_graph()

    # Estado inicial com o tema do artigo
    initial_state = {
        "topic": "Uso da inteligência artificial na área da saúde."
    }

    # Executa o fluxo completo
    result = flow.invoke(initial_state)

    # Exibe o resultado final do artigo
    print("\n✅ Artigo Final Revisado:\n")
    print(result["final_article"])