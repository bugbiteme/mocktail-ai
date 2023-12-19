import os
from openai import OpenAI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel



app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Get the API key from the environment variable
#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#if not client.api_key:
#    raise ValueError("No OpenAI API key found")

# be sure to delete or comment out. for debug only
# print(client.api_key) 


# Define a request model
class RecipePrompt(BaseModel):
    prompt: str

@app.get("/")
async def usage():
    return {"message": "See /docs for API usage"}


@app.post("/generate-recipe/")
async def generate_recipe(request: RecipePrompt):
    recipe = "\nMocktail\n1. Add Water\n2. Add Ice\n3. Add a twist of this and that\n4. Enjoy your "+ request.prompt
    image_url = "https://www.cupofzest.com/wp-content/uploads/2022/03/Blue-Lagoon-Mocktail-Thumbnail-2-Web.jpg.jpg"
    return {"recipe_name": request.prompt, "recipe": recipe, "image_url": image_url} 