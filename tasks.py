from crewai import Task, Crew
from agents import agent_researcher, agent_writer, agent_reviewer

def task_researcher(input: str):
    task = Task(
        description=f"Realize uma pesquisa aprofundada sobre: {input}",
        expected_output='Um resumo com as informações mais relevantes sobre o tema.',
        agent=agent_researcher
    )
    crew = Crew(agents=[agent_researcher], tasks=[task], verbose=True)
    return crew.kickoff()

def task_writer(input: str):
    task = Task(
        description=f"Com base na pesquisa abaixo, escreva um artigo claro e bem estruturado:\n\n{input}",
        expected_output='Um artigo bem escrito e informativo sobre o tema.',
        agent=agent_writer
    )
    crew = Crew(agents=[agent_writer], tasks=[task], verbose=True)
    return crew.kickoff()

def task_reviewer(input: str):
    task = Task(
        description=f"Revise o seguinte artigo, corrija erros e melhore a clareza:\n\n{input}",
        expected_output="Um artigo revisado e corrigido, pronto para publicação.",
        agent=agent_reviewer
    )
    crew = Crew(agents=[agent_reviewer], tasks=[task], verbose=True)
    return crew.kickoff()