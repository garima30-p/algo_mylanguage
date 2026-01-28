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

    # All punctuation symbols we want as separate tokens
    punctuations = "=,+-<>:"

    for char in line:
        if char == '"':
            in_quotes = not in_quotes
            current += char

        elif in_quotes:
            # Inside quotes, everything is literal
            current += char

        elif char in punctuations:
            # Flush current token before punctuation
            if current:
                tokens.append(current)
                current = ""
            # Add punctuation as its own token
            tokens.append(char)

        elif char == " ":
            # Space ends a token (outside quotes)
            if current:
                tokens.append(current)
                current = ""

        else:
            # Normal character
            current += char

    # Flush last token
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
    value_tokens = tokens[index + 1:]
    value_string = " ".join(value_tokens)
    value = parse_value(value_string)
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