def getTransactions(t):
    if t != 'print_it':
        global nameOfTransactions
        global dictOfCountTransactions
        global dictMoneyOfTransactions
        telephone, transactionAndSumm = t.split('-')
        nameCurrentTransaction, summCurrentTransaction = transactionAndSumm.split(':')

        if nameCurrentTransaction in nameOfTransactions:
            dictOfCountTransactions[nameCurrentTransaction] = dictOfCountTransactions[nameCurrentTransaction] + 1
            dictMoneyOfTransactions[nameCurrentTransaction] = dictMoneyOfTransactions[nameCurrentTransaction] + int(summCurrentTransaction)
        else:
            dictOfCountTransactions[nameCurrentTransaction] = 1
            dictMoneyOfTransactions[nameCurrentTransaction] = int(summCurrentTransaction)
            nameOfTransactions.append(nameCurrentTransaction)
    else:
        for i in nameOfTransactions:
            print(dictOfCountTransactions[i], i, dictMoneyOfTransactions[i])



nameOfTransactions = []
dictOfCountTransactions = dict()
dictMoneyOfTransactions = dict()


getTransactions('12345-перевод:1000')
getTransactions('12345-перевод:2000')
getTransactions('12345-оплата жкх:2000')
getTransactions('12544334343-перевод:500')
getTransactions('673857-оплата жкх:300')
getTransactions('print_it')
