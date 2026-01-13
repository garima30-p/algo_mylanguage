# --- ALGO Minimal Interpreter ---
import sys

ACTIONS = {
    "show": "OUTPUT",
    "write": "OUTPUT",
    "print": "OUTPUT",
    "display": "OUTPUT",
}

def tokenize(line):
    tokens = []
    current = ""
    in_quotes = False

    for char in line:
        if char == '"':
            in_quotes = not in_quotes
            current += char

        elif char == " " and not in_quotes:
            if current:
                tokens.append(current)
                current = ""
        else:
            current += char

    if current:
        tokens.append(current)

    return tokens

def detect_action(tokens):
    for t in tokens:
        if t in ACTIONS:
            return ACTIONS[t], t
    return None, None

def parse_value(token):
    # If it's quoted, remove quotes
    if token.startswith('"') and token.endswith('"'):
        return token[1:-1]
    return token

def execute_output(tokens, action_word):
    index = tokens.index(action_word)
    value_token = tokens[index + 1]
    value = parse_value(value_token)
    print(value)


def run(program_text):
    for line in program_text.split("\n"):
        tokens = tokenize(line)
        action, action_word = detect_action(tokens)

        if action == "OUTPUT":
            execute_output(tokens, action_word)
        else:
            print(f"Unknown instruction: {line}")

# --- Entry Point ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python interpreter.py <filename.garima>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename) as f:
        program = f.read()

    run(program)