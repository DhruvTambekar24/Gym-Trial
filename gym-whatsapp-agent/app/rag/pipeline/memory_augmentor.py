def augment_with_memory(context, memory_texts):
    if not memory_texts:
        return context
    return context + "\n\nMemory:\n" + "\n".join(memory_texts)
