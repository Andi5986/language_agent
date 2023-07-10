from language_agent.prompt import agent_prompt

def main():
    context = 'You ......'
    user_input = 'Test'
    response = agent_prompt(context, user_input)
    print("Agent's response:", response)

if __name__ == "__main__":
    main()
