console.log('status.js is connected..!');

// get the  status of each employee
const allStatus = document.querySelectorAll(".status");

// setting the colors for different type of status 

allStatus.forEach(status => {
  if (status.innerHTML.toString().toLowerCase().includes("pending")) {
    status.parentElement.style.backgroundColor = '#fbfb9d';
    
  }else if (status.innerHTML.toString().toLowerCase().includes("approved")) {
    status.parentElement.style.backgroundColor = '#8ed18e';
    var count = status.parentElement.childElementCount - 1;
    status.parentElement.children[count].innerHTML = 'N/A'
  }else if (status.innerHTML.toString().toLowerCase().includes("rejected")) {
    status.parentElement.style.backgroundColor = '#ff9c9c';
  }
});