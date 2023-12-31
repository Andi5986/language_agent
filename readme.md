# Language-Agent

Language-Agent is a Python package that allows for easy integration with OpenAI's GPT-4 model. The package provides a simple API to generate text completions given a user prompt.

Lanuage-Agent is perfect for developers looking to utilize OpenAI's powerful language model in their applications without the need to directly interact with OpenAI's API.

## Key Features

- Simple API for text generation
- Automatic handling of API keys through environment variables
- Easily customizable user prompt and context

## Installation

To install Lanuage-Agent, you can use pip:

```bash
 pip install language_agent
 ```

Before using the package, you'll need to set your OpenAI API key in a `.env` file:

```bash
 OPENAI_API_KEY='your-key-here' 
 ```


Make sure the `.env` file is in the root directory of your project.

## Usage

Using AI-Agent is simple. Below is a sample code snippet:

```python
from dotenv import load_dotenv
from language_agent.prompt import agent_prompt

load_dotenv()

def main():
    context = 'write the cotext i.e. you are a reviewer of an exam'
    user_input = 'Write your question to match the context'
    response = agent_prompt(context, user_input)
    print("Agent's response:", response)

if __name__ == "__main__":
    main()
```

In this example, the context and user input are combined and sent to OpenAI's GPT-4 model, which generates a text completion. The text completion is then printed to the console.

## License
Language-Agent is licensed under the terms of the MIT License.

Please note that using Language-Agent requires an API key from OpenAI, which may be subject to additional terms of use. Users are responsible for securely managing their API keys by storing them in a .env file and not sharing or exposing them in public or unsecured areas