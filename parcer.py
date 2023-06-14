import sys


def parse_input():
    question_id = 1
    lines = []

    for line in sys.stdin:
        line = line.strip()

        if line.startswith(str(question_id + 1) + " ") or line == str(question_id + 1):
            question_id += 1
            yield list(lines)
            lines = []

        lines.append(line)

    if lines:
        yield list(lines)


def parse_answers(question):
    lines = []
    reversed_question = question[::-1]
    i = 0
    counter = 0

    while i < len(question):
        line = reversed_question[i]
        prev_line = reversed_question[i + 1] if i + 1 < len(question) else None

        if line == '' or line.endswith(":") or line.endswith("?"):
            # End of answers
            if counter > 0:
                break

        if line and line != "```":
            lines.append(line)

            if not is_joinable(line, prev_line):
                yield " ".join(lines[::-1])
                lines = []
                counter += 1

        i += 1

    if lines:
        yield " ".join(lines[::-1])



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
