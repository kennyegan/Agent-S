from multi_agent_qa.controller import QATestController

if __name__ == "__main__":
    prompt = "Test turning Wi-Fi off and then on"
    qa_controller = QATestController(prompt)
    qa_controller.run()           # -> prints summary
