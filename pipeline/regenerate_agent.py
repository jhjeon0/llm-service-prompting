import dspy


class GenerateAnswer(dspy.Signature):
    """
    Make instruction based on reason and context
    """

    context = dspy.InputField(desc="may contain requirements")
    reason = dspy.InputField()
    question = dspy.InputField()
    answer = dspy.OutputField(desc="satisfying every context")


def regenerate_agent(context: str, reason: str, api_key: str):
    turbo = dspy.OpenAI(model="gpt-3.5-turbo", api_key=api_key, temperature=0.35)
    dspy.settings.configure(lm=turbo)

    generate_answer = dspy.ChainOfThought(GenerateAnswer)
    pred = generate_answer(context=context, reason=reason, question="based on context")
    # print(turbo.inspect_history(1))
    # print(pred.answer)
    return pred.answer
