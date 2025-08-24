def str_replace(text,ch):
    result = ''
    for i in text: 
            if i == ' ': 
                i = ch  
            result += i 
    return result

text = "D t C mpBl ckFrid yS le"
ch = "a"

result = str_replace(text, ch)
print(result)
# 'DataCampBlackFridaySale'