import openai


with open('openai.key', 'r') as f:
    openai.api_key = f.read()

# Corrects what goes into the output file with open ai
def main():
    with open('output', 'r') as f:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt='Correct this text without changing it\'s meaning:\n' + f.read() + '\ncorrection:',
            temperature=0.7,
            max_tokens=3000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        print(response.choices[0].text)


if __name__ == '__main__':
    main()
