import express from 'express'
import { router } from './rotues/user.js'
const app = express()
app.set('view engine','ejs')
app.get("/",(req,res)=>{
  console.log("Here")
  res.render("index.ejs",{message:"World"})
})
app.use("/users",router)
app.listen(3000)