from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Union, Optional


# True = Accepted, False = Rejected
# str = jump
# None = next item in list

class WorkflowItem(ABC):

    @abstractmethod
    def check_workflow(self, rating: dict[str, int]) -> Optional[Union[str, bool]]:
        pass


class JumpPoint(WorkflowItem):
    jump_to: Optional[Union[str, bool]]

    def __init__(self, in_str: str):
        # check if accept or reject
        if in_str == "A":
            self.jump_to = True
        elif in_str == "R":
            self.jump_to = False
        else:
            self.jump_to = in_str

    def check_workflow(self, rating: dict[str, int]) -> Optional[Union[str, bool]]:
        return self.jump_to


class Comparison(WorkflowItem):
    slt: bool
    operate_on: str
    compare_val: int
    action: Optional[Union[str, bool]]

    def __init__(self, in_str: str):
        right_str = ""

        # less than
        if "<" in in_str:
            self.slt = True
            self.operate_on, right_str = in_str.split("<")
        else:
            self.slt = False
            self.operate_on, right_str = in_str.split(">")

        raw_comp_val, raw_action = right_str.split(":")

        self.compare_val = int(raw_comp_val)

        if raw_action == "A":
            self.action = True
        elif raw_action == "R":
            self.action = False
        else:
            self.action = raw_action

    def check_workflow(self, rating: dict[str, int]) -> Optional[Union[str, bool]]:
        if self.slt and rating[self.operate_on] < self.compare_val:
            return self.action
        elif not self.slt and rating[self.operate_on] > self.compare_val:
            return self.action
        else:
            return None


def break_down_xmas_string(in_str: str) -> list[dict[str, int]]:
    ratings = []

    for row in in_str.split("\n"):
        row = row.strip("{}")

        rating = dict()
        for element in row.split(","):
            l, r = element.split("=")
            rating[l] = int(r)

        ratings.append(rating)

    return ratings


def break_down_workflows(in_str: str) -> dict[str, list[WorkflowItem]]:
    workflows = dict()

    for wf_row in in_str.split("\n"):
        key, raw_wfs = wf_row.split("{")
        raw_wfs = raw_wfs.strip("}")
        wf_list = []

        for wf in raw_wfs.split(","):
            if ">" in wf or "<" in wf:
                wf_list.append(Comparison(wf))
            else:
                wf_list.append(JumpPoint(wf))

        workflows[key] = wf_list

    return workflows


def workflow_handler(curr_list: list[WorkflowItem], workflow_directory: dict[str, list[WorkflowItem]], part: dict[str, int]) -> bool:
    for wf_item in curr_list:
        val = wf_item.check_workflow(part)

        # accept / reject
        if type(val) is bool:
            return val

        # jump to other list
        elif type(val) is str:
            return workflow_handler(workflow_directory[val], workflow_directory, part)

def main():
    workflows, ratings = open("data.txt").read().split("\n\n")

    workflows = break_down_workflows(workflows)
    ratings = break_down_xmas_string(ratings)

    score = 0

    for part in ratings:
        if workflow_handler(workflows["in"], workflows, part):
            score += sum(part.values())

    print(score)


if __name__ == '__main__':
    main()
