const myHeading = document.querySelector("h1");
myHeading.textContent = "Hello world!";

//A function without a name or anonymous
/*document.querySelector("html").addEventListener("click", function () {
    alert("Ouch! Stop poking me!");
  });

//an arrow functioon same as anonymous

document.querySelector("html").addEventListener("click",() => {
    alert("Ouch! Stop poking me!");
});*/


const myImage = document.querySelector("img");

myImage.onclick = () => {
  const mySrc = myImage.getAttribute("src");
  if (mySrc === "images/firefox-icon.jpeg") {
    myImage.setAttribute("src", "images/firefox2.jpeg");
  } else {
    myImage.setAttribute("src", "images/firefox-icon.jpeg");
  }
};

let myButton = document.querySelector("button");
let myHeading = document.querySelector("h1");

function setUserName() {
    const myName = prompt("Please enter your name.");
    if (!myName) {
      setUserName();
    } else {
      localStorage.setItem("name", myName);
      myHeading.textContent = `Mozilla is cool, ${myName}`;
    }
  }
  

myButton.onclick = () => {
setUserName();
};
    


  