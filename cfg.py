'''配置文件'''

ROOT_DIR = 'resources'
ACTION_DISTRIBUTION = [['1', '2', '3'],
                  ['4', '5', '6', '7', '8', '9', '10', '11'],
                  ['12', '13', '14'],
                  ['15', '16', '17', '18']]


PET_ACTIONS_MAP = {'pet_1': ACTION_DISTRIBUTION}
for i in range(1, 4):
   PET_ACTIONS_MAP.update({'pet_%s' % i: ACTION_DISTRIBUTION})
# PET_ACTIONS_MAP.update({'pet_3' : ACTION_DISTRIBUTION})
