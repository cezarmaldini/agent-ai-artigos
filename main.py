from graph import build_graph

if __name__ == "__main__":
    flow = build_graph()

    # Estado inicial com o tema do artigo
    initial_state = {
        "topic": "Primeiros passos na utilização do CrewAI para criação de agentes de IA"
    }

    # Executa o fluxo completo
    result = flow.invoke(initial_state)

    # Exibe o resultado final do artigo
    print("\n✅ Artigo Final Revisado:\n")
    print(result["final_article"])