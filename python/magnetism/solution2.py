nDots = 20
for i in range(nDots):
    x = np.random.uniform()*6-3
    y = np.random.uniform()*6-3
    dx = np.random.uniform()*0.4-0.2
    dy = np.random.uniform()*0.4-0.2
    xList = [x, x + dx]
    yList = [y, y + dy]
    # print xList, yList
    theChart.plot(xList, yList, '-', c='g')
    # theChart.plot(xList, yList, 'o-', c='r')
    # theChart.plot(xList, yList, 'o', c='b')
    # 
    # Another formatting control is linewidth 'lw':
    #
    # theChart.plot(xList, yList, 'o-', lw='4', c='b')

