def formatter(symbol, text):
    # Getting width of sides
    sides = symbol * 3
    # putting the symbol on the text sides
    formatted_text = f"{sides} {text} {sides}"
    # Getting the symbol above and below the text
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"

print(formatter("*", "Test"))