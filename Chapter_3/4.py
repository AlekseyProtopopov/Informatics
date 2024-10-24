symlist = ['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'DOA', 'GOOG']
symlist.append('RHT')
print(symlist)

symlist.insert(1, 'AA')
print(symlist)

symlist.remove('MSFT')
print(symlist)

symlist.append('YHOO')
print(symlist)

index_yhoo = symlist.index('YHOO')
print(index_yhoo)  
print(symlist[index_yhoo])

count_yhoo = symlist.count('YHOO')
print(count_yhoo)

symlist.remove('YHOO')
print(symlist)
