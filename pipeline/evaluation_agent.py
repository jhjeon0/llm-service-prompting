import dspy


class GenerateAnswer(dspy.Signature):
    """Evaluation the result to ensure given context.
    The evaluation will be 'true' or 'false'.
    The result is a boolean AND operation.
    """

    context = dspy.InputField(desc="Evaluation metrics for answer.")
    user_msg = dspy.InputField(desc="user message")
    result = dspy.InputField(desc="target")
    answer = dspy.OutputField(desc="following system prompt")


def evaluation_agent(api_key: str, user_msg: str, result: str, eval_list: list[str]):
    turbo = dspy.OpenAI(api_key=api_key, model="gpt-3.5-turbo")
    dspy.settings.configure(lm=turbo)
    generate_answer = dspy.ChainOfThought(GenerateAnswer)
    pred = generate_answer(context=eval_list, result=result, user_msg=user_msg)

    return pred
