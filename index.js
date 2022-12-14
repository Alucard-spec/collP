let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";
  setTimeout(showSlides, 2000); 
}




/*
 ! Skills Tracker
 */

let tracker={}
let addKaro =(Skill,Course)=>{
  if(Skill in tracker){
      tracker[Skill].push(Course)
  }
  else{
    tracker[Skill]=[]
    tracker[Skill].push(Course)
  }
}
