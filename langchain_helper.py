
import os
from secrete import openapi_key
os.environ['OPENAI_API_KEY'] = openapi_key

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

llm=OpenAI(temperature=0.6)



def gen_res_name_and_items(cuisine):
    #Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest me a fancy name for this.")
    # prompt_template_name.format(cuisine="Italian")

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")
    #Chain 2: Menu items

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. return it as a comma separated list")
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    from langchain.chains import SequentialChain
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )
    response= chain({'cuisine':cuisine})
    return response

if __name__=="__main__":
    print(gen_res_name_and_items("Italian"))