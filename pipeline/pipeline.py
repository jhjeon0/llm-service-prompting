import os
from pipeline.generate_system_prompt import generate_system_prompt
from pipeline.create_evaluation import evaluation_agent
from pipeline.regenerate_agent import regenerate_agent
from util.create_config import create_yaml
from util.read_output import read_output


def pipeline(requirements: list[str], question: list[str]):
    system_prompt = generate_system_prompt(requirements)
    evaluations = evaluation_agent(system_prompt)

    # 평가 -> promptfoo, promptfoo yml 생성
    create_yaml(system_prompt, question, evaluations)
    os.system("npx promptfoo@latest eval -o output.json")

    json_data = read_output()
    if json_data["results"]["results"][0]["gradingResult"]["pass"]:
        return system_prompt

    else:
        reason = json_data["results"]["results"][0]["gradingResult"]["reason"]
        system_prompt = regenerate_agent(context=requirements, reason=reason)
        pipeline(system_prompt, question)
