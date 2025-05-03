import os
from jinja2 import Environment, FileSystemLoader

dir_path = os.path.dirname(os.path.realpath(__file__))

env = Environment(loader=FileSystemLoader(dir_path))

available_agents_template = env.get_template("available_agents_prompt.jinja")
agent_selector_template = env.get_template("agent_selector.jinja")


if __name__ == "__main__":
    available_agents_prompt = available_agents_template.render(
        agents=[
            {"name": "Agent 1", "description": "Agent 1 description", "skills": [{"name": "Skill 1", "description": "Skill 1 description", "examples": ["Example 1", "Example 2"]}]},
            {"name": "Agent 2", "description": "Agent 2 description", "skills": [{"name": "Skill 2", "description": "Skill 2 description", "examples": ["Example 3", "Example 4"]}]},
        ]
    )

    prompt = agent_selector_template.render(
        question="How is Thai stock market this week?",
        available_agents_prompt=available_agents_prompt
    )

    print(prompt)
