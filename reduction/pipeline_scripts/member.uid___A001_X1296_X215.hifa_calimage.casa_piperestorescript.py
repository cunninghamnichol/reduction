from recipes.almahelpers import fixsyscaltimes # SACM/JAO - Fixes
__rethrow_casa_exceptions = True
h_init()
try:
    hifa_importdata (dbservice=False, bdfflags=False, vis=['../rawdata/uid___A002_Xcf0c6b_X4bbc'], session=['session_1'], ocorr_mode='ca')
    fixsyscaltimes(vis = 'uid___A002_Xcf0c6b_X4bbc.ms')# SACM/JAO - Fixes
    h_save() # SACM/JAO - Finish weblog after fixes
    h_init() # SACM/JAO - Restart weblog after fixes
    hifa_restoredata (vis=['uid___A002_Xcf0c6b_X4bbc'], session=['session_1'], ocorr_mode='ca')
finally:
    h_save()
