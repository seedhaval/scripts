from lib import calc_subject, calc_unit_term, calc_final


def calculate(md, type, cols):
    md['type'], md['cols'] = (type, cols)

    calc_subject.calc_marathi(md)
    calc_subject.calc_maths(md)
    calc_subject.calc_sanskrit(md)
    calc_subject.calc_hindi(md)
    calc_subject.calc_english(md)
    calc_subject.calc_hindi_sanskrit_combo(md)
    calc_subject.calc_science(md)
    calc_subject.calc_social_science(md)
    calc_subject.calc_technical(md)
    calc_subject.calc_arogya(md)
    calc_subject.calc_jals(md)
    calc_subject.calc_ncc(md)

    calc_unit_term.calc_unit_1(md)
    calc_unit_term.calc_unit_2(md)
    calc_unit_term.calc_term_1(md)
    calc_unit_term.calc_term_2(md)

    calc_final.calc_final(md)
