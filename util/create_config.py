import yaml


def create_yaml(prompt: list[str], topics: list[str], value: str):
    data = {
        "description": "YAML_test",
        "prompts": prompt + "{{topic1}}",
        "providers": ["openai:gpt-4o"],
        "tests": [
            {
                "vars": {f"topic{i+1}": topic for i, topic in enumerate(topics)},
                "assert": [{"type": "llm-rubric", "value": value}],
            }
        ],
    }

    # 데이터를 YAML 파일로 저장
    with open("promptfooconfig.yaml", "w") as file:
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True, indent=2)

    print("YAML 파일이 생성되었습니다.")
