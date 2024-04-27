from lib.calchelper import add, multiply, get_grade


def calc_marathi(md):
    add(md, "mar.1", "3 4 5 6")
    add(md, "mar.2", "2 mar.1")
    add(md, "mar.3", "9 10 11 12")
    add(md, "mar.4", "8 mar.3")
    add(md, "mar.5", "mar.2 mar.4")
    multiply(md, "mar.6", "mar.5", 0.5)


def calc_maths(md):
    add(md, "mat.1", "72 74 76")
    add(md, "mat.2", "73 75 77")
    add(md, "mat.3", "mat.1 mat.2")
    add(md, "mat.4", "80 82 84")
    add(md, "mat.5", "81 83 85")
    add(md, "mat.6", "mat.4 mat.5")
    add(md, "mat.7", "mat.3 mat.6")
    multiply(md, "mat.8", "mat.7", 0.5)


def calc_sanskrit(md):
    add(md, "snsk.1", "15 16 17 18")
    add(md, "snsk.2", "14 snsk.1")
    add(md, "snsk.3", "21 22 23 24")
    add(md, "snsk.4", "20 snsk.3")
    add(md, "snsk.5", "snsk.2 snsk.4")
    multiply(md, "snsk.6", "snsk.5", 0.5)


def calc_hindi(md):
    add(md, "hin.1", "27 28 29 30")
    add(md, "hin.2", "26 hin.1")
    add(md, "hin.3", "33 34 35 36")
    add(md, "hin.4", "32 hin.3")
    add(md, "hin.5", "hin.2 hin.4")
    multiply(md, "hin.6", "hin.5", 0.5)


def calc_english(md):
    add(md, "eng.1", "60 61 62 63")
    add(md, "eng.2", "59 eng.1")
    add(md, "eng.3", "66 67 68 69")
    add(md, "eng.4", "65 eng.3")
    add(md, "eng.5", "eng.2 eng.4")
    multiply(md, "eng.6", "eng.5", 0.5)


def calc_hindi_sanskrit_combo(md):
    add(md, "ssh.1", "39 41 43 45")
    add(md, "ssh.2", "40 42 44 46")
    add(md, "ssh.3", "ssh.1 ssh.2")
    add(md, "ssh.4", "49 51 53 55")
    add(md, "ssh.5", "50 52 54 56")
    add(md, "ssh.6", "ssh.4 ssh.5")
    add(md, "ssh.7", "ssh.1 ssh.4")
    multiply(md, "ssh.7", "ssh.7", 0.5)
    add(md, "ssh.8", "ssh.2 ssh.5")
    multiply(md, "ssh.8", "ssh.8", 0.5)
    add(md, "ssh.9", "ssh.7 ssh.8")


def calc_science(md):
    add(md, "sci.1", "88 90 91 92")
    add(md, "sci.2", "89 93 94 95")
    add(md, "sci.3", "sci.1 sci.2")
    add(md, "sci.4", "98 100 101 102")
    add(md, "sci.5", "99 103 104 105")
    add(md, "sci.6", "sci.4 sci.5")
    add(md, "sci.7", "sci.3 sci.6")
    multiply(md, "sci.8", "sci.7", 0.5)


def calc_social_science(md):
    add(md, "soc.1", "108 109")
    add(md, "soc.2", "110 111")
    multiply(md, "soc.3", "soc.2", 0.5)
    add(md, "soc.4", "112 113")
    multiply(md, "soc.5", "soc.4", 0.5)
    add(md, "soc.6", "soc.1 soc.3 soc.5")
    add(md, "soc.7", "116 117")
    add(md, "soc.8", "118 119")
    multiply(md, "soc.9", "soc.8", 0.5)
    add(md, "soc.11", "120 121")
    multiply(md, "soc.12", "soc.11", 0.5)
    add(md, "soc.13", "soc.7 soc.9 soc.12")
    add(md, "soc.14", "soc.6 soc.13")
    multiply(md, "soc.15", "soc.14", 0.5)


def calc_technical(md):
    add(md, "tec.1", "122 123 124")
    multiply(md, "tec.2", "tec.1", 0.71428)
    add(md, "tec.3", "125 126 127")
    multiply(md, "tec.4", "tec.3", 0.71428)
    add(md, "tec.5", "tec.2 tec.4")
    multiply(md, "tec.6", "tec.5", 0.5)


def calc_arogya(md):
    add(md, "aro.1", "142 143 144 145 146")
    get_grade(md, "aro.2", "aro.1")
    add(md, "aro.3", "147 148 149 150 151")
    add(md, "aro.4", "aro.1 aro.3")
    multiply(md, "aro.5", "aro.4", 0.5)
    get_grade(md, "aro.6", "aro.5")


def calc_jals(md):
    add(md, "jals.1", "132 133 134 135 136")
    get_grade(md, "jals.2", "jals.1", 50)
    add(md, "jals.3", "137 138 139 140 141")
    add(md, "jals.4", "jals.1 jals.3")
    get_grade(md, "jals.5", "jals.4")


def calc_ncc(md):
    add(md, "ncc.1", "128 129")
    add(md, "ncc.2", "130 131")
    add(md, "ncc.3", "ncc.1 ncc.2")
    multiply(md, "ncc.4", "ncc.3", 0.5)
