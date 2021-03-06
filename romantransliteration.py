"""
    Author: Saimon
    Email: saimoncse19@gmail.com

"""


vowel_signs = ["া", "ি", "ী", "ু", "ূ", "ৃ", "ৄ", "ে", "ৈ", "ো", "ৌ"]

vowel_signs.append("্")


def romanize(text: str):
    """

    :param text: bengali text
    :return: romanized version of bengali text
    """
    new_text = ""
    for x, i in enumerate(text):
        if i == "অ":
            new_text += "a"

        elif i == 'আ' or i == "া":
            new_text += "ā"

        elif i == 'ই' or i == "ি":
            new_text += "i"

        elif i == 'ঈ' or i == "ী":
            new_text += "ī"

        elif i == 'উ' or i == "ু":
            new_text += "u"

        elif i == 'ঊ' or i == "ূ":
            new_text += "ū"

        elif i == 'ঋ' or i == "ৃ":
            new_text += "ṛ"

        elif i == 'এ' or i == "ে":
            new_text += "e"

        elif i == 'ঐ' or i == "ৈ":
            new_text += "ai"

        elif i == 'ও' or i == "ো":
            new_text += "o"

        elif i == 'ঔ' or i == "ৌ":
            new_text += "au"

        elif i == 'ঃ':
            new_text += "ḥ"

        elif i == 'ং':
            new_text += "ṁ"

        elif i == 'ঁ':
            new_text += "ɱ"

        elif i == '্য':
            if text[x+1] not in vowel_signs:
                new_text += "ya"
            else:
                new_text += "y"

        elif i == '্ব':
            new_text += "v"

        elif i == '্':
            new_text += ""

        elif i == '"ৎ"':
            new_text += "TH"

        elif i == "ক":
            if text[x+1] not in vowel_signs:
                new_text += "ka"
            else:
                new_text += "k"

        elif i == 'খ':
            if text[x + 1] not in vowel_signs:
                new_text += "kha"
            else:
                new_text += "kh"

        elif i == 'গ':
            if text[x + 1] not in vowel_signs:
                new_text += "ga"
            else:
                new_text += "g"

        elif i == 'ঘ':
            if text[x + 1] not in vowel_signs:
                new_text += "gha"
            else:
                new_text += "gh"

        elif i == 'ঙ':
            new_text += "ṅ"

        elif i == 'চ':
            if text[x + 1] not in vowel_signs:
                new_text += "ca"
            else:
                new_text += "c"

        elif i == 'ছ':
            if text[x + 1] not in vowel_signs:
                new_text += "cha"
            else:
                new_text += "ch"

        elif i == 'জ':
            if text[x + 1] not in vowel_signs:
                new_text += "ja"
            else:
                new_text += "j"

        elif i == 'ঝ':
            if text[x + 1] not in vowel_signs:
                new_text += "jha"
            else:
                new_text += "jh"

        elif i == 'ঞ':
            if text[x + 1] not in vowel_signs:
                new_text += "ña"
            else:
                new_text += "ñ"

        elif i == 'ট':
            if text[x + 1] not in vowel_signs:
                new_text += "ṭa"
            else:
                new_text += "ṭ"

        elif i == 'ঠ':
            if text[x + 1] not in vowel_signs:
                new_text += "ṭha"
            else:
                new_text += "ṭh"

        elif i == 'ড':
            if text[x + 1] not in vowel_signs:
                new_text += "ḍa"
            else:
                new_text += "ḍ"

        elif i == 'ড়':
            if text[x + 1] not in vowel_signs:
                new_text += "ḏa"
            else:
                new_text += "ḏ"

        elif i == 'ঢ':
            if text[x + 1] not in vowel_signs:
                new_text += "ḍha"
            else:
                new_text += "ḍh"

        elif i == 'ঢ়':
            if text[x + 1] not in vowel_signs:
                new_text += "ḏha"
            else:
                new_text += "ḏh"

        elif i == 'ণ':
            if text[x + 1] not in vowel_signs:
                new_text += "ṇa"
            else:
                new_text += "ṇa"

        elif i == 'ত':
            if text[x + 1] not in vowel_signs:
                new_text += "ta"
            else:
                new_text += "t"

        elif i == 'থ':
            if text[x + 1] not in vowel_signs:
                new_text += "tha"
            else:
                new_text += "th"

        elif i == 'দ':
            if text[x + 1] not in vowel_signs:
                new_text += "da"
            else:
                new_text += "d"

        elif i == 'ধ':
            if text[x + 1] not in vowel_signs:
                new_text += "dha"
            else:
                new_text += "dh"

        elif i == 'ন':
            if text[x + 1] not in vowel_signs:
                new_text += "na"
            else:
                new_text += "n"

        elif i == 'প':
            if text[x + 1] not in vowel_signs:
                new_text += "pa"
            else:
                new_text += "p"

        elif i == 'ফ':
            if text[x + 1] not in vowel_signs:
                new_text += "pha"
            else:
                new_text += "ph"

        elif i == 'ব':
            if text[x + 1] not in vowel_signs:
                new_text += "ba"
            else:
                new_text += "b"

        elif i == 'ভ':
            if text[x + 1] not in vowel_signs:
                new_text += "bha"
            else:
                new_text += "bh"

        elif i == 'ম':
            if text[x + 1] not in vowel_signs:
                new_text += "ma"
            else:
                new_text += "m"

        elif i == 'য':
            if text[x + 1] not in vowel_signs:
                new_text += "ya"
            else:
                new_text += "y"

        elif i == 'য়':
            if text[x + 1] not in vowel_signs:
                new_text += "ẏa"
            else:
                new_text += "ẏ"

        elif i == 'র':
            if text[x + 1] not in vowel_signs:
                new_text += "ra"
            else:
                new_text += "r"

        elif i == 'ল':
            if text[x + 1] not in vowel_signs:
                new_text += "la"
            else:
                new_text += "l"

        elif i == 'শ':
            if text[x + 1] not in vowel_signs:
                new_text += "śa"
            else:
                new_text += "ś"

        elif i == 'ষ':
            if text[x + 1] not in vowel_signs:
                new_text += "ṣa"
            else:
                new_text += "ṣ"

        elif i == 'স':
            if text[x + 1] not in vowel_signs:
                new_text += "sa"
            else:
                new_text += "s"

        elif i == 'হ':
            if text[x + 1] not in vowel_signs:
                new_text += "ha"
            else:
                new_text += "h"

        elif i == "্":
            new_text += ""

        else:
            new_text += i

    return new_text
