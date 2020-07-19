import pandas as pd


table1_test = pd.read_csv('table1.csv',)
data = pd.DataFrame(table1_test)

table2_test = pd.read_csv('table2.csv')
data2 = pd.DataFrame(table2_test)

#1. SELECT * FROM data;
#print(data)

#2. SELECT * FROM data LIMIT 10;
print(data.loc[:9])

#3. SELECT id FROM data;  //id 是 data 表的特定一列
print(data.loc[:,:'id'])

data2 = pd.DataFrame(table1_test,columns=['id'])
print(data2)

#4. SELECT COUNT(id) FROM data;
print(data.shape[0])

#5. SELECT * FROM data WHERE id<1000 AND age>30;
print(data[data.id < 1000 and data.age > 30])
print( data[ (data['id'] < 10000) & (data['age'] > 30)] )
print(data2)

#6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print(data.groupby('id')['order_id'].nunique())


#7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
print(pd.merge(data, data2, on='id'))

#8. SELECT * FROM table1 UNION SELECT * FROM table2;
print(pd.concat([data,data2]))

#9. DELETE FROM table1 WHERE id=10;
print(data.drop(index=9))
print(data.drop(data[data['id'] == 10].index))

#10. ALTER TABLE table1 DROP COLUMN column_name;
print(data.drop(columns='name'))