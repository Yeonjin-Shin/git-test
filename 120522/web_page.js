let red_btn = document.getElementById("red_btn");
let blue_btn = document.getElementById("blue_btn");
let green_btn = document.getElementById("green_btn");
let content = document.getElementById("content");
            
red_btn.addEventListener("click", ()=>{
    content.style.backgroundColor="red";
})

blue_btn.addEventListener("click", ()=>{
    content.style.backgroundColor="blue";
})

green_btn.addEventListener("click", ()=>{
    content.style.backgroundColor="green";
})