import express from 'express';
const router = express.Router()
router.get('/',(req,res)=>{
    res.send("This is a User")
})
router.get('/new',(req,res)=>{
    res.send("This is another users")
})

export {router}
