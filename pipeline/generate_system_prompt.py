import os
import dspy


class GenerateAnswer(dspy.Signature):
    """
    Create an instruction based on the given requirements.
    """

    context = dspy.InputField(desc="requirements")
    question = dspy.InputField(desc="")
    answer = dspy.OutputField(desc="system prompt")


def generate_system_prompt(question: list[str]):
    turbo = dspy.OpenAI(
        model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"), temperature=0.35
    )
    dspy.settings.configure(lm=turbo)

    generate_answer = dspy.ChainOfThought(GenerateAnswer)
    pred = generate_answer(context=question[0], question="시스템 프롬프트를 만들어줘")

    return pred.answer
