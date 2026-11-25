# 초안: 단계만 정의해 둔 뼈대입니다.
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict, total=False):
    inquiries: list[str]
    classified: list[dict]
    summaries: dict[str, str]
    approved: bool


def load(state: State):      return {"inquiries": []}           # TODO: 주간 문의 CSV
def classify(state: State):  return {"classified": []}          # TODO: 14회차 /classify 호출
def summarize(state: State): return {"summaries": {}}           # TODO: 부서별 요약 Agent
def approve(state: State):   return {"approved": False}         # TODO: interrupt 승인


g = StateGraph(State)
for name, fn in [("load", load), ("classify", classify), ("summarize", summarize), ("approve", approve)]:
    g.add_node(name, fn)
g.add_edge(START, "load"); g.add_edge("load", "classify"); g.add_edge("classify", "summarize")
g.add_edge("summarize", "approve"); g.add_edge("approve", END)
graph = g.compile()
