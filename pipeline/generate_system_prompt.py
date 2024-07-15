import dspy


class GenerateAnswer(dspy.Signature):
    """
    Make instruction based on context
    """

    context = dspy.InputField(desc="may contain requirements")
    question = dspy.InputField()
    answer = dspy.OutputField(desc="satisfying every context")


def generate_system_prompt(context: list[str], api_key):
    turbo = dspy.OpenAI(model="gpt-3.5-turbo", api_key=api_key, temperature=0.35)
    dspy.settings.configure(lm=turbo)
    generate_answer = dspy.ChainOfThought(GenerateAnswer)
    pred = generate_answer(context=context, question="based on context")
    # print(turbo.inspect_history(1))
    print("base_system_prompt:: ", pred.answer)
    return pred.answer
