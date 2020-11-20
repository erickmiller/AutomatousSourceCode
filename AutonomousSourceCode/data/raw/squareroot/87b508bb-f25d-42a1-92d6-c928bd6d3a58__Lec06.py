# MIT600���������ѧ����̵��ۡ���2008���＾������
# ������
# ����������ocourse.org
# �γ����۰棺http://ocourse.org/bbs/forum.php?mod=forumdisplay&fid=29
# by yoeo24

def squareRootBi(x, epsilon):
    """Assume x >= 0 and epsilon > 0
       Return y s.t. y*y is within epsilon of x"""
    #����x>=0�Ҧ�>0������y��ʹ��y*y��x�Ħ���
    assert x >= 0, 'x����Ϊ�Ǹ�����������' + str(x)
    assert epsilon > 0, '�ű���Ϊ������������' + str(epsilon)
    low = 0
    high = max(x,1.0)
    #high = max(x,1)
    guess = (low + high)/2.0
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 100:
        #print 'low:', low, 'high:', high, 'guess:', guess
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high)/2.0
        ctr += 1
    assert ctr <=100, 'ѭ����������������Χ'
    print 'Bi������ѭ����', ctr, '��ֵ', guess
    return guess

def testBi():
    print '     squareRoot(4, 0.0001)'
    squareRootBi(4, 0.0001)
    print '     squareRoot(9, 0.0001)'
    squareRootBi(9, 0.0001)
    print '     squareRoot(2, 0.0001)'
    squareRootBi(2, 0.0001)
    print '     squareRoot(0.25, 0.0001)'
    squareRootBi(0.25, 0.0001)

def squareRootNR(x, epsilon):
    """Assume x >= 0 and epsilon > 0
       Return y s.t. y*y is within epsilon of x"""
    #����x>=0�Ҧ�>0������y��ʹ��y*y��x�Ħ���
    assert x >= 0, 'x����Ϊ�Ǹ�����������' + str(x)
    assert epsilon > 0, '�ű���Ϊ������������' + str(epsilon)
    x = float(x)
    guess = x/2.0
    #guess = 0.001
    diff = guess**2 -x
    ctr = 1
    while abs(diff) > epsilon and ctr <= 100:
        #print '��ֵ:', diff, '����ֵ:', guess
        guess = guess - diff/(2.0*guess)
        diff = guess**2 - x
        ctr += 1
    assert ctr <=100, 'ѭ����������������Χ'
    print 'NR������ѭ����', ctr, '��ֵ', guess
    return guess

def compareMethods():
    print '     squareRoot(2, 0.01)'
    squareRootBi(2, 0.01)
    squareRootNR(2, 0.01)
    raw_input()
    print '     squareRoot(2, 0.0001)'
    squareRootBi(2, 0.0001)
    squareRootNR(2, 0.0001)
    raw_input()
    print '     squareRoot(2, 0.000001)'
    squareRootBi(2, 0.000001)
    squareRootNR(2, 0.000001)
    raw_input()
    print '     squareRoot(123456789, 0.0001)'
    #ע�⣬�˴��������ֲ��ȣ���ֻ������Ļ�ϵ�¼�������������и���
    squareRootBi(123456789, 0.0001)
    squareRootNR(123456789, 0.0001)
    raw_input()
    print '     squareRoot(123456789, 0.0000001)'
    squareRootBi(123456789, 0.0000001)
    squareRootNR(123456789, 0.0000001)
    raw_input()
    print '     squareRoot(2736336100, 0.0001)'
    squareRootBi(2736336100, 0.0001)
    squareRootNR(2736336100, 0.0001)
    raw_input()

def showLists():
    Techs = ['MIT', 'Cal Tec']
    print Techs
    raw_input()
    Ivys = ['Harvard', 'Yale', 'Brown']
    print Ivys
    raw_input()
    Univs = []
    Univs.append(Techs)
    print Univs
    raw_input()
    Univs.append(Ivys)
    print Univs
    raw_input()
    for e in Univs:
        print e
        for c in e: print c
    raw_input()
    Univs = Techs + Ivys
    print Univs
    raw_input()
    Univs.remove('Harvard')
    print Univs
