symlist = ['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'DOA', 'GOOG']
print(symlist[0])   
print(symlist[1])   
print(symlist[-1])  
print(symlist[-2])
symlist[2] = 'AIG'
print(symlist)
print(symlist[0:3])  
print(symlist[-2:])
mysyms = []
mysyms.append('GOOG')
print(mysyms)
symlist[-2:] = mysyms
print(symlist) 
