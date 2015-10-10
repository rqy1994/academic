# -*- coding: utf-8 -*-
__author__ = 'rqy'

import re
import database
import login

#connect database
cur = database.conn.cursor()
sqli = "insert into info values(%s,%s,%s,%s,%s)"

#login academic system
login.loginAS()

#process data 2048
id = [ '1689', '1690', '1692', '1708', '1693', '1709', '1694', '1710', '1695', '1696', '1697', '1711', '1698', '1712', '1699', '1700', '1713', '1701', '1714', '1702', '1715', '1703', '1716', '1704', '2028', '1717', '2048', '1705', '1718', '1706', '1719', '1707', '1720', '1721', '1728', '1722', '1723', '1729', '1730', '1731', '1732', '1733', '1734', '1735', '1725', '1736', '1726', '1737', '1727', '1738', '1748', '2068', '1739', '1749', '1740', '1750', '1741', '1742', '1751', '1743', '1744', '1752', '1753', '1745', '1746', '1747', '1768', '1769', '1770', '1771', '2348', '2609', '1848', '2368', '1772', '1773', '1774', '1775', '1776', '1777', '1778', '1754', '1779', '1780', '1781', '1755', '1756', '1757', '1758', '1759', '1760', '1761', '2628', '2629', '1762', '1763', '1764', '1765', '1766', '1782', '1783', '1784', '1785', '1786', '1787', '1767', '1788', '1789', '1808', '1790', '1809', '1791', '1810', '1811', '1792', '1812', '1793', '1794', '1813', '1814', '1815', '1795', '1817', '1818', '1819', '1820', '1821', '1822', '1823', '1796', '1824', '1797', '1825', '1798', '1826', '1799', '1827', '1828', '1800', '1829', '1801']
# id = [ '1798', '1826', '1799', '1827', '1828', '1800', '1829', '1801']
schedule_url = 'http://202.118.201.228/academic/teacher/teachresource/roomschedule.jsdo'

id2 = ['1689']

for i in id:
	print i
	weeknum = 0
	from_data = {'aid':'353','buildingid':'1688','room':str(i),'Submit2':u'\u786e \u5b9a','whichweek':'-1','week':'1'}
	html = login.s.post(url = schedule_url,data = from_data)
	tmp_str = re.finditer(r'<table cellpadding="0" cellspacing="1" class="infolists_tab" >(.*?)</table>',html.text,re.S)

	mark = 0

	for tmp in tmp_str:
		weeknum += 1
		mark += 1
		if mark <= 5:
			continue

		s = tmp.group()
		l = re.findall(r'<td>(.*?)</td>',s,re.S)
		cnt = 0
		for num in range(1,11):
			for week in range(1,8):
				if l[cnt] == u'\u221a':
					flag = 1
					database.cur.execute(sqli,(i,weeknum,week,num,flag))
					database.conn.commit()
					print num,week
				else:
					flag = 0
					database.cur.execute(sqli,(i,weeknum,week,num,flag))
					database.conn.commit()
				cnt += 1
		if weeknum == 7:
			break

cur.close()
database.conn.close()

print 'End'