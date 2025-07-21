import Database from "better-sqlite3";
const db = new Database("myapp.db")
// const query = `CREATE TABLE users(
// id INTEGER PRIMARY KEY,
// name STRING NOT NULL,
// username STRING NOT NULL UNIQUE,
// phone INTEGER NOT NULL)`
// db.exec(query)
// const data = [
//     {name:"Meer",username:"meer11",phone:'03204522701'},
//     {name:"Meer1",username:"meerhoj",phone:'03204522702'},
//     {name:"Meer2",username:"meer11w",phone:'03204522703'},
//     {name:"Meer3",username:"meer11e",phone:'03204522704'}
// ];
// const insertData = db.prepare("INSERT INTO users(name,username,phone)VALUES(?,?,?)" )
// data.forEach((user)=>{
//     insertData.run(user.name,user.username,user.phone)
// });
// const query = 'SELECT * FROM users'
// const user = db.prepare(query).all()
// console.log(user)


import express from 'express'
const app = express()
const port = 3000

app.get('/', (req, res) => {
    const query = 'SELECT * FROM users'
const user = db.prepare(query).all()
  res.json({users:user})
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

