import os
from dotenv import load_dotenv
from crewai import Agent, LLM

load_dotenv()

llm = LLM(
    model='openai/gpt-4',
    temperature=0.5,
    api_key=os.getenv('OPENAI_API_KEY')
)

# Agente pesquisador
agent_researcher = Agent(
    role='Pesquisador',
    goal='Pesquisar informações relevantes sobre o tema proposto',
    backstory='Você é um especialista em reunir dados úteis de fontes confiáveis.',
    llm=llm,
    verbose=True
)

# Agente escritor
agent_writer = Agent(
    role='Escritor',
    goal='Escrever um artigo claro e informativo baseado na pesquisa',
    backstory='Você é um redator com foco em transformar ideias em conteúdo acessível e atrativo.',
    llm=llm,
    verbose=True
)

# Agente revisor
agent_reviewer = Agent(
    role='Revisor',
    goal='Melhorar o texto final com correções gramaticais e clareza de ideias',
    backstory='Você é um editor detalhista com experiência em revisar conteúdos complexos.',
    llm=llm,
    verbose=True
)