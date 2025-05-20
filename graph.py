from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
from tasks import task_researcher, task_writer, task_reviewer

class ArticleState(TypedDict):
    topic: Optional[str]
    research: Optional[str]
    article: Optional[str]
    final_article: Optional[str]

# Nó: Recebe o tema inicial
def receive_topic_step(state: ArticleState) -> ArticleState:
    return {"topic": state["topic"]}

# Nó: Pesquisa o tema
def research_task_step(state: ArticleState) -> ArticleState:
    topic = state["topic"]
    result = task_researcher(topic)
    return {"research": result}

# Nó: Redige o artigo
def writing_task_step(state: ArticleState) -> ArticleState:
    article = task_writer(state["research"])
    return {"article": article}

# Nó: Revisa o artigo final
def review_task_step(state: ArticleState) -> ArticleState:
    final_article = task_reviewer(state["article"])
    return {"final_article": final_article}

# Cria o grafo do fluxo
# === Fluxo completo: pesquisa -> redação -> revisão ===
def build_graph():
    graph = StateGraph(ArticleState)

    graph.add_node("receive_topic", receive_topic_step)
    graph.add_node("research_task", research_task_step)
    graph.add_node("writing_task", writing_task_step)
    graph.add_node("review_task", review_task_step)

    graph.set_entry_point("receive_topic")
    graph.add_edge("receive_topic", "research_task")
    graph.add_edge("research_task", "writing_task")
    graph.add_edge("writing_task", "review_task")
    graph.add_edge("review_task", END)

    return graph.compile()