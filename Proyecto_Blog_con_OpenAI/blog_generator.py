#Import the open ai package
import openai
#Import the dotenv values ​​module from the dotenv package to secure our password
from dotenv import dotenv_values
#Instantiate object in the "config" variable
config = dotenv_values(".env")
#Place the API key that we configured with the dotev_values ​​module
openai.api_key = config['API_KEY']
#"generated_poem" function with 2 parameters.
def generate_poem(topic, style=""):
  #Our first promt will consult the topic of the poem to chatgpt
  prompt = f'Write a poem on the following {topic} '
  #Our second prompt will add the style and query chatgpt, this will happen in case the user enters a style
  if style:
    prompt += f'and with the following {style} '
  #We call the "create" method inside the "openai.completions" object, and specify the attributes (model, prompt, max token and temperature)
  response = openai.completions.create(
    model = 'gpt-3.5-turbo-instruct',
    prompt = prompt,
    max_tokens = 300,
    temperature = 0.7
  )
  #We finish the function, extracting only the text that chatgpt gives us.
  retrieve_blog = response.choices[0].text
  #We return the response "retrieve_blog"
  return retrieve_blog
#we create a boolean flag "keep_writing"
keep_writing = True
#While loop with the flag as a parameter
while keep_writing:
  #Asks if the user wants to create the poem
  answer = input('Write a poem? Y for yes, anything else for no. ')
  #If you enter "Y", we take the values ​​entered by the user and pass them as arguments in the call to the "generate_poem()" function.
  if (answer == 'Y'):
    poem_topic = input('What should this paragraph talk about? ')
    poem_style= input('What style of poem do you want? (sonnet, romantic, haiku, free verse, or leave blank for a general style) ')
    print('*******************POEM*********************')
    print(generate_poem(poem_topic, poem_style))
    print('*******************************************')
  #Otherwise, the boolean flag becomes false and nothing is done.
  else:
    keep_writing = False