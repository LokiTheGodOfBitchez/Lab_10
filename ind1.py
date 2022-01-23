#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")
    a = {"a", "e", "g", "o", "p"}
    b = {"e", "h", "i", "o", "u"}
    c = {"g", "h", "p", "s", "t", "w"}
    d = {"f", "h", "n", "s", "t", "x", "y"}

    not_a = u - a
    not_b = u - b

    x = (a - c) & not_b
    y = (not_a & d) | (c - d)

    print(f"x = {x}")
    print(f"y = {y}")
    