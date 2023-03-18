from lib.calchelper import add, oneof, get_fail_count_lt, add_comment, \
    auto_condo, get_grade, multiply

snsk_hin_cmb_nm = 'ssh.7 ssh.8'
lang_grp_nm = 'fin.mar.1 fin.hin.1 fin.eng.1'
mat_grp_nm = 'fin.mat.1 fin.sci.1'
smj_nm = 'fin.smj.1'
grade_nm = 'fin.aro.1 fin.jals.1 fin.ncc.1'
six_sub_nm = f'{lang_grp_nm} {mat_grp_nm} {smj_nm}'
all_sub_nm = f'{six_sub_nm} {grade_nm}'

all_sub_title = ['मराठी', 'हिंदी / संस्कृत', 'इंग्लिश', 'गणित', 'विज्ञान',
                 'समाजशास्त्र / टेकनिकल', 'आरोग्य व शा.शिक्षण', 'जलसंरक्षण',
                 'स्काऊट गाईड/NCC/RSP/स्व विकास कलारसास्वाद']


def calc_final_step_1(md):
    add(md, 'fin.mar.1', 'mar.6')
    oneof(md, 'fin.hin.1', 'hin.6 snsk.6 ssh.9')
    add(md, 'fin.eng.1', 'eng.6')
    add(md, 'fin.mat.1', 'mat.8')
    add(md, 'fin.sci.1', 'sci.8')
    oneof(md, 'fin.smj.1', 'soc.15 tec.6')
    add(md, 'fin.aro.1', 'aro.4')
    add(md, 'fin.jals.1', 'jals.4')
    add(md, 'fin.ncc.1', 'ncc.4')


def calc_final_combined_lang(md):
    get_fail_count_lt(md, 'tmp.lang.fail.cnt', '', lang_grp_nm, 35)
    get_fail_count_lt(md, 'tmp.lang.lt.25.cnt', '', lang_grp_nm, 25)
    get_fail_count_lt(md, 'tmp.lang.lt.25.cnt2', '', snsk_hin_cmb_nm, 13)
    md['tmp.lang.lt.25.cnt'] += md.get('tmp.lang.lt.25.cnt2', 0)
    add(md, 'tmp.lang.total', lang_grp_nm)

    if md['tmp.lang.lt.25.cnt'] > 0 or md['tmp.lang.total'] < 105:
        md['tmp.lang.combined.pass'] = False
        return
    md['tmp.lang.combined.pass'] = True
    if md['tmp.lang.fail.cnt'] > 0:
        add_comment(md, "Combined passing भाषा गट")


def calc_final_combined_maths(md):
    get_fail_count_lt(md, 'tmp.maths.fail.cnt', '', mat_grp_nm, 35)
    get_fail_count_lt(md, 'tmp.maths.lt.25.cnt', '', mat_grp_nm, 25)
    add(md, 'tmp.maths.total', mat_grp_nm)

    if md['tmp.maths.lt.25.cnt'] > 0 or md['tmp.maths.total'] < 70:
        md['tmp.maths.combined.pass'] = False
        return
    md['tmp.maths.combined.pass'] = True
    if md['tmp.maths.fail.cnt'] > 0:
        add_comment(md, "Combined passing गणित गट")


def calc_final_auto_condo(md):
    for i, v in enumerate(all_sub_nm.split()):
        auto_condo(md, v, all_sub_title[i])


def add_grace_req(md, start, grace_req, ar):
    for sub in ar:
        if start <= md[sub] < 35:
            grace_req.append([sub, round(35 - md[sub], 2)])


def get_grace_required(md):
    start = 15 if md['additional_grace'].lower().strip() == 'yes' else 25
    grace_req = []
    if md['tmp.lang.combined.pass'] == False:
        add_grace_req(md, start, grace_req, lang_grp_nm.split())
    if md['tmp.maths.combined.pass'] == False:
        add_grace_req(md, start, grace_req, mat_grp_nm.split())
    add_grace_req(md, start, grace_req, [smj_nm])
    return grace_req


