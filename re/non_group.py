#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Function:
【教程】详解Python正则表达式之： (?:…) non-capturing group 非捕获组
https://www.crifan.com/detailed_explanation_about_python_regular_express_non_capturing_group/

Version:    2013-09-06
Author:     Crifan Li
Contact:    https://www.crifan.com/about/me/
"""

import re


def python_re_non_capturing_group():
    """
        demo Pyton non-capturing group
    """
    inputStr = "hello 123 world 456 nihao 789";
    rePatternAllCapturingGroup =     "\w+ (\d+) \w+ (\d+) \w+ (\d+)"
    rePatternWithNonCapturingGroup = "\w+ (\d+) \w+ (?:\d+) \w+ (\d+)"
    print("inputStr=", inputStr)
    print("rePatternAllCapturingGroup=", rePatternAllCapturingGroup)
    print("rePatternWithNonCapturingGroup=", rePatternWithNonCapturingGroup)
    print("--- 1. show normal case, all captured group ---")
    foundDigitsAllCapturingGroup = re.search(rePatternAllCapturingGroup, inputStr)
    if (foundDigitsAllCapturingGroup):
        firstGroup = foundDigitsAllCapturingGroup.group(1)
        print("firstGroup=", firstGroup)  # firstGroup= 123
        secondGroup = foundDigitsAllCapturingGroup.group(2)
        print("secondGroup=", secondGroup) # secondGroup= 456
        thirdGroup = foundDigitsAllCapturingGroup.group(3)
        print("thirdGroup=", thirdGroup)  # thirdGroup= 789
    print("--- 2. show with non-capturing group ---")
    foundDigitsWithNonCapturingGroup = re.search(rePatternWithNonCapturingGroup, inputStr)
    if (foundDigitsWithNonCapturingGroup):
        firstGroup = foundDigitsWithNonCapturingGroup.group(1)
        print("firstGroup=", firstGroup)  # firstGroup= 123
        secondGroup = foundDigitsWithNonCapturingGroup.group(2)
        print("secondGroup=", secondGroup)  # secondGroup= 789
        # thirdGroup = foundDigitsWithNonCapturingGroup.group(3); # will error -> IndexError: no such group
        print("""Explains:
1. for second group (?:\d+),
is something like (?:xxx)
is a non-capturing group
so only match this group,
but not usable(indexable) later
so, here second group is not 456, but is 789

2. also, second group is omitted
so there is not index=3 group
so above use group(3) will cause error:
IndexError: no such group
        """)


###############################################################################
if __name__ == "__main__":
    python_re_non_capturing_group();