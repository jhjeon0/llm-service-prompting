from pipeline.generate_system_prompt import generate_system_prompt
from pipeline.generate_agent import run
from pipeline.evaluation_agent import evaluation_agent
from pipeline.regenerate_agent import regenerate_agent


api_key = ""

# user input
user_context = ["검색엔진에 효율적으로 검색하기 위한 단어 1개만을 추출해야 한다."]
eval_list = [
    "Check if the given {result} is a single word.",
    "Check if the given {result} is a keyword",
]
question = "요즘 박스오피스에는 흥미가 안생긴다."


def _recursive(system_prompt):
    # system prompt 생성

    # 답변
    answer = run(system_prompt=system_prompt, user_content=question, api_key=api_key)
    print("답변:: ", answer)
    # 검증
    evaluation = evaluation_agent(user_msg=question, result=answer, eval_list=eval_list)
    print(evaluation.answer)
    # print(evaluation.rationale)
    if evaluation.answer in ["true", "True"]:
        print(system_prompt)
        print("'Done'")

    else:

        system_prompt = regenerate_agent(
            context=user_context, reason=evaluation.rationale, api_key=api_key
        )
        print("-" * 40)
        print("system_prompt:: ", system_prompt)
        # answer = run(system_prompt=system_prompt, user_content=question)
        # evaluation = evaluation_agent(user_msg=question, result=answer, eval_list=eval_list)
        # print("'modified'", system_prompt)
        _recursive(system_prompt)


_recursive(generate_system_prompt(context=user_context, api_key=api_key))
