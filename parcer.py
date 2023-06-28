import sys


def parse_input():
    question_id = 1
    lines = []

    for line in sys.stdin:
        line = line.strip()

    if lines:
        yield list(lines)



def transform_title(num, title):
    trimmed_title = title[len(str(num)):]
    return f"{num}.{trimmed_title}"


def run():
    for index, data in enumerate(parse_input()):
        title, answers = parse_question(data)
        lines = [
            transform_title(index + 1, title),
            *transform_answers(answers),
        ]

        yield "\n".join(lines)


print("\n\n".join(run()))
# print(json.dumps(output, indent=4, sort_keys=True))
