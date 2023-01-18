class Subject:
    """Creates instances of subjects with the required parameters"""
    def __init__(self, course_code, course_title, credit_unit):
        self.course_code = course_code.upper()
        self.course_title = course_title.upper()
        self.credit_unit = credit_unit


#year 1 first semester
bio_111 = Subject('bio 111, ', 'general biology i', 3)
chm_111 = Subject('chm 111, ', 'general chemistry i (physical and inorganic)', 3)
phy_111 = Subject('phy 111, ', 'general physics i', 2)
mth_111 = Subject('mth 111, ', 'general mathematics i',3)
ict_101 = Subject('ict 101, ', 'introduction to computer', 2)
eng_101 = Subject('eng 101, ', 'use of english', 2)
ctz_101 = Subject('ctz 101, ', 'citizenship', 2)
etp_101 = Subject('etp 101, ', 'introduction to entrepreneurship', 1)
bdt_151 = Subject('bdt 151, ', 'introduction to laboratory techniques', 2)
ptp_111 = Subject('ptp 111, ', 'introduction to principles of pharmacy technician practice', 2)

#year 1 second semester
bio_112 = Subject('bio 112, ', 'general biology ii', 3)
chm_112 = Subject('chm 112, ', 'general chemistry ii (organic chemistry)', 3)
phy_112 = Subject('phy 112, ', 'general physics ii', 2)
bio_122 = Subject('bio 122, ', 'general biology practical', 1)
chm_122 = Subject('chm 122, ', 'general chemistry practical', 1)
phy_122 = Subject('phy 122, ', 'general physics practical', 1)
mth_112 = Subject('mth 112, ', 'general mathematics ii', 2)
eng_102 = Subject('eng 102, ', 'communication skills', 2)
aum_122 = Subject('aum 122, ', 'introduction to action and uses of medicines', 3)
bdt_152 = Subject('bdt 152, ', 'basic dispensing theory i', 3)
mcb_112 = Subject('mcb 112, ', 'basic microbiology i', 2)

#year 2 first semester
aum_221 = Subject('aum 221, ', 'action and uses of medicines i', 3)
bdt_251 = Subject('bdt 251, ', 'basic dispensing theory ii', 3)
bdt_253 = Subject('bdt 253, ', 'pharmaceutical calculations', 3)
ana_241 = Subject('ana 241, ', 'anatomy and physiology i', 3)
bdp_231 = Subject('bdp 231, ', 'basic dispensing practical i', 3)
phc_201 = Subject('phc 201, ', 'primary health care i', 2)
sta_211 = Subject('sta 211, ', 'introduction to statistics', 2)
mcb_211 = Subject('mcb 211, ', 'basic microbiology ii', 1)
bdt_255 = Subject('bdt 255, ', 'logistics and supply chain management system', 2)

#year 2 second semester
aum_222 = Subject('aum 222, ', 'action and uses of medicines ii', 3)
bdt_252 = Subject('bdt 252, ', 'basic dispensing theory iii', 2)
bdp_232 = Subject('bdp 232, ', 'basic dispensing practical ii', 3)
ana_242 = Subject('ana 242, ', 'anatomy and physiology ii', 3)
bdt_254 = Subject('bdt 254, ', 'logistics and supply chain management ii', 2)
psy_202 = Subject('psy 202, ', 'introduction to psychology', 2)
etp_202 = Subject('etp 202, ', 'practice of entrepreneurship', 3)

#year 3 first semester
hcp_361 = Subject('hcp 361, ', 'hospital community and industrial practice', 6)
bdp_331 = Subject('bdp 331, ', 'basic dispensing practical iii', 3)
bdt_351 = Subject('bdt 351, ', 'basic dispensing theory iv', 3)
aum_321 = Subject('aum 321, ', 'action and uses of medicines iii', 3)
ict_301 = Subject('ict 301, ', 'computer application in pharmacy', 2)
sem_301 = Subject('sem 301, ','seminar presentation i', 2)

#year 3 second semester
ana_342 = Subject('ana 342, ', 'anatomy and physiology iii', 3)
phc_302 = Subject('phc 302, ', 'primary health care ii', 2)
ptp_312 = Subject('ptp 312, ', 'principles of pharmacy technician practice ii', 2)
aum_322 = Subject('aum 322, ', 'action and uses of medicines iv', 3)
bdp_332 = Subject('bdp 332, ', 'basic dispensing practical iv', 3)
bdt_352 = Subject('bdt 352, ', 'basic dispensing theory v', 3)
sem_302 = Subject('sem 302, ','seminar presentation ii', 2)