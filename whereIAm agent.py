
# Import necessary libraries
import random
from smolagents import CodeAgent, DuckDuckGoSearchTool, AzureOpenAIServerModel

from smolagents import Tool
import random
import requests

class WeatherInfoTool(Tool):
    name = "weather_info"
    description = "Fetches real-time weather information for a given location using OpenWeatherMap API."
    inputs = {
        "location": {
            "type": "string",
            "description": "The location to get weather information for."
        }
    }
    output_type = "string"

    def __init__(self):
        super().__init__()
        # self.api_key = api_key

    def forward(self, location: str):
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid=""&units=metric"
            response = requests.get(url)
            data = response.json()

            if response.status_code != 200 or 'main' not in data:
                return f"Error fetching weather for {location}: {data.get('message', 'Unknown error')}"

            temp = data['main']['temp']
            condition = data['weather'][0]['description'].capitalize()
            return f"Weather in {location}: {condition}, {temp}°C"
        
        except Exception as e:
            return f"Error fetching weather: {str(e)}"

# Initialize the tool
weather_info_tool = WeatherInfoTool()


import datasets
from langchain.docstore.document import Document
from smolagents import Tool
from langchain_community.retrievers import BM25Retriever

class GuestInfoRetrieverTool(Tool):
    """Tool for retrieving guest information from the dataset."""
    name = "guest_info_retriever"
    description = "Retrieves detailed information about gala guests based on their name or relation."
    inputs = {
        "query": {
            "type": "string",
            "description": "The name or relation of the guest you want information about."
        }
    }
    output_type = "string"

    def __init__(self, docs):
        self.retriever = BM25Retriever.from_documents(docs)

    def forward(self, query: str):
        results = self.retriever.get_relevant_documents(query)
        if results:
            return "\n\n".join([doc.page_content for doc in results[:3]])
        return "No matching guest information found."

def load_guest_dataset():
    """Load and prepare the guest dataset with the retrieval tool."""
    # Load the dataset
    guest_dataset = datasets.load_dataset("agents-course/unit3-invitees", split="train")
    
    # Convert dataset entries into Document objects
    docs = [
        Document(
            page_content="\n".join([
                f"Name: {guest['name']}",
                f"Relation: {guest['relation']}",
                f"Description: {guest['description']}",
                f"Email: {guest['email']}"
            ]),
            metadata={"name": guest["name"]}
        )
        for guest in guest_dataset
    ]
    
    # Initialize and return the tool
    return GuestInfoRetrieverTool(docs)



# Set up the Azure OpenAI model
model = AzureOpenAIServerModel(
    model_id="",
    azure_endpoint="",
    api_key="",
    api_version=""
)


# Initialize the web search tool
search_tool = DuckDuckGoSearchTool()

# Initialize the weather tool
weather_info_tool = WeatherInfoTool()


guest_info_tool = load_guest_dataset()

alfred = CodeAgent(
    tools=[guest_info_tool, weather_info_tool, search_tool], 
    model=model,
    add_base_tools=True,  
    planning_interval=3   
)



query = "Tell me about halish ricard J and he's  Location and  climate"
response = alfred.run(query)

print("AI Response:")
print(response)





