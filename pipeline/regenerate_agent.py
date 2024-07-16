import os
import dspy


class GenerateAnswer(dspy.Signature):
    """
    Create an instruction based on the given requirements and reason.
    """

    context = dspy.InputField(desc="requirements")
    reason = dspy.InputField()
    question = dspy.InputField()
    answer = dspy.OutputField(desc="system prompt")


def regenerate_agent(question: list[str], reason: str):
    turbo = dspy.OpenAI(
        model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"), temperature=0.35
    )
    dspy.settings.configure(lm=turbo)

    generate_answer = dspy.ChainOfThought(GenerateAnswer)
    pred = generate_answer(
        context=question[0], reason=reason, question="based on context"
    )

    return pred.answer
