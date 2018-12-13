
def unique_chain(*iterables):
    known_ids = set()
    for it in iterables:
        for element in it:
            if element.id not in known_ids:
                known_ids.add(element.id)
                yield element
