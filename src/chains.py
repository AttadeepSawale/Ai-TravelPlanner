from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from config import GOOGLE_GENAI_API_KEY

# Initialize AI Model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=GOOGLE_GENAI_API_KEY)

# Define prompt templates
travel_prompt = PromptTemplate(
    input_variables=["source", "destination"],
    template="""
    You are an AI travel assistant. Provide the most efficient travel options from {source} to {destination}.
    Include different travel modes (cab, bus, train, flight) with estimated costs, durations, and key pros/cons for each.
    Format the response clearly with bullet points or a table.
    """
)
travel_chain = LLMChain(llm=llm, prompt=travel_prompt)

tips_prompt = PromptTemplate(
    input_variables=["destination"],
    template="""
    Provide 3 essential travel tips for someone visiting {destination}.
    Ensure the tips cover safety, local customs, or budgeting for a smoother experience.
    """
)
tips_chain = LLMChain(llm=llm, prompt=tips_prompt)

best_time_prompt = PromptTemplate(
    input_variables=["destination"],
    template="""
    What is the best time to visit {destination}? Consider weather, peak tourist seasons, and major events.
    Provide a brief explanation along with recommended months.
    """
)
best_time_chain = LLMChain(llm=llm, prompt=best_time_prompt)
