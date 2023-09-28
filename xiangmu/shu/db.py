import pymysql

class Mysql(object):
	def __init__(self):
		try:
			self.db = pymysql.Connect(
				host = '127.0.0.1',
				port = 3306,
				user = 'root',
				password = '1',
				database = 'demo',
			)
			self.youbiao = self.db.cursor()
			print('连接成功')
		except:
			print('连接失败')

	def get_data(self):
		self.youbiao.execute('SELECT * FROM biao')
		result = self.youbiao.fetchall()
		
		return result
	
	def add_data(self, name, val):
		self.youbiao.execute('INSERT INTO biao (name, val) VALUES (%s, %s)',(name,val))
		self.youbiao.execute('SELECT * FROM biao WHERE name = %s',(name,))
		self.youbiao.connection.commit()
		
		return self.get_data()

	def del_data(self, id):
		self.youbiao.execute('DELETE FROM biao WHERE id = %s',(id,))
		self.youbiao.connection.commit()
	
		return self.get_data()

	def close_db(self):	
		self.db.close()
