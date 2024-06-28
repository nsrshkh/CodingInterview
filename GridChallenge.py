# def gridChallenge(grid):
#     grid_len = len(grid)
#     n_grid = [sorted(list(i)) for i in grid]
#     col_len = len(n_grid[0])
#     grid_cols = [[n_grid[j][i] for j in range(grid_len)] for i in range(col_len)]
#     for i in range(col_len):
#         if grid_cols[i] != sorted(grid_cols[i]):
#             return "NO"
#     return "YES"

def gridChallenge(grid):
    grid_len = len(grid)
    n_grid = []
    s_grid = []

    for i in grid:
        n_grid.append(sorted(list(i)))
    col_len = len(n_grid[0])
    for j in range(col_len):
        s = [n_grid[k][j] for k in range(grid_len)]
        s_grid.append(s)

    for i in range(col_len):
        if s_grid[i] != sorted(s_grid[i]):
            return "NO"
    return "YES"


# grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
grid = ['mpxz', 'abcd', 'wlmf']
# grid = ['eibjbwsp', 'ptfxehaq', 'jxipvfga', 'rkefiyub', 'kalwfhfj', 'lktajiaq', 'srdgoros', 'nflvjznh']
# grid = ['lnpxeemwlqlzpxrmrmwbseqfnpkzaafdnukixaopcfvhqw', 'dhfhhoyhhzleldljmirjbqagcleivzomlpanqzsmqnrzij',
#         'zcsrvgqlmrgknqhwtcqzyldjanlczysnspvusziqtazjlu', 'idiknfqdygrwhvdzperlvgueqhuezsrwzztlodqgipnqzb',
#         'zjfyxbghvdecpzhvoxzojcpciaspyoeaetimmoccjqxtmv', 'mxwnhdyjutecwbrxdjmrbdjvbzprgnekvnvhxnuvekoflo',
#         'jjbjxzuaafatzdwlnzcorkiagrwzvrmjqqbdlmgyewzsea', 'bmvyqojhnbfrypiiwvtgifmqqdcuilohbfvkqjhlcwsfyo',
#         'zrbjhsrxnllmsdfqurkjfomwsvgfepwttohojxmrhexpmy', 'hcdxtucpeptgqhckpdxdcgpvhkiuucvwbuhtmbskqdlasw',
#         'rtocxkyrsrbluwvpfkekqkdwncvozfgmcrswpksiqmfnnl', 'xawlpinqjstxvrqvsugbvszhibbcmbdwktgwjlezakyqrr',
#         'cfghwolkahdafrcuufklziipmtkhuxdrxqlavcrxavxuas', 'plcsutiemkgfunhpyeiuvxwjppzsopglcyhgidsyhjnutp',
#         'vyyrbmfyfwpcowlpytmkvsyrzgiausrulsxtwysjgpgtqi', 'bsoknggdytplubxzjczatotnpovriwibeamjfnyxibvama',
#         'imkshtavbjpnkafuxwbzpiqlnnotrxmjepzeuwtuewtqab', 'ttjzqrcdcofkljaevmauexsxlkrxuanxgrsmsrxckixpoz',
#         'aocndkatjggduuyiksgmovthyoomrfsaxlnjouszxxoqtc', 'ahmkgizkvsbrqyricbtnpvpnibvgvnnrnqphkstvcjsbli',
#         'biasqbcofwdgabnipodjkriiyqlhaddpegkmydutcyoksk', 'avyaodwtgbdsnhheoearlinfcadeteiiudobbvqdqizcry',
#         'mhdekyvubghealrenyshjcjuhxxzimsgvukcdfdbjramzq', 'ayrzjanrebdgowsngullkgyvlgqzjexebleigxvgwjnbyf',
#         'vcpnclkhoawabjlhfnrncxfswjjmpxqcwoeqpyaitwdrjf', 'ghngenuvshwuaubahlzazwmgnsmtzyqfvvoxnhiufhxpac',
#         'ljrwslmgjilvdommuvpebcznjalxuazyujtzpewdbxjnwj', 'jqirnjnheowbioheyleyhkrcyfxuweyipumfojetmvomuz',
#         'vnnlsozyplofqkxfwcmlyntfrhspvbscocodlejqrymdeu', 'lgjcimksyragrhhagkmlnaysfxzswxfkhqzrhjlgkemmhp',
#         'weoxhopddcyiiikwblqvvcxcuxkebhywdacpmjrlkosxmw', 'bwcxxsytqdpybjxyqgmggitkgpkiytnwprsnxrygryxigo',
#         'qtwyleqxqflmaudekmdmgscfvjfwkchacxmokxrcfgwnhl', 'dgcmvhgnzigmrxougsbhwdhugyvloaqlliybbzkttmolln',
#         'jqmrfoyhwxbiyvzntvxozfswwjbeybahggfjrrzzhbapyi', 'oxbjadgrttqnfbevqolflhdpmgwgudhwfeebauqhhygvnt',
#         'kwmqirrljycddqcvjanibiarpcjjqiuvkdbdyzogbcixah', 'yyykebcfsnixcjdbkxtqvqynafmtuvoepeayiaqinvmjen',
#         'lsyxwgpfxlfkxckzsjzonxkhullkatmnwwfuicgjzbnvzf', 'vihglfapunknuitwtcxzdwjyfwqurvsydacylgcyohrbou',
#         'olmojrovoqseuqausssdupqzhbmyblomlbbqzwgbtgyiwq', 'tcshhbdgxsrtxywgqahqfimbnckwdhtbzlpwevuqjyqrbd',
#         'vjmcknagopzpwrmrianbgyhyginqduwdfjgmdqttcqroof', 'srmfsjigydlqlgsmvgqddpqmqkjzptzwdfpjmpnvgaezlx',
#         'yphbhtrmqcnrfklqmkblvginnhxxtlnnwcfuwujdqwkvaq', 'jahvrihhicrqvttmdzwbemjjqnstvtudvifdvrbjxalirj']

print(gridChallenge(grid))