def apply_grace(md, grace_req):
    avlbl_grace = 20
    grace_applied = {}
    for sub, req in sorted(grace_req, key=lambda x: x[1]):
        if req < avlbl_grace:
            grace_applied[sub] = [md[sub], req]
            avlbl_grace -= req
            md[sub] += req
        else:
            break
    md['grace_applied'] = grace_applied


def calc_grace(md):
    md['grace_applied'] = {}
    add(md, 'tmp.6.total', six_sub_nm)
    get_fail_count_lt(md, 'tmp.total.fail.cnt', '', six_sub_nm, 35)
    if md['tmp.6.total'] < 210 or md['tmp.total.fail.cnt'] == 0:
        return
    grace_req = get_grace_required(md)
    apply_grace(md, grace_req)


def add_grace_comment(md):
    for i, sub in enumerate(all_sub_nm.split()):
        if sub in md['grace_applied']:
            grace = md['grace_applied'][sub][1]
            if grace <= 10:
                add_comment(md, f"Grace - {all_sub_title[i]}")
            else:
                add_comment(md, f"Extra Grace - {all_sub_title[i]}")


def get_ledger_remark(md):
    passed = True
    get_fail_count_lt(md, 'tmp.lang.fail.cnt', '', lang_grp_nm, 35)
    get_fail_count_lt(md, 'tmp.mat.fail.cnt', '', mat_grp_nm, 35)
    if md['tmp.lang.fail.cnt'] > 0 and md['tmp.lang.combined.pass'] == False:
        passed = False
    if md['tmp.mat.fail.cnt'] > 0 and md['tmp.maths.combined.pass'] == False:
        passed = False
    if md[smj_nm] < 35:
        passed = False
    if md['tmp.final.fail.cnt'] == 0:
        val = 'उत्तीर्ण'
        md['final.pass.status'] = 'उत्तीर्ण'
    elif passed == True:
        val = f"F{md['tmp.final.fail.cnt']} उत्तीर्ण"
        md['final.pass.status'] = 'उत्तीर्ण'
    else:
        val = f"F{md['tmp.final.fail.cnt']} जून पुनर्परीक्षेस पात्र"
        md['final.pass.status'] = 'जून पुनर्परीक्षेस पात्र'
    md['fin.rem.l1'] = val


def get_final_report_text(md):
    for sub in six_sub_nm.split():
        r_sub = sub.replace('.1', '.r1')
        if sub in md['grace_applied']:
            md[r_sub] = f"{md[sub]}#"
        else:
            md[r_sub] = md[sub]


def get_final_ledger_text(md):
    for sub in six_sub_nm.split():
        l_sub = sub.replace('.1', '.l1')
        if sub in md['grace_applied']:
            marks, reqg = md['grace_applied'][sub]
            md[l_sub] = f"{marks} + {reqg}"
        else:
            md[l_sub] = md[sub]

    for sub in grade_nm.split():
        l_sub = sub.replace('.1', '.l1')
        get_grade(md, l_sub, sub)

    add(md, 'fin.grp.l1', lang_grp_nm)
    add(md, 'fin.grp.l2', mat_grp_nm)
    add(md, 'fin.total.l1', f'fin.grp.l1 fin.grp.l2 {smj_nm}')
    multiply(md, 'fin.100.l1', 'fin.total.l1', 1.0 / 6.0)
    add_grace_comment(md)
    get_ledger_remark(md)


def calc_final(md):
    md['fin.cmnt'] = ''
    calc_final_step_1(md)
    add(md, 'tmp.final.calc.req', six_sub_nm)
    if not 'tmp.final.calc.req' in md:
        return
    calc_final_auto_condo(md)
    calc_final_combined_lang(md)
    calc_final_combined_maths(md)
    calc_grace(md)
    get_fail_count_lt(md, 'tmp.final.fail.cnt', '', six_sub_nm, 35)
    get_final_ledger_text(md)
    get_final_report_text(md)
    md['fin.cmnt'] = md['fin.cmnt'].strip().strip(',')
