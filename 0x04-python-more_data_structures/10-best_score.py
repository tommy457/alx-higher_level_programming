#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        return sorted(a_dictionary.items(), key=lambda item: item[1])[-1][0]
    return None
