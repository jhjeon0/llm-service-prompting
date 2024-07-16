"""Auto create system prompt"""

from pipeline.pipeline import pipeline


user_input = []
question = []

if __name__ == "__main__":
    pipeline(requirements=user_input, question=question)
